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
    5. foreign key: reference a unique key in another table.
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
-- username CHAR(9) always occupies 9 character's spaces
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
CREATE TABLE address(id INT NOT NULL, street VARCHAR(255), postcode VARCHAR(10), town VARCHAR(30) DEFAULT "Harrow");
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
1. SQL Arithmetic operators
```sql
SELECT 5 - 5 = 0;
SELECT 5 * 5 = 25;
SELECT 5 / 5 = 1;
SELECT 5 % 5 = 0;

-- return results of "column_name1 + column_name2 + 5" for every records from table_name
SELECT column_name1 + column_name2 + 5 FROM table_name;
```

2. SQL Comparison operators
    1. `=`, `>`, `>=`, `<`, `<=`
    2. `<>` or `!=` means not equal to
```sql
-- commonly used in WHERE
-- retrieve all records' columns  that "column_name1 + column_name2" equal to "0"
SELECT * 
FROM table_name
WHERE column_name1 + column_name2 = 0; 
```

3. SQL also has Logical operators
    - https://www.w3schools.com/sql/sql_operators.asp

4. ORDER BY clause
    1. used for ordering or sorting data
    2. can sorting data by multiple columns
    3. `ASC` ascending order (default)
    4. `DESC` descending order
```sql
SELECT * -- all columns
FROM table_name -- in table table_name
ORDER BY  column_name1 ASC, column_name2 DESC -- sorted by column_name1 ASC then column_name2 DESC
```

5. WHERE clause
    1. used for filer data
    2. used with operators
```sql
-- with Comparison operators
WHERE column_name1 = value1

-- with Logical operators
-- return if "Country = 'USA' AND Id <20", and "Country = 'UK'"
WHERE Country = 'USA' AND Id <20 OR Country = 'UK' ;

-- return if "date_of_birth" in "2020-01-01" to "2020-12-31"
WHERE date_of_birth BETWEEN '2020-01-01' AND '2020-12-31';

-- return if "faculty" start with "Sc"
-- ues '%' to represent multiple characters
-- ues '_' to represent one character
WHERE faculty LIKE 'Sc%' ;

-- return if "country" in the tuple "('USA', 'UK')"
WHERE country IN('USA', 'UK')
```
6. example at "4_chinook_database_customer.sql"

7. SELECT DISTINCT clause
    1. return without duplicates 
    2. can also used for distinct combinations
    3. `NULL` considered as unique values
```sql
SELECT DISTINCT column_name1
FROM table_name;

-- distinct combinations
-- might return "1, USA", "2, USA", "1, UK", "2, UK", "NULL, USA", "1, UK" "NULL, NULL"
SELECT DISTINCT Id, Country
FROM customer;

-- count how many unique values in column_name1
SELECT COUNT(DISTINCT column_name1)  
FROM table_name;
```

## Module 4
1. Schema in different DBMS
    1. MySQL: a collection of data structures within a database
    2. SQL server: a collection of individual, but related components (tables, fields, etc.)
    3. PostgreSQL: a namespace with named database objects (views, indexes, etc.)
    4. Oracle: Property of each respective database user
2. Schema concepts
    1. organization of data in the form of tables
    2. relationships between the tables
3. Schema levels ( in Entity Relationship Diagram (ER-D))
    1. external/view: how different users want to view the data
    2. conceptual/logical: defines entities, attributes, and relationships. developers work at this level
    3. internal/physical: describes how the data is really stored on disk
    4. database
4. Entity Relationship model
    1. main concepts
        1. data
        2. relationships
        3. constraints
    2. Relationships
        1. table: represents a file that stores data
        2. column/attribute: the principal storage unit
        3. domain: a set of acceptable values that a column is allowed to contain
        4. record/row/tuple: 
        5. key: an attributes for uniquely identify a specific row
        6. degree:  number of columns within a table
        7. cardinality: number of records within a table
    3. Constraints
        1. key constraints
            1. key attribute must be unique for each record
            2. key attribute cannot have NULL values
        2. Domain constraints
            1. the requirement of inserting values that have a valid data type
        3. Referential integrity constraints
            1. based on the concept of foreign keys
            2. a table refers to a key attribute of another table, that key attribute must exist
5. Types of relationships:
    1. one-to-one: a customer can only have an account
    2. one-to-many: a customer can have multiple orders, but an order can only come from a customer
    3. many-to-many: a customer can buy multiple items, and an item can be bought from many customers
6. Types of keys
    1. candidate keys: an attribute unique to each table row. It cannot be NULL.
    2. primary key: choose from the candidate keys. It would be better to ensure that it isn't modified later.
    3. composite primary key: a combination of multiple attributes if there isn't a single primary key.
    4. foreign key: columns used to connect tables.
7. Entity: an object with related attributes
8. Types of attribute
    1. simple: can not be classified further
    2. composite: can be split, e.g., Name can split into First_name and Last_name
    3. single-valued
    4. multi-valued: can store multiple values, should be avoided in a relational database
    5. derived: can be derived from another attribute, e.g., Age can be derived from Birth
    6. Key

9. Database normalization
    1. the goal is to minimize database challenges
    2. it's a process for structuring tables 
    3. minimize data duplications
    4. avoid errors during data modifications
    5. simplify data queries from the database
    6. creating each table with a single purpose

10. common database challenges/anomalies
    1. Insert anomaly: the insertion of one record leads to the insertion of several more required data sets.
    2. Update anomaly: updating data in one column requires updates in multiple others.
    3. Deletion anomaly: deletion of one record leads to the deletion of several more required data sets.

11. Database normalization form
    1. First normal form (1NF)
        1. enforce the data atomicity rule and eliminate unnecessary repeating data groups
        2. data atomicity: one single instance value of the column attribute in any field (one value per field)
        3. for example
            1. include `Tutors` in the `Courses Table` may have repeating data groups since a `Tutor` can tutor multiple `Courses`
            2. split the `Courses Table` into `Tutors Table` and `Course Table`, then connect they by foreign key
            3. a `Tutor` in the `Tutors Table` may have multiple values in `Contact infos` column
            4. split the `Contact infos` column to the `phone` column and the `email` column
    2. Second normal form (2NF)
        1. a table dependency should be functional, not partial.
        2. functional dependency: each column in the table is functionally dependent on the primary key.
        3. partial dependency: a table with a composite primary key means.
    3. Third normal form (3NF)
        1. an attribute dependency should not have a transitive dependency.
        2. transitive dependency: a non-key attribute in the table may not be functionally dependent on another non-key attribute in the same table
        3. for example
            1. the `Postcode` column attributes are functionally dependent on the `City`
            2. changing the value of the `City` in the table has a direct impact on the `Postcode` value
            3. separate the `Postcode` from the table to avoid transitive dependency
12. Database normalization form example

<img src=".\4_resource\data_normalization.png" alt="Data Normalization Example" width="50%"/>

## Module 5
1. Quiz
```sql
CREATE DATABASE SportsClub;
CREATE TABLE Players (
    playerID INT, playerName VARCHAR(50), age INT, PRIMARY KEY(playerID)
);

INSERT INTO Players (playerID, playerName, age) VALUES (1, "Jack", 25);
SELECT playerName FROM Players WHERE playerID = 2;
SELECT playerName FROM Players;
UPDATE Players SET age = 22 WHERE playerID = 3;
DELETE FROM Players WHERE playerID = 4;
SELECT playerID % 2 FROM Players;
SELECT name FROM Players WHERE age > 25;

CREATE TABLE Course( 
 courseID int NOT NULL, courseName VARCHAR(50), PRIMARY KEY (courseID), 
   FOREIGN KEY (departmentID) REFERENCES Department (departmentID)
);  

```