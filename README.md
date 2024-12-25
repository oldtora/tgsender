# Telegram Sender Bot

This is a Python-based Telegram automation bot built using Telethon. The bot monitors specific Telegram groups/channels for new posts and automatically comments with random phrases using different accounts.

---

## Features
- Monitors specified Telegram channels/groups for new posts.
- Automatically sends random comments under new posts.
- Supports multiple Telegram accounts.
- Ensures accounts are subscribed to channels before commenting.
- Switches accounts if one is banned from a channel.

---

## Installation Guide

### **1. Clone the Repository**
First, clone the repository from GitHub onto your server:
```bash
git clone https://github.com/oldtora/tgsender.git
cd tgsender


2. Install Python and Dependencies
Ensure you have Python 3.8 or higher installed.

a) Update your system and install Python:
bash
Copy code
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
b) Create a virtual environment (optional but recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate
c) Install required Python packages:
bash
Copy code
pip install -r requirements.txt
3. Configure the Bot
a) Add Telegram accounts
In the accounts.txt file, add your Telegram account credentials in the following format:

ruby
Copy code
API_ID:API_HASH:SESSION_NAME
Example:

ruby
Copy code
123456:abcdef1234567890abcdef1234567890:account1
789012:ghijkl78901234567890ghijkl789012:account2
b) Specify monitored channels/groups
In the groups.txt file, add the usernames (or IDs) of the Telegram channels/groups you want to monitor, one per line:

Copy code
example_channel1
example_channel2
c) Define random comments
In the phrases.txt file, add the comments the bot will randomly choose from, one per line:

css
Copy code
Thank you for the information! 🚀
Great post! 🔥
Looking forward to more updates! 📢
4. Run the Bot
You can run the bot manually to ensure it works as expected:

bash
Copy code
python3 main.py
5. Run as a Background Service
To keep the bot running 24/7, set it up as a systemd service.

a) Create the systemd service file:
bash
Copy code
sudo nano /etc/systemd/system/tgsender.service
b) Add the following content to the file:
plaintext
Copy code
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
Replace /path/to/tgsender with the full path to the project directory.

c) Reload systemd and start the service:
bash
Copy code
sudo systemctl daemon-reload
sudo systemctl start tgsender.service
sudo systemctl enable tgsender.service
d) Check the service status:
bash
Copy code
sudo systemctl status tgsender.service
6. Log Monitoring
To check the bot's activity logs:

bash
Copy code
journalctl -u tgsender.service -f
7. Troubleshooting
Ensure all dependencies are installed properly.
Check the accounts.txt, groups.txt, and phrases.txt files for correct formatting.
If you face issues with banned accounts or API limits, consider using more Telegram accounts.
Requirements
Python 3.8 or higher
Telethon library (specified in requirements.txt)
Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

License
This project is licensed under the MIT License.

yaml
Copy code

---

### **How to Use This**
- Save this guide as `README.md` in the root of your GitHub repository.
- It provides a step-by-step guide for users to clone, configure, and deploy your bot.

Let me know if you need any changes or additions! 🚀
