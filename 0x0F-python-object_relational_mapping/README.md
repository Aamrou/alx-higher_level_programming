0x0F. Python - Object-relational mapping
Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

General
Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
More Info
Install MySQLdb module version 1.3.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 5.7 in Ubuntu 14.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
Install SQLAlchemy module version 1.2.x
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'
Also, you can have this warming message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
cursor.execute(statement, parameters)  
    ```

    You can ignore it.
Tasks
0. Get all states
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below

Your code should not be executed when imported

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql -- Create states table in hbtn_0e_0_usa with some data CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa; USE hbtn_0e_0_usa; CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id) ); INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:/0x0F$ cat 0-select_states.sql | mysql -uroot -p Enter password: guillaume@ubuntu:/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa (1, 'California') (2, 'Arizona') (3, 'Texas') (4, 'New York') (5, 'Nevada') guillaume@ubuntu:~/0x0F$

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x0F-python-object_relational_mapping
File: 0-select_states.py
1. Filter states
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below

Your code should not be executed when imported

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql -- Create states table in hbtn_0e_0_usa with some data CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa; USE hbtn_0e_0_usa; CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id) ); INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:/0x0F$ cat 0-select_states.sql | mysql -uroot -p Enter password: guillaume@ubuntu:/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa (4, 'New York') (5, 'Nevada') guillaume@ubuntu:~/0x0F$

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x0F-python-object_relational_mapping
File: 1-filter_states.py
2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

You must use format to create the SQL query with the user input

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below

Your code should not be executed when imported

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql -- Create states table in hbtn_0e_0_usa with some data CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa; USE hbtn_0e_0_usa; CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id) ); INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:/0x0F$ cat 0-select_states.sql | mysql -uroot -p Enter password: guillaume@ubuntu:/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona' (2, 'Arizona') guillaume@ubuntu:~/0x0F$

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x0F-python-object_relational_mapping
File: 2-my_filter_states.py
3. SQL Injection...
Wait, do you remember the previous task? Did you test ´"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"´ as an input?

guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)

You must use the module MySQLdb (import MySQLdb)

Your script should connect to a MySQL server running on localhost at port 3306

Results must be sorted in ascending order by states.id

Results must be displayed as they are in the example below

Your code should not be executed when imported

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql -- Create states table in hbtn_0e_0_usa with some data CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa; USE hbtn_0e_0_usa; CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id) ); INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:/0x0F$ cat 0-select_states.sql | mysql -uroot -p Enter password: guillaume@ubuntu:/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona' (2, 'Arizona') guillaume@ubuntu:~/0x0F$

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x0F-python-object_relational_mapping
File: 3-my_safe_filter_states.py
