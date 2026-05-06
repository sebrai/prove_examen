# prøve examen

## projekt: *file uploader*

### features

- *log inn*
- *register user*
- *upload files with file type,name,and contents stored in db*

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
    +----------+--------------+------+-----+---------+-------+
    | Field    | Type         | Null | Key | Default | Extra |
    +----------+--------------+------+-----+---------+-------+
    | id       | uuid         | NO   | PRI | uuid()  |       |
    | name     | varchar(255) | NO   |     | NULL    |       |
    | data     | longtext     | NO   |     | NULL    |       |
    | mimetype | varchar(255) | NO   |     | NULL    |       |
    +----------+--------------+------+-----+---------+-------+
```
