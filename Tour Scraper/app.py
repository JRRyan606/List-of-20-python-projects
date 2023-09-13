import time

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the URL of the band's tour page
band_tour_url = "https://www.bandwebsite.com/tour"

# Define your email configuration
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_password"

# Create a session to persist the connection
session = requests.Session()

# Store the initial page content
initial_page_content = session.get(band_tour_url).content

# Function to check for new tours and send an email notification
def check_and_send_email():
    global initial_page_content

    # Retrieve the current page content
    current_page_content = session.get(band_tour_url).content

    # Parse the HTML content
    initial_soup = BeautifulSoup(initial_page_content, "html.parser")
    current_soup = BeautifulSoup(current_page_content, "html.parser")

    # Extract tour information (modify this based on the band's website structure)
    initial_tour_info = initial_soup.find_all("div", class_="tour-date")
    current_tour_info = current_soup.find_all("div", class_="tour-date")

    # Compare the initial and current tour information
    if initial_tour_info != current_tour_info:
        # There are new tours; send an email notification
        subject = "New Tours Available"
        message = "New tour dates are available on the band's website."

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to your email account
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP server connection
        server.quit()

        # Update the initial page content to the current content
        initial_page_content = current_page_content

# Check for new tours periodically (e.g., every hour)
# You can use a scheduling library like APScheduler for more advanced scheduling
while True:
    check_and_send_email()
    # Adjust the sleep duration as needed (e.g., 3600 seconds for 1 hour)
    time.sleep(3600)
