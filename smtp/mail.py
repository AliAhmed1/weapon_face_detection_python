import yagmail
import getpass
def SendMail():
    try:
        #initializing the server connection
        pswd = getpass.getpass('Password: ')

        # contents = [yagmail.inline("/ali.161.8.jpg")]
        yag = yagmail.SMTP(user='saliahmed11111@gmail.com', password=pswd)
        #sending the email
        yag.send(to='saliahmed11111@gmail.com', subject='Testing Yagmail'
        , 
        contents=[
        "Hello Mike! Here is a picture I took last week:",
        "E:\\Attendance_management_system\\smtp\\img.jpg"
        
        
        ]

        # ,contents= "asjlkdjasklj"

        )
        print("Email sent successfully")
    except:
        print("Error, email was not sent")