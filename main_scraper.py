import requests
import re

# 配置信息
API_RECEIVER = "https://www.manong.jp/manongA4343Dfed321.php"
SECRET_KEY = "my_secure_secret_key_123"
TECHS = ["Java", "Python", "PHP", "Go"]
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

for tech in TECHS:
    url = f"https://career.levtech.jp/engineer/offer/search/?emp[]=2&keyword={tech}"
    try:
        response = requests.get(url, headers=HEADERS)
        match = re.search(r'p-search-result__count[^>]*>([\d,]+)<', response.text)
        
        if match:
            count_str = match.group(1).replace(',', '')
            count = int(count_str)
            
            # 发送到你的 PHP 接口
            data = {'key': SECRET_KEY, 'tech': tech, 'count': count}
            res = requests.post(API_RECEIVER, data=data)
            print(f"成功: {tech} -> {count}, 服务器响应: {res.text}")
        else:
            print(f"警告: 未找到 {tech} 的匹配数字")
    except Exception as e:
        print(f"出错: {e}")
