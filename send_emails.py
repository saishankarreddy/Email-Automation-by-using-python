import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
import csv
BASE_DIR = r"D:\Desktop\llm-env\Scripts\email_automation"
CSV_FILE = os.path.join(BASE_DIR, "hr_list.csv")
LOG_FILE = os.path.join(BASE_DIR, "logs.txt")



with open(CSV_FILE, encoding="utf-8") as f:
    

    EMAIL = "saishankareddykarri@gmail.com"
    PASSWORD = "rbpj pyfo bhir tmaq"



def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL, PASSWORD)
    log("Login successful")

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            msg = MIMEMultipart()
            msg["From"] = EMAIL
            msg["To"] = row["email"]
            msg["Subject"] = "Application for Python / DevOps Fresher Role"

            body = f"""
Hi {row['name']},

I am currently seeking opportunities in early career roles and wanted to check if there are any relevant openings at {row['company']}.

I would really appreciate any guidance or help you could share.I am sharing my resume for your reference.
Please let me know if there are any suitable positions.

Thank you for your time. 
Sai Shankar


Here is my Resume: https://docs.google.com/document/d/1TDl4IalgdBfpEpxlb6GEJ2dtMa6NLoHU/edit#heading=h.pfe8l9j2izra


"""
            msg.attach(MIMEText(body, "plain"))

            server.send_message(msg)
            log(f"Email sent to {row['email']}")
            time.sleep(25cx)  # VERY IMPORTANT (anti-spam)

    server.quit()
    log("All emails sent successfully")

except Exception as e:
    log(f"Error: {e}")
