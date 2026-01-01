# SQL : Fundamentals

A comprehensive guide to Relational Database Management Systems (RDBMS) based on the TryHackMe SQL Fundamentals course.

### 1. Database Landscape: Database Management Systems (DBMS)

Understanding the different ways data is stored and managed.

| **Category**               | **Specific Systems / Examples**                                                    |
| :------------------------- | :--------------------------------------------------------------------------------- |
| **Relational (RDBMS)**     | MySQL, MariaDB, PostgreSQL, SQLite, Microsoft SQL Server, Oracle Database, IBM Db2 |
| **Non-Relational (NoSQL)** | MongoDB (Document), Redis (Key-Value), Elasticsearch (Search), Neo4j (Graph)       |
| **Architectural Types**    | Hierarchical, Network, Object-oriented, Centralized                                |

### 2. Database & Table Navigation

Commands for interacting with the database server and exploring its contents.

- **List all databases:** `SHOW DATABASES;`
- **Create a new database:** `CREATE DATABASE <db_name>;`
- **Select a database to use:** `USE <db_name>;`
- **Identify current database:** `SELECT DATABASE();`
- **Delete a database:** `DROP DATABASE <db_name>;`
- **List tables in the current DB:** `SHOW TABLES;`
- **View table structure/columns:** `DESC <table_name>;` or `DESCRIBE <table_name>;`

### 3. Data Definition Language (DDL)

Templates for defining and modifying the structure of your data.

- **Create Table Template:**
  ```sql
  CREATE TABLE <table_name>(
  id_name INT AUTO_INCREMENT PRIMARY KEY,
    column2_name <DATATYPE> NOT NULL,
    column3_name <DATATYPE> <CONSTRAINTS>
  );
  ```
- **Example:**
  ```sql
  CREATE TABLE book_inventory(
  book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(225) NOT NULL,
    publication_date DATE
  );
  ```
- **Add a column to an existing table:**
  ```sql
  ALTER TABLE <table_name> ADD <column_name> <datatype>;
  ```

### 4. Data Manipulation & Querying (DML)

Templates for retrieving, filtering, and organizing data from tables.

#### Basic Selection & Filtering

- **Select all data of a table:** `SELECT * FROM <table_name>;` or `--SELECT _ FROM <table_name>;`
- **Select all data of a column:** `SELECT <column_name> FROM <table_name>;`
- **Select all data of multiple columns and then sorting:** `SELECT <column_name1>, <column_name2> FROM <table_name> ORDER BY <column_name1> ASC;`
- **Select unique values:** `SELECT DISTINCT <column_name> FROM <table_name>;`
- **Filter by specific criteria:** `SELECT * FROM <table> WHERE <column_name> = "value";`
- **Search for patterns (LIKE):** `SELECT * FROM <table> WHERE <column_name> LIKE "%string_pattern%";`
- **Filter by range/logic:** `SELECT * FROM <table> WHERE <column1_name> < n_value AND <column2_name> = "s_value";`
- **Inserting values into table:** `INSERT INTO table_name (column1, column2) VALUES (value1, value2);` or `INSERT INTO table_name VALUES (value1, value2);`

#### Sorting & Functions

- **Sort results:** `ORDER BY <column_name> ASC|DESC;`
- **Calculate string length:** `SELECT <column_name>, LENGTH(<column_name>) AS new_name FROM <table>;`
- **Sum a column:** `SELECT SUM(<column_name>) AS new_name FROM <table>;`
- **Find remainders (Modulo):** `WHERE MOD(<column_name>, 10) != 0;`

#### Advanced Aggregation

- **Combine multiple rows into one string:**
  ```sql
  SELECT GROUP_CONCAT(<column_name> SEPARATOR ' & ') AS new_name_value
  FROM <table_name>		--<database_name>.<table_name>
  WHERE <condition>;	--MOD(amount, 10) != 0;
  ```

### 5. Practical Query Example

The following query identifies the specific tool described as a multi-tool for pentesters and geeks:

```sql
SELECT * FROM tools_db.hacking_tools
WHERE category = "Multi-tool"
AND description LIKE "%pentesters%"
AND description LIKE "%geeks%";
```
