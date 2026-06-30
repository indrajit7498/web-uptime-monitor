# ============================================
# Configuration File for Web Uptime Monitor
# ============================================

# List of websites you want to monitor
WEBSITES_TO_MONITOR = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.example-broken-site12345.com"  # example of a site that will fail
]

# How often to check the websites (in seconds)
CHECK_INTERVAL = 60  # checks every 60 seconds

# ---------- Email Alert Settings ----------
# Set to True if you want email alerts when a site goes down
ENABLE_EMAIL_ALERTS = False

# Use a Gmail "App Password", NOT your real Gmail password.
# Generate one here: https://myaccount.google.com/apppasswords
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"
