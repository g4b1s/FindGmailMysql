import smtplib
import time
import imaplib
import email
import MySQLdb


def read_email_from_gmail(cur,SMTP_SERVER,FROM_EMAIL,FROM_PWD,CRITERIA):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('Inbox')

        # type, data = mail.search(None, 'TEXT', 'INCONSTITUCIONALISSIMAMENTE')
        type, data = mail.search(None, 'ALL')
        

        mail_ids = data[0]
        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            if str(data[0][1]).find(CRITERIA) != -1:
                # print data[0][1]
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        email_date = msg['date']
                        # print 'From : ' + email_from + '\n'
                        # print 'Subject : ' + email_subject + '\n'
                        # print 'Date : ' + email_date + '\n'
                        inserdb(cur,email_from, email_subject,email_date)
    except Exception, e:
        print str(e)


def inserdb(cur, email_from, email_subject,email_date):
    sql = """INSERT INTO email(data,origem,assunto) VALUES ('"""+email_from+"""','"""+email_subject+"""','"""+email_date+"""');"""    
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()



if __name__=='__main__':
    ORG_EMAIL   = "@gmail.com"
    FROM_EMAIL  = "EMAIL" + ORG_EMAIL
    FROM_PWD    = "PASSWORD"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT   = 993
    CRITERIA    = "DevOps"

    db = MySQLdb.connect(host="127.0.0.1",  
                         user="root",      
                         passwd="secret",    
                         db="app")
    cur = db.cursor()

    read_email_from_gmail(cur,SMTP_SERVER,FROM_EMAIL,FROM_PWD,CRITERIA)
    # cur.execute("CREATE TABLE IF NOT EXISTS email(id int(11) NOT NULL AUTO_INCREMENT, data varchar(45) NOT NULL, origem varchar(255) NOT NULL,assunto varchar(255) NOT NULL,PRIMARY KEY (id))")  
