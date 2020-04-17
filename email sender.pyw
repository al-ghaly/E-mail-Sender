import smtplib
import tkinter as tk
from tkinter import ttk, messagebox


def send_gmail(frm, password, to, subject, body):
    try:
        message = 'Subject: %s\nDear Friend\n\n%s\n\n\n' % (subject, body)
        # the standard format for the sent message
        connection = smtplib.SMTP('smtp.gmail.com', 587)   # make a connection object
        connection.ehlo()   # send request to the host server
        connection.starttls()  # encrypting the data sent
        connection.login(frm, password)   # log in to mail
        failed = connection.sendmail(frm, to, message)  # send email and return dictionary of failed mail
        connection.quit()  # end the connection
        if len(failed) > 0:
            raise Exception
        messagebox.showinfo('Done', 'E-mail sent')
    except:
        messagebox.showerror('Error', 'Invalid Input')


app = tk.Tk()
app.geometry('550x600')
app.title('E-mail Sender')
ttk.Label(app, text='E-mail', font=('Arial', 10, 'bold')).grid(row=0, column=0,padx=30, pady=10)
ttk.Label(app, text='Password', font=('Arial', 10, 'bold')).grid(row=1, column=0, pady=10)
ttk.Label(app, text='To', font=('Arial', 10, 'bold')).grid(row=2, column=0, pady=10)
ttk.Label(app, text='Subject', font=('Arial', 10, 'bold')).grid(row=3, column=0, pady=10)
email = ttk.Entry(app, width=50)
email.grid(row=0, column=1, padx=100)
password = ttk.Entry(app, width=50, show='*')
password.grid(row=1, column=1)
to = ttk.Entry(app, width=50)
to.grid(row=2, column=1)
subject = ttk.Entry(app, width=50)
subject.grid(row=3, column=1)
ttk.Label(app, text='Message', font=('Arial', 10, 'bold')).grid(row=4, column=0, padx=30, pady=30, sticky=tk.N)
text = tk.StringVar()
message = tk.Text(app, width=38, height=12)
message.grid(row=4, column=1, pady=40)


def send():
    mail = email.get()
    pas = password.get()
    receiver = to.get()
    sub = subject.get()
    body = message.get('1.0', 'end')
    send_gmail(mail, pas, receiver, sub, body)


ttk.Button(app, text='Send', width=50, command=send).grid(row=5, column=1, pady=50, ipady=10)
app.mainloop()
