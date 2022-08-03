import win32com.client as win32
import os


olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

def send_mail():
    # construct email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Hello, this is email Testing'
    mailItem.BodyFormat = 1
    mailItem.Body = 'Hello, I just want to send you an email~'
    mailItem.To = 'tinghao.chen@siliconmotion.com'
    # mailItem.To = 'terry9026955@gmail.com'
    mailItem.Sensitivity  = 2
    
    # optional (account you want to use to send the email)
    # mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('terry9026955@gmail.com'))) 
    
    mailItem.Display()
    mailItem.Save()
    mailItem.Send()


def send_attachment():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Error message Email'
    mailItem.BodyFormat = 1
    mailItem.Body = "The Script Failed"
    # mailItem.To = 'tinghao.chen@siliconmotion.com' 
    mailItem.To = 'terry9026955@gmail.com'

    mailItem.Attachments.Add(os.path.join(os.getcwd(), 'error_code.log'))
    #mailItem.Attachments.Add(os.path.join(os.getcwd(), 'csv file.png'))

    mailItem.Display()
    mailItem.Save()
    mailItem.Send()

if __name__ == "__main__":
    # send_mail()
    send_attachment()
    #print(os.path.join(os.getcwd(), 'error_coce.log'))