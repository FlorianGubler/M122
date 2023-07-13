#!/bin/bash

# SMTP Configuration

smtp_host="smtp.gmail.com"

smtp_port=465

smtp_username="m122.testmail@gmail.com"

smtp_password="123"


# Email Details

email_from="m122.testmail@gmail.com"

email_to="gubler.florian@gmx.net"

email_subject="Basketball Report"

email_body="This is the body of the email."


# Construct the email headers and body

email_headers="From: $email_from\r\n"

email_headers+="To: $email_to\r\n"

email_headers+="Subject: $email_subject\r\n"

email_headers+="Content-Type: text/plain; charset=UTF-8\r\n"

email_headers+="Content-Transfer-Encoding: 8bit\r\n\r\n"

email_message="$email_headers$email_body"


# Send the email

echo -e "$email_message" | openssl s_client -quiet -connect "$smtp_host:$smtp_port" -tls1 -starttls smtp -crlf -ign_eof \

    -CApath /etc/ssl/certs/ -crl_check -verify_hostname "$smtp_host" \

    -key <(echo -e "EHLO host.example.com\r\nAUTH LOGIN\r\n$smtp_username\r\n$smtp_password\r\nMAIL FROM: <$email_from>\r\nRCPT TO: <$email_to>\r\nDATA\r\n") \

    > /dev/null 2>&1


# Check the exit code

if [[ $? -eq 0 ]]; then

    echo "Email sent successfully."

else

    echo "Failed to send email."

fi
