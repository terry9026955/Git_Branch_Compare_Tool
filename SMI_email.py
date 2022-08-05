from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText                # 用於製作文字內文
from email.mime.multipart import MIMEMultipart      # email內容載體
from email import encoders                          # 用於附檔編碼
from email.mime.base import MIMEBase                # 用於承載附檔
import configparser


import check_fail_log


def send_mail():
    # 讀 email.ini 的內容
    config = configparser.ConfigParser()
    config.read('email.ini')


    from_who = config['EMAIL_SENDER']['email_sender']
    to_who = config['EMAIL_RECEIVER']['email_receiver']
    
    
    # 資料設定
    email_sender = from_who
    email_receiver = to_who
    #email_receiver = "jerry.ku@siliconmotion.com"


    # 標題與內文與附件檔名
    subject = "(Testing) Script Failed Notice Message"
    body = """There are some failures happening...\nPlease check soon\nDo not reply this letter\nThank you\n\n(Send from python code)"""
    attachments = ['error_code.log']
    

    # 建立訊息物件，利用物件建立基本設定
    em = MIMEMultipart()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.attach(MIMEText(body))    
     
     
    # 加入附件檔內容至信件內容
    for file in attachments:
        with open(file, 'rb') as fp:
            add_file = MIMEBase('application', "octet-stream")
            add_file.set_payload(fp.read())
            
            
        encoders.encode_base64(add_file)
        add_file.add_header('Content-Disposition', 'attachment', filename=file)
        em.attach(add_file)


    # 寄信
    try:
        with smtplib.SMTP('email.siliconmotion.com.tw', timeout = 120) as smtp:     # 設定要連線的Server (公司內網，沒port)
            smtp.starttls()                                                         # 連server
            #smtp.login(email_sender, email_password)                               # 登入帳密 (不需要登入帳密)
            smtp.sendmail(email_sender, email_receiver, em.as_string())             # 寄信
            print("Send successfully!")
            
            
    except Exception as ex:
        print("Send failed......")
        print(ex)
    
    
    
def checkErr_and_sendMail():
    isErr = check_fail_log.get_fail_log()   # 接收回傳的 checkError flag
    print(isErr)
    check_fail_log.store_error_log()
    
    
    # 出錯就寄信通知
    if isErr == True:
        send_mail()
    else:
        print("No error")



if __name__ == '__main__':
    checkErr_and_sendMail()
    