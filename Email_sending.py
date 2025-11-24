import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password):
    # Create the email headers and body
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        # Log in to the server
        server.login(login, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        # Terminate the SMTP session
        server.quit()

# Example usage
sender = "sjeoor@outlook.com"
receiver = "sjeoor@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."
smtp_server = "smtp.office365.com"
smtp_port = 587
login = "sjeoor@outlook.com"
password = "your_password_here"  # Replace with your actual password
send_email(sender, receiver, subject, body, smtp_server, smtp_port, login, password)