"""
Automated Web Uptime Monitor
-----------------------------
Checks if websites are UP or DOWN at regular intervals,
logs the results, and sends an email alert if a site goes down.

Author: Indrajit Dudhane
"""

import requests
import time
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import config


# ---------- Setup Logging ----------
logging.basicConfig(
    filename="uptime_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_website(url):
    """
    Sends a GET request to the given URL and returns its status.
    Returns True if site is UP (status code 200-399), False if DOWN.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code < 400:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.RequestException as e:
        return False, str(e)


def send_email_alert(url, status):
    """
    Sends an email notification when a website is detected as DOWN.
    Uses Gmail SMTP (App Password required, not your normal password).
    """
    if not config.ENABLE_EMAIL_ALERTS:
        return

    subject = f"ALERT: {url} is DOWN!"
    body = f"The website {url} appears to be DOWN.\nStatus/Error: {status}\nTime: {datetime.now()}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config.SENDER_EMAIL
    msg["To"] = config.RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(config.SENDER_EMAIL, config.SENDER_PASSWORD)
            server.sendmail(config.SENDER_EMAIL, config.RECEIVER_EMAIL, msg.as_string())
        logging.info(f"Email alert sent for {url}")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")


def monitor_websites():
    """
    Continuously monitors all websites listed in config.py
    at the interval defined by CHECK_INTERVAL (in seconds).
    """
    print("Starting Automated Web Uptime Monitor... (Press CTRL+C to stop)")
    while True:
        for url in config.WEBSITES_TO_MONITOR:
            is_up, status = check_website(url)

            if is_up:
                message = f"{url} is UP (Status: {status})"
                print(f"[OK] {message}")
                logging.info(message)
            else:
                message = f"{url} is DOWN (Reason: {status})"
                print(f"[FAIL] {message}")
                logging.warning(message)
                send_email_alert(url, status)

        time.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    monitor_websites()
