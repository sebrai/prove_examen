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

### uploaded file

#### get a file

- **path:** *"/get/'file_id' "*
- **uses:**

``` html
 <img src="http://host:port/get/file_id">
```

#### download a file

- **path:** *"/download/'file_id' "*
- **preview:**
*image to be placed*

### hosting

- *waitress*

#### running in treminal

``` Bash
waitress-serve --port=8080 app:app
```

#### hosting from file

``` python
from waitress import serve


serve(app, host='0.0.0.0', port=5000)
```

### install guide

1. *requires git to copy*

    ``` Bash
    winget install --id Git.Git -e --source winget
    git --version
    ```

2. *install python if you havent already*

    ``` Bash
       sudo apt install python3 python3-venv

    ```

3. *clone the projekt*

    ``` Bash
    git clone https://github.com/sebrai/prove_examen.git
    ```

4. *create enviorment*

    ``` Bash
     cd prove_examen/
     python# -m venv .venv
    ```

5. *install libraries*

    ``` Bash
    pip install -r req.txt
    ```

6. *adding .env*

    **add a .env file with theese lines:**

    ``` csv
    p_word = "your password"
    user = "your username"
    skey = "secret key"
    ```

    *(secret key can be anything)*

7. *running*

    ``` Bash
        python app.py
    ```
