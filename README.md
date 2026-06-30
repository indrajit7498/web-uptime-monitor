# Automated Web Uptime Monitor

A simple Python tool that automatically checks whether websites are **UP** or **DOWN**, logs the results with timestamps, and sends an **email alert** if a website goes down.

## Why I built this

Websites and APIs can go down unexpectedly, and businesses need to know immediately. This project simulates a basic version of tools like UptimeRobot or Pingdom — checking site availability on a schedule and notifying the owner when something fails.

## Features

- Monitors multiple websites at once (just add URLs to a list)
- Checks status every X seconds (configurable)
- Logs every check (UP/DOWN, status code, timestamp) to `uptime_log.txt`
- Sends an automatic email alert when a site goes down
- Handles errors gracefully (timeouts, connection errors, invalid URLs)

## Tech Stack

- **Python 3**
- `requests` — to make HTTP calls to websites
- `smtplib` — to send email alerts
- `logging` — to record results to a log file
- `time` — to run checks at intervals

## How It Works

1. The script reads a list of website URLs from `config.py`.
2. For each URL, it sends an HTTP GET request using the `requests` library.
3. If the response status code is below 400, the site is marked **UP**. Otherwise, or if the request fails/times out, it's marked **DOWN**.
4. Every result is written to `uptime_log.txt` with a timestamp.
5. If a site is DOWN and email alerts are enabled, an email is sent via Gmail's SMTP server.
6. The script repeats this process every `CHECK_INTERVAL` seconds (default: 60s) until stopped.

## Project Structure

```
web-uptime-monitor/
│
├── monitor.py          # Main script - runs the monitoring loop
├── config.py            # Settings: websites to monitor, interval, email config
├── requirements.txt      # Python dependencies
├── uptime_log.txt        # Auto-generated log file (created when script runs)
└── README.md
```

## Setup & Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/web-uptime-monitor.git
   cd web-uptime-monitor
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Edit `config.py`:
   - Add the websites you want to monitor in `WEBSITES_TO_MONITOR`
   - (Optional) Set `ENABLE_EMAIL_ALERTS = True` and add your Gmail App Password to receive email alerts

4. Run the script:
   ```
   python monitor.py
   ```

5. Watch the terminal output and check `uptime_log.txt` for the full history.

## Sample Output

```
[OK] https://www.google.com is UP (Status: 200)
[OK] https://www.github.com is UP (Status: 200)
[FAIL] https://www.example-broken-site12345.com is DOWN (Reason: ConnectionError)
```

## Future Improvements

- Add a web dashboard (Flask) to visualize uptime history and graphs
- Store results in a database (SQLite) instead of a text file
- Add SMS/Telegram/Slack alerts in addition to email
- Calculate uptime percentage per website over time
- Dockerize the project for easy deployment

## How to Explain This Project in an Interview

**"What does it do?"**
> It's a Python script that pings a list of websites at regular intervals to check if they're online. If a site fails to respond properly, it logs the failure and sends an automated email alert — similar to how real-world monitoring tools like UptimeRobot work, just on a smaller scale.

**"What was the biggest challenge?"**
> Handling network errors gracefully — a website can fail in many ways (timeout, DNS failure, server error, connection refused), so I used `try/except` around the `requests` call to catch all of these and treat them consistently as "DOWN" instead of crashing the script.

**"Why these technologies?"**
> `requests` is the standard, lightweight way to make HTTP calls in Python. `smtplib` is built into Python so no extra setup is needed for email alerts. `logging` gives me timestamped, persistent records of every check, which is important for tracking historical uptime.

**"How would you scale this?"**
> I'd move the checking logic into a background task with something like Celery or APScheduler, store results in a database instead of a flat file, and build a small Flask/React dashboard so users can see uptime percentage and history visually instead of reading raw logs.
