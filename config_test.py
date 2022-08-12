import configparser


config = configparser.ConfigParser()
config.read('email.ini')


from_who = config['EMAIL_SENDER']['email_sender']
to_who = config['EMAIL_RECEIVER']['email_receiver']
#to_who = config['EMAIL_RECEIVER']
print(to_who)