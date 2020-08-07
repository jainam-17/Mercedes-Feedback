import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '19f52f0ac57b79'
    password = '4b6cfdce547989'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'jainampatel93@gmail.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Mercedes Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #send email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
