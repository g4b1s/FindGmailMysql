#Description

Find  occurrences of word DevOps in emails in gmail and store in mysql

#Before Start

1. Install python libs
```
pip install -r requirements.txt
```

2. Docker mysql
```
docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 -d mysql:latest

```

5. Connect in mysql and run create table
```
mysql -u root -h127.0.0.1 -p

CREATE TABLE IF NOT EXISTS email(id int(11) NOT NULL AUTO_INCREMENT, data varchar(45) NOT NULL, origem varchar(255) NOT NULL,assunto varchar(255) NOT NULL,PRIMARY KEY (id));
```

6. Use Gmail
```
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "EMAIL" + ORG_EMAIL 
FROM_PWD    = "PASSWORD"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
CRITERIA    = "DevOps"

replace EMAIL with your email username
replace PASSWORD with your email password

```

7. Run
```
python script.py
```