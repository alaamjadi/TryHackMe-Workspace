# Networking: Core Protocols

**References:** DNS [RFC1035](https://www.ietf.org/rfc/rfc1035.txt), WHOIS [RFC3912](https://www.ietf.org/rfc/rfc3912.txt), HTTP [RFC2616](https://www.ietf.org/rfc/rfc2616.txt), HTTPS [REFC2660](https://www.ietf.org/rfc/rfc2660.txt), FTP [RFC959](https://www.ietf.org/rfc/rfc959.txt), SMTP [RFC5321](https://www.ietf.org/rfc/rfc5321.txt), POP3 [RFC1939](https://www.ietf.org/rfc/rfc1939.txt), IMAP [RFC9051](https://www.ietf.org/rfc/rfc9051.txt)

### 1. Protocol Overview Table

| Protocol   | Layer | Transport | Port     | Primary Function                   |
| :--------- | :---- | :-------- | :------- | :--------------------------------- |
| **DNS**    | 7     | UDP/TCP   | 53       | Maps domain names to IP addresses  |
| **HTTP**   | 7     | TCP       | 80/8080  | Unsecured web communication        |
| **HTTPS**  | 7     | TCP       | 443/8443 | Secured web communication          |
| **FTP**    | 7     | TCP       | 21       | High-speed file transfer           |
| **SMTP**   | 7     | TCP       | 25       | Sending/transferring email         |
| **POP3**   | 7     | TCP       | 110      | Retrieving email (Local download)  |
| **IMAP**   | 7     | TCP       | 143      | Synchronizing email (Server-based) |
| **TELNET** | 7     | TCP       | 23       | Remote terminal connection         |

### 2. DNS (Domain Name System)

DNS translates human-readable domain names into machine-readable IP addresses.

#### Common Record Types:

- **A**: Maps a hostname to one or more IPv4 addresses.
- **AAAA**: Similar to A Record, but for IPv6
- **CNAME**: Maps one domain name to another (alias).
- **MX**: Identifies the mail server responsible for the domain.

**Commands:** `nslookup <domain.tld>` or `dig <domain.tld>`

### 3. WHOIS

Provides public registration data for domain entities. It includes registration dates and contact info for the registrant, unless protected by a privacy service.

**Commands:** `whois <domain.tld>`

### 4. HTTP & HTTPS

Defines communication between web browsers and servers using specific methods.

#### Methods:

- **GET**: Retrieves data (HTML, images) from the server.
- **POST**: Submits new data (forms, uploads) to the server.
- **PUT**: Creates or overwrites resources on the server.
- **DELETE**: Removes specified resources from the server.

#### CLI:

```shell
telnet <host> 80
GET / HTTP/1.1
Host: <domain>
```

### 5. FTP (File Transfer Protocol)

- **Ports:** FTP server listens on port 21, but actual data transfer occurs over a separate secondary connection.

**Commands:** `USER`/`PASS`: authentication, `RETR`: Download a file (Retrieve), `STOR`: Upload a file (Store), `type ascii`: Switches to text transfer mode.

#### CLI:

```shell
ftp <host>
<username> (or anonymous)
<password> (or press enter for anonymous user)
type ascii (switching to ASCII mode)
get <file_name>
pwd (or ls, cd, pwd)
close (or bye)
```

### 6. Email Protocols (SMTP vs. POP3 vs. IMAP)

#### Simple Mail Transfer Protocol (SMTP): Sending

- **Function**: Client to server, or server to server transfers.
- **Commands**: `HELO`: initiate, `MAIL FROM`, `RCPT TO`, `DATA`: message body, `.`: end message.

#### CLI:

````shell
telnet <host> 25
HELO/EHLO <host>
MAIL FROM: <sender_email>
RCPT TO: <receiver_email>
DATA

From: <sender_email>
To: <receiver_email>
Subject: <subject>
```
<Message>
```
.
QUIT
````

#### Post Office Protocol version 3 (POP3): Retrieving

- **Function**: Downloads email to a local client; typically deletes the copy from the server.
- **Commands**: `USER`/`PASS`: authentication, `STAT`: check size, `LIST`: lists all messages and their sizes, `RETR`: retrieves the specified message, `DELE`: marks a message for deletion, `QUIT`: ends the POP3 session applying changes, such as deletions.

#### CLI:

```shell
telnet <ip_address> 110
AUTH
USER <username>
PASS <password>
STAT
LIST
RETR <message_number>
DELE <message_number>
```

#### IMAP: Synchronizing

- **Function**: Keeps messages on the server to allow synchronization across multiple devices (phone, laptop, etc.).
- **Commands**: `LOGIN <username> <password>`: authentication, `SELECT <mailbox_name>`: selects the mailbox folder to work with, `FETCH <mail_number> <data_item_name>`:retrieve specific body data (example: fetch 3 body[]), `MOVE <sequence_set> <mailbox>`: moves the specified messages to another mailbox, `COPY <sequence_set> <data_item_name>`: copies the specified messages to another mailbox, `LOGOUT`: logs out.

#### CLI:

```shell
telnet <ip_address> 143
A LOGIN <user_name> <password>
B SELECT <folder_name>
C FETCH <message_number> body[]
D LOGOUT`
```
