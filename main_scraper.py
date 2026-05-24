import requests  # <-- 这一行是必须的！你的错误就是因为没写它
import re

# 配置信息
API_RECEIVER = "https://www.manong.jp/manongA4343Dfed321.php"
SECRET_KEY = "my_secure_secret_key_123" # 确保和你 PHP 里定义的一致
TECHS = ["Java", "Python", "PHP", "Go"]

for tech in TECHS:
    url = f"https://career.levtech.jp/engineer/offer/search/?emp[]=2&keyword={tech}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        match = re.search(r'p-search-result__count[^>]*>([\d,]+)<', response.text)
        if match:
            count = int(match.group(1).replace(',', ''))
            # 这里的参数名必须和 PHP 里的 $_POST['...'] 对应
            data = {'key': SECRET_KEY, 'tech': tech, 'count': count}
            requests.post(API_RECEIVER, data=data)
            print(f"成功发送: {tech} -> {count}")
    except Exception as e:
        print(f"出错: {e}")
