import configparser

ini = configparser.ConfigParser()
ini.read('email.ini')
receiver = ini['EMAIL_RECEIVER']['email_receiver']
receiver = receiver.split(',')
print(receiver)

