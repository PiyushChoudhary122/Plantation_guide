import smtplib
import tkinter.ttk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *


def emailwin():
    global emailwinmain

    def emailwinmain():
        store = 'emailchk.temp'
        with open(store, 'w') as f:
            f.write(emailentry.get())
            f.close()

        with open(store) as f:
            data = f.readlines()
            # a = data[0].rstrip()
            a = "1000014540@dit.edu.in"
        mail_content = '''
                               Thank you for using this program .
                               The programmer hopes that you will plant more trees using this program and take care of them and help Earth to become pollution free.

                               Thank You
                               yours sincerely,
                               PIYUSH CHOUDHARY
                               programmer
                               '''

        # The mail addresses and password
        sender_address = "projectplant5537@gmail.com"
        sender_pass = 'projecttree'
        receiver_address = a
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Mail from PROGRAMMER :PROJECT TREE'  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

    # the last window starts from here
    thank = Tk()
    thank.title('THANKYOU')
    thank.config(bg='black')
    thank.geometry('1300x656')
    style = tkinter.ttk.Style()
    style.configure("W.TButton", font=('calibri', 16), relief='grooved', foreground='orange', background='black')

    hedding_label = Label(thank, text="Thank you for Using this Programme", font='Heveletica 26', fg='orange',
                          bg='black')
    hedding_label.pack()

    receiversadd = Label(thank, text='Enter your Email address ', font='Heveletica 18', fg='OliveDrab1', bg='black')
    receiversadd.place(x=100, y=125)

    emailentry = Entry(thank, fg='orange', bg='black')
    emailentry.place(x=390, y=132)

    email_label = Label(thank, text="Email:-projecttree@gmail.com", font='Heveletica 20', fg='orange', bg='black')
    email_label.place(x=900, y=550)

    chk = tkinter.ttk.Button(thank, text='send', style="W.TButton", command=emailwinmain)
    chk.pack()
    thank.mainloop()

emailwin()