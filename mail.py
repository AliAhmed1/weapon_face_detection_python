import yagmail
import getpass
def SendMail():
    try:
        #initializing the server connection
        #pswd = getpass.getpass('Password: ')
        # pswd = 
        # contents = [yagmail.inline("/ali.161.8.jpg")]
        yag = yagmail.SMTP(user='haildottech@gmail.com', password='')
        #sending the email
        yag.send(to='saliahmed11111@gmail.com', subject='Testing Yagmail'
        , 
        contents=[
        "Hello Mike! Here is a picture I took last week:",
        "E:\\weapon-face-mail-system\\4.jpg"
        
        
        ]

        # ,contents= "asjlkdjasklj"

        )
        print("Email sent successfully")
    except:
        print("Error, email was not sent")