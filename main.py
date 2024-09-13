import pdfkit
import email

# Read the .eml file
with open('出票成功确认.eml', 'r') as file:
    msg = email.message_from_file(file)

# Get the email body
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            body = part.get_payload(decode=True).decode()
            break
else:
    body = msg.get_payload(decode=True).decode()

# Convert the email body to PDF
pdfkit.from_string(body, 'output.pdf')
