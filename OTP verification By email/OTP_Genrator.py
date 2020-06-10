from random import randint, choice
import smtplib
import credentials

otp = randint(0000, 9999)

lst = [[randint(0, 9)], [chr(randint(65, 90))], [
    chr(randint(97, 122))], [choice(['@', '#', '$', '&'])]]
psw = list()
for x in range(8):
    psw.append(choice(lst)[0])
fnl_psw = ''.join(map(str, psw))


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(credentials.EMAIL, credentials.PASSWORD)
    subject = 'OTP for verification....'
    body = f'Your otp is {otp} and password is {fnl_psw}'
    msg = f'Subject : {subject} \n\n {body}'
    smtp.sendmail(credentials.EMAIL, 'harshidkoladara.hk3624@gmail.com', msg)

print(f'OTP : {otp} \nPASSWORD : {fnl_psw}')