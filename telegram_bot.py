# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:12:11 2026

@author: Administrator
"""

import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)