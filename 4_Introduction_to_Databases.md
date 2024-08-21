# Introduction to Databases for Back-End Development
## Module 1 
1. Database tasks
    1. store data
    2. form relationships
    3. filter data
    4. search data
    5. perform CRUD operations
3. Graph databases: 
4. Document databases: data stored as JSON objects.
5. Relational databases
    1. table 
    2. header/fields
    3. rows/records
    4. a row/instance/entity
6. Primary key: like a unique ID that cannot be replicated elsewhere in the table.
7. Foreign key: keys in one table that connects to the primary key in the original table.
8. Visualizing data through charts is a common practice in data utilization.
    1. common charts: bar, bubble, line, pie, dual axis, Gantt, heat maps, and scatter plots.
    2. the choice of chart depends on
        1. the target audience who will use the information
        2. the idea you intend to present
        3. the goal you want to achieve
9. Types of databases
    1. Relational databases (SQL database): used for storing structured data in tabular format
    2. non-relational databases (NoSQL databases): provide a flexible structure for sorting and scaling data
        1. Document databases: data stored in documents similar to JSON.
        2. Key-value databases: Each item contains keys and values.
        3. Graph databases: data stored in the form of nodes and edges.
        4. Wide-column databases: data stored in tables, rows, and dynamic columns.
    3. other database
        1. Flat files: basically text files, like CSV files.
        2. Hierarchical database: represents a one-to-many relationship; one child can only have one parent.
        3. Network databases: many-to many relationships.
        4. Object-oriented databases: data stored in the form of objects.
10. data terms
    1. Big data: complex data that grows exponentially with time
    2. cloud database
    3. Business intelligence: analyzing data and other information to make informed decisions
### Intro to SQL
1. Structured Query Language (SQL) is used to interact with relational databases/ structured data.
2. Database Management System (DBMS)
3. CRUD operations
    1. Create/insert
    2. Read
    3. Update
    4. Delete
4. SQL command can categorized into five subsets 
    1. Data Definition Language: create, alter, drop...
    2. Data Manipulation Language: insert, update, delete...
    3. Data Query Language: select
    4. Data Control Language: grant, revoke
    5. Transaction Control Language
5. Common SQL statement
```sql
-- DDL
-- create the database or tables
CREATE TABLE table_name(column_name1 DATATYPE(size), column_name2 DATATYPE(size), column_name3 DATATYPE(size));
-- delete a database or a table
DROP TABLE table_name;
-- add a column to a table
ALTER TABLE table_name ADD (column_name DATATYPE(size));
-- add a primary key to a table:
ALTER TABLE table_name ADD primary key (column_name);
-- empty the table but not delete the table itself
TRUNCATE TABLE table_name;

-- DQL
-- retrieve data from tables
SELECT * FROM table_name;

-- DML
-- add records of data into an existing table
INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
-- modify or update data contained within a table
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
-- delete data from a table
DELETE FROM table_name WHERE condition;
```
6. data types
    1. Numeric: INT, TINYINT, BIGINT, FLOAT, REAL
    2. Date and time: DATE, TIME, DATETIME
    3. Character and string: CHAR, VARCHAR
    4. Binary: BINARY, VARBINARY
    5. Miscellaneous
        1. Character Large Object (CLOB): stores a large block of text in some form of text encoding.
        2. Binary Large Object (BLOB): stores a collection of binary data such as images.
7. database components:
    1. tables or entities (or objects in OOD): the data is stored.
    2. attributes: details about the table or entity
    3. fields: columns used to capture attributes. 
    4. record: one row of details about a table. 
    5. primary key: a unique value for an entity.
8. Integrity constraints:
    1. key constraints: should never be NULL or the same for two different rows of data.
    2. domain constraints: the rules defined for the values that can be stored for a certain column.
    3. referential integrity constraints: when a table has foreign keys, the referenced column value must exist.
9. Types of keys in a database table:
    1. candidate key: unique value in each row of the table.
    2. composite key: two or more attributes to form a unique value.
    3. primary key: a selected candidate key.
    4. alternate key: a candidate key not selected as the primary key.
    5. reference a unique key in another table.
10. Table structure<br/>
<img src=".\4_resource\structure.webp" alt="SQL Table structure" width="50%"/>

## Module 2
1. Exercise use MySQL
2. MySQL data types https://www.w3schools.com/mysql/mysql_datatypes.asp
### SQL data types
1. Numeric
```sql
-- create a database
CREATE DATABASE cm_devices;
-- change to the database
USE cm_devices;
-- create a table
CREATE TABLE devices (deviceID INT, deviceName VARCHAR(50), price DECIMAL);
-- show tables in the current database
SHOW tables;
-- show "devices" table’s columns and data types.
SHOW columns FROM devices;
-- delete "devices" table
DROP TABLE devices;
```

2. String
    1. CHAR: A FIXED length string (can contain letters, numbers, and special characters). The size parameter specifies the column length in characters
    2. VARCHAR: A VARIABLE length string (can contain letters, numbers, and special characters). The size parameter specifies the **maximum** column length.
```sql
CREATE TABLE customers (username CHAR(9), fullName VARCHAR(100), email VARCHAR(255));
-- username CHAR(9) always occupoes 9 character's spaces
-- fullName VARCHAR(100) only occupies as much as the character's spaces, up to 50
SHOW TABLES;
SHOW columns FROM customers;
```

3. Database constraints: limit the type of data that can be stores in a table
    1. constraints: applied at column level
    2. rule: applied tp a specific column
```sql
-- Constraints
-- NOT NULL: data fields cannot be left empty.
-- DEFAULT: sets a default value for a column if no value is specified
CREATE TABLE address(id INT NOT NULL, street VARCHAR(255), postcode VARCHAR(10), town VARCHAR(30)  DEFAULT"Harrow");
```

4. SQL statement and syntax (MySQL)
```sql
-- CREATE DATABASE
CREATE DATABASE database_name;
-- DROP (delete) DATABASE
DROP DATABASE database_name;
-- CREATE TABLE
CREATE TABLE table_name(column_name1 DATATYPE(size), column_name2 DATATYPE(size), column_name3 DATATYPE(size));

-- ALTER (change) TABLE
-- ADD
ALTER TABLE table_name ADD(column_name DATATYPE(size));
-- DROP
ALTER TABLE table_name DROP COLUMN column_name;
-- MODIFY (change datatype)
ALTER TABLE table_name MODIFY column_name DATATYPE(size)

-- INSERT INTO
INSERT INTO table_name(column1_name, column2_name, column3_name)
VALUES
(value11, value21, value31),
(value12, value22, value32),
(value13, value23, value33);
CURRENT_DATE() -- return current date

-- SELECT
SELECT column1_name, column2_name FROM table_name
-- SELECT all_columns FROM table
SELECT * FROM table_name

-- INSERT INTO from another table
INSERT INTO target_table(column_name)
SELECT column_name
FROM source_table;

-- UPDATE
-- this update will apply to all column3 = 'value3'
-- use primary key column to update the specific record
UPDATE table_name
SET column1 = 'new_value1' , column2 = 'new_value2'
WHERE column3 = 'value3';

-- DELETE
DELETE FROM table_name
WHERE column1 = 'value1';

-- DELETE all records in table_name
DELETE FROM table_name;

-- TRUNCATE: Removes all rows value from a table
-- similar to the DELETE with no WHERE, but faster
TRUNCATE TABLE table_name;
```

## Module 3
## Module 4
## Module 5