# Purpose of Project:
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. They have a directory having json log files of user activity; and another directory of json metadada files of songs. We created a Postgres database with tables designed to optimize queries on song play analysis.
Our was a star schema with a fact table- songplay; and dimesion tables- user, song, artist time. We also built an ETL pipeline in Python to transfer data in our data warehouse.

# Database Schema Design and ETL Pipeline
Several attrributes like song_id, artist_id, user_id etc. were used as foreign keys in the fact table. Although we did not specifically define foreign keys in the Postgress database but the use was equivalent. 
We wrote the queries to drop and create tables in the sql_queries.py file. We extracted data from the json files in the etl.ipynb file and passed the extraced data in the Insert SQL queries. We also had to extract dat and time from the ts column.
The most challenging SQL query was to write a join between songs and artist table while passing parameters like song, artist, length
from the json log files. The major step for each ETL operation was to read the data from the json file, convert into a data frame of only required columns anf then transferring that data into the tables.
