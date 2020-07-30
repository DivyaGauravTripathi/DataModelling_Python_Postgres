# Purpose of Project: 

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.  They have a directory having json log files of user activity; and another directory of json metadada files of songs. We created a Postgres database with tables designed to optimize queries on song play analysis.


# Database Schema Design and ETL Pipeline:

*Our was a star schema with a fact table- songplay; and dimesion tables- user, song, artist time. We also built an ETL pipeline in Python to transfer data in our data warehouse.*
 
Several attrributes like song_id, artist_id, user_id etc. which were primary key sin dimension tables were also used as foreign keys in the fact table. Although we did not specifically define foreign keys in the Postgress database like MY SQL; but the use was equivalent. 
We wrote the queries to drop and create tables in the sql_queries.py file. We extracted data from the json files in the etl.ipynb file and passed the extraced data in the Insert SQL queries. We also had to extract date and time from the ts column.
The most challenging SQL query was to write a join between songs and artist table while passing parameters like song, artist, length
from the json log files. The major step for each ETL operation was to read the data from the json file, convert into a data frame of only required columns anf then transferring that data into the tables.

# Files in Repository:

We have the following files in repository:
*sql_queries.py* - This file has SQL scripts for create, drop and insert operations in the dimension and fact tables.
*create_tables.py* - This file creates a connection and then creates Sparkify database. It then uses the SQL queries written in sql_queries.py file to drop and create dimension and fact tables.
*test.ipynb*- This file has select statements which we can run to see if rows were inserted in the tables.
*etl.ipynb*- This file has the Python scrips for ETL process. It is to run on one song json file and one log data json file. It imports the insert queries from sql_queries.py file. It extracts the data from the json files; transforms it into the trequired form and loads the data into the tables.
*etl.py*- This file combines the queries written in etl.ipynb file and run sit on all the songs json files and log data json files.

# How to run the python scripts:
1. We write queries in the sql_queries. py file.
2. We then run the create_tables from command terminal file to create the database and tables from scratch.
3. We run code blocks of the etl.ipynb file to insert data from one song json file and one log json file into the tables.
4. We run the code blocks of test.ipynb file to check if data is being inserted into our tables.
5. We run the etl.py file from command terminal to insert data from all the files into the tables.

# ERD:


