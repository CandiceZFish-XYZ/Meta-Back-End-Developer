# Database - relational

- field, record
- entity, instance of entity

- Establish relationship: Primary key, foreign key

## Week 1 Introduction to Databases

### Objectives

Database

- Outline what a database is (conceptual)
- Outline real-world examples of database usage
- Explain how data is organized in a db
- Explain importance of related data within a db
- Identify an instance of related data within a db
- Overview of new trends in db applications
- Identify diff types of dbs
- High-level overview of how db evolved

Interaction method - SQL

- Purpose of SQL
- SQL role
- Advantages of SQL and how these will assist you
- High-level overview of Syntax: DDL, DML, DQL, DCL
- Main SQL commands, CRUD

DB structure

- Concept and purpose of a db table
- Key components of a db table: columns, rows, data types, keys

### Basic DB structure

#### Tables

- Outline what a database table is (conceptual)
- How data is structured in db table

#### DDL

- `mysql -u root -p`
- `quit`

- `CREATE DATABASE db_name;`
- `USE db_name;`
- `SHOW tables;`

- `CREATE TABLE tb_name(col1 datatype(limit), col2 datatype(limit));`
- `CREATE TABLE tb_name(col1 datatype(limit), col2 datatype(limit)) PRIMARY KEY (col1) FOREIGN KEY (col2) REFERENCES (table(col2_));`
- `SHOW columns FROM table;`

## Week 2 CRUD Operations

### Data types

- Numeric Data Types
- String
- default values

### CRUD

Create and Read

- `INSERT INTO table(col1, col2) VALUES (val1, val2), (val1_1, val2_2), (val1_3, val2_3)...;`
- `SELECT * FROM table;`
- `INSERT INTO tb_A (col_A) SELECT col_B FROM tb_B;`

Update and Delete

- `UPDATE table SET col_1 = 'value_1', col_2 = 'value_2' WHERE ID = 3;`
-
- `DELETE FROM table WHERE col = 'value';`
- `DELETE FROM table;` == `TRUNCATE TABLE table;`
-
- `DROP table;`

- `ALTER TABLE table ADD FOREIGN KEY (col_name) REFERENCES table (col1_);`

## Week 3 SQL Arithmetic operators

### Operators

- `SELECT col1 + col2 FROM table;`
- `SELECT * FROM table WHERE col1 + col2 = value;`

### Sorting and filtering

- `SELECT col1, col2 FROM table WHERE col_x = value ORDER BY col_1 ASC, col_2 DESC;`
- `SELECT col1, col2 FROM table WHERE condition`

  - Comparison operators, Logical operators(BETWEEN, LIKE, IN)

- `SELECT DISTINCT col1 ...`
- `SELECT col1(DISTINCT col2) ...`

## Week 4 Database Schema

### Designing DB Schema

- Organization of data from table
- Relationship of data between tables

- known as Data modeling
- skeletons

Database schema can be broadly divided into three categories.

- Conceptual or logical schema that defines entities, attributes and relationships.
  - Entity Relationship Diagram (ER-D)
- Internal or physical schema that defines how data is stored in a secondary storage. In other words, the actual storage of data and access paths.
- External or view schema that defines different user views.

### Relational DB Design

- Entities and relation

### DB Normalization

- 1NF (data atomicity)
- 2NF (no partial dependency, FK not neccessary!)
- 3NF (no transitive dependency)
