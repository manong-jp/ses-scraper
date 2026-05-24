import requests
import re

API_RECEIVER = "https://www.manong.jp/manongA4343Dfed321.php"
SECRET_KEY = "my_secure_secret_key_123"
TECHS = ["Java", "Python", "PHP", "Go"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

for tech in TECHS:
    url = f"https://career.levtech.jp/engineer/offer/search/?emp[]=2&keyword={tech}"
    try:
        response = requests.get(url, headers=headers)
        # 寻找 Levtech 搜索结果页中的数字
        match = re.search(r'p-search-result__count[^>]*>([\d,]+)<', response.text)
        
        if match:
            count = int(match.group(1).replace(',', ''))
            # 发送到服务器
            payload = {'key': SECRET_KEY, 'tech': tech, 'count': count}
            res = requests.post(API_RECEIVER, data=payload)
            print(f"[{tech}] 发送数据 {count}: {res.text}")
        else:
            print(f"[{tech}] 错误: 没找到匹配的数字，网页可能已改版。")
            
    except Exception as e:
        print(f"[{tech}] 异常: {e}")
