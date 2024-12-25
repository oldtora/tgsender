# Telegram Sender Bot

This is a Python-based Telegram automation bot built using Telethon. The bot monitors specific Telegram groups/channels for new posts and automatically comments with random phrases using different accounts.

## Features
- Monitors specified Telegram channels/groups for new posts.
- Automatically sends random comments under new posts.
- Supports multiple Telegram accounts.
- Ensures accounts are subscribed to channels before commenting.
- Switches accounts if one is banned from a channel.

## Installation Guide

```bash
# 1. Clone the Repository
# First, clone the repository from GitHub onto your server:
git clone https://github.com/oldtora/tgsender.git
cd tgsender

# 2. Install Python and Dependencies
# Ensure you have Python 3.8 or higher installed. Update your system and install Python:
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y

# Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate

# Install required Python packages:
pip install -r requirements.txt

# 3. Configure the Bot
# Add Telegram accounts to the `accounts.txt` file in the following format:
# API_ID:API_HASH:SESSION_NAME
# Example:
123456:abcdef1234567890abcdef1234567890:account1
789012:ghijkl78901234567890ghijkl789012:account2

# Specify monitored channels/groups in the `groups.txt` file:
example_channel1
example_channel2

# Define random comments in the `phrases.txt` file:
Thank you for the information! 🚀
Great post! 🔥
Looking forward to more updates! 📢

# 4. Run the Bot
# Run the bot manually to ensure it works as expected:
python3 main.py

# 5. Run as a Background Service
# To keep the bot running 24/7, set it up as a systemd service. Create a systemd service file:
sudo nano /etc/systemd/system/tgsender.service

# Add the following content:
[Unit]
Description=Telegram Sender Bot
After=network.target

[Service]
User=your_username
WorkingDirectory=/path/to/tgsender
ExecStart=/usr/bin/python3 /path/to/tgsender/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

# Replace `/path/to/tgsender` with the full path to your project directory. Reload systemd and start the service:
sudo systemctl daemon-reload
sudo systemctl start tgsender.service
sudo systemctl enable tgsender.service

# Check the service status:
sudo systemctl status tgsender.service

# 6. Log Monitoring
# To check the bot's activity logs:
journalctl -u tgsender.service -f

# 7. Troubleshooting
# Ensure all dependencies are installed properly. Check the `accounts.txt`, `groups.txt`, and `phrases.txt` files for correct formatting. If you face issues with banned accounts or API limits, consider using more Telegram accounts.
