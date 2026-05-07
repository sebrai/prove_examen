# prøve examen

## projekt: *file uploader*

### features

- *log inn*
- *register user*
- *upload files with file type,name,and contents stored in db*
- *be able to get the uploaded file iether by a download page or though url*

### tech used

- *mariadb* (*database*)
- *flask* (*backend*)
- *jinja2* (*frontend*)
- *.env* (*env files*)

### database

**users:**

``` sql
    +----------+--------------+------+-----+---------+-------+
    | Field    | Type         | Null | Key | Default | Extra |
    +----------+--------------+------+-----+---------+-------+
    | id       | uuid         | NO   | PRI | uuid()  |       |
    | name     | varchar(31)  | NO   |     | NULL    |       |
    | email    | varchar(255) | NO   |     | NULL    |       |
    | password | varchar(255) | NO   |     | NULL    |       |
    | role     | varchar(15)  | NO   |     | user    |       |
    +----------+--------------+------+-----+---------+-------+
```

**files:**

``` sql
    +-----------+--------------+------+-----+---------+-------+
    | Field     | Type         | Null | Key | Default | Extra |
    +-----------+--------------+------+-----+---------+-------+
    | id        | uuid         | NO   | PRI | uuid()  |       |
    | name      | varchar(255) | NO   |     | NULL    |       |
    | data      | longtext     | NO   |     | NULL    |       |
    | mimetype  | varchar(255) | NO   |     | NULL    |       |
    | poster_id | uuid         | YES  | MUL | NULL    |       |
    +-----------+--------------+------+-----+---------+-------+
```

### two database hosts

**currently i have two ways to host my backend database:**

1. *external raspberry pi*
2. *wsl debian*

**both let me connect to the databse as long as:**

1. **the databse is the same in both versions of mariadb**

    *mysql dumpto extract db as sql file:*

    ``` Bash
    mariadb-dump -u [username] -p [database_name] > [filename].sql
    ```

    *using scp file tranfer:*  (*current to other*)

    ``` Powershell
    scp /path/to/local/file.txt username@remote_host:/path/to/remote/directory/
    ```

    *restore db on other machine:*

    ``` Bash
     mariadb -u [username] -p [database_name] < [filename].sql
    ```

2. **the right host addres is added into my get_db_connectin function**

    ``` python
    def get_db_connection():
        return mysql.connector.connect(
            host="correct host", # 127.0.0.1 or Localhost for debian, 10.200.14.13 for rpi
            user=user,
            password=pword, # user and pword uploaded useing dotenv
            database="uploader"
        )
    ```

### security

- **hashed passwords**
- **parametered sql**
- **backups**
