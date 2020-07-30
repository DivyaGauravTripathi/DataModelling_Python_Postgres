# DROP TABLES

songplay_table_drop = "Drop table If Exists songplays " 
user_table_drop = "Drop table If Exists users"
song_table_drop = "Drop table If Exists songs"
artist_table_drop = "Drop table If Exists artists"
time_table_drop = "Drop table If Exists time"

# CREATE TABLES

songplay_table_create = ("""Create Table If Not Exists songplays (songplay_id serial primary key,start_time varchar Not Null,user_id varchar Not Null,level varchar,song_id varchar,artist_id varchar, session_id varchar, location varchar,user_agent varchar)""")

user_table_create = ("""Create Table If Not Exists users(user_id int primary key,first_name varchar not null,last_name varchar not null,gender varchar,level varchar not null)""")

song_table_create = ("""Create Table If Not Exists songs (song_id varchar primary key,title varchar not null,artist_id varchar not null,year varchar,duration numeric)""")

artist_table_create = ("""Create Table If Not Exists artists (artist_id varchar primary key,name varchar not null,location varchar,latitude varchar,longitude varchar)""")

time_table_create = ("""Create Table If Not Exists time (start_time varchar primary key,hour int not null,day int not null,week int not null,month int not null,year int not null,weekday varchar not null)""")

# INSERT RECORDS

songplay_table_insert = ("""Insert into songplays (start_time,user_id,level,song_id,artist_id, session_id, location,user_agent)
Values(%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""Insert into users (user_id,first_name,last_name,gender,level) Values(%s,%s,%s,%s,%s) ON CONFLICT (user_id) 
Do Update Set Level = Excluded.Level;
""")

song_table_insert = ("""Insert Into songs (song_id,title,artist_id,year,duration) Values(%s,%s,%s,%s,%s) ON CONFLICT (song_id) 
Do Nothing;
""")

artist_table_insert = ("""Insert Into artists (artist_id,name,location,latitude,longitude ) Values(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) 
Do Nothing;
""")


time_table_insert = ("""Insert into time(start_time,hour,day,week,month,year,weekday) Values(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) 
Do Nothing;
""")

# FIND SONGS

song_select = ("""Select songs.song_id,artists.artist_id From songs Join artists on songs.artist_id = artists.artist_id WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;
""")

# QUERY LISTS 

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]