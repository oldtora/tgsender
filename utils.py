import os

def load_accounts(file_path):
    accounts = []
    with open(file_path, 'r') as f:
        for line in f:
            api_id, api_hash, session = line.strip().split(':')
            accounts.append({'api_id': api_id, 'api_hash': api_hash, 'session': session})
    return accounts

def load_groups(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def load_phrases(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def send_alert(message):
    print(f"[ALERT] {message}")
