import  smtplib
import ssl
import pyautogui
rec_name = pyautogui.prompt('Enter the name of the receiver')
def get_mail(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8' ) as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
names, emails = get_mail('contacts.txt')
email = emails[names.index(rec_name.lower())]
msg = pyautogui.prompt('Enter the message you want to enter')
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('voiceassistant2479@gmail.com', 'ajax@2479')
mail.sendmail('voiceassistant2479@gmail.com',email,msg)
mail.close()