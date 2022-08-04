from email.message import EmailMessage
import smtplib


def send_mail():
    # 資料設定
    email_sender = "tinghao.chen@siliconmotion.com"
    #email_receiver = "jerry.ku@siliconmotion.com"
    email_receiver = "tinghao.chen@siliconmotion.com"



    # 標題與內文
    subject = "Hello, This is corporate email testing"
    body = """I've just sent you an email message for testing!\n測試用! 請勿回覆此信件~~~\n我把SMTP連的server改成公司的然後把port拿掉就能寄信了\n耶耶"""
    # body2 = []

    # with open('error_code.log' , 'r') as ermsg:
    #     body2.append(ermsg.readlines())     # 一行一行讀進來 list 裡面
    # print(body2)

    # 建立訊息物件，利用物件建立基本設定
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)



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
    
    
    
    
def error_save():
    body2 = []
    global body3
    with open('error_code.log' , 'r') as ermsg:
        for i in ermsg:
            print(i)
        




if __name__ == '__main__':
    #send_mail()
    error_save()