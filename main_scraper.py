import requests
import re
import time

API_RECEIVER = "https://www.manong.jp/manongA4343Dfed321.php"
SECRET_KEY = "my_secure_secret_key_123"
TECHS = ["Java", "Python", "PHP", "Go"]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://career.levtech.jp/',
    'Connection': 'keep-alive'
}

for tech in TECHS:
    # 确保这行代码在同一行内
    url = f"https://career.levtech.jp/engineer/offer/search/?emp[]=2&keyword={tech}"
    try:
        time.sleep(2)
        response = requests.get(url, headers=HEADERS, timeout=15)
        
        if response.status_code == 200:
            match = re.search(r'p-search-result__count[^>]*>([\d,]+)<', response.text)
            if match:
                count = int(match.group(1).replace(',', ''))
                print(f"[{tech}] 成功: {count}")
                res = requests.post(API_RECEIVER, data={'key': SECRET_KEY, 'tech': tech, 'count': count}, timeout=10)
            else:
                print(f"[{tech}] 错误: 没找到数据")
        else:
            print(f"[{tech}] 403错误: 被网站拦截")
    except Exception as e:
        print(f"[{tech}] 异常: {e}")
