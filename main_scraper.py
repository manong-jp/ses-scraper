import requests
import re
import time

# 配置信息
API_RECEIVER = "https://www.manong.jp/manongA4343Dfed321.php"
SECRET_KEY = "my_secure_secret_key_123"
TECHS = ["Java", "Python", "PHP", "Go"]

# 强化版 HEADERS，用于绕过反爬检查
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://career.levtech.jp/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin'
}

for tech in TECHS:
    url = f"
