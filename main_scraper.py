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
        
        # --- 调试修改部分 ---
        # 打印部分页面内容以便排查
        print(f"[{tech}] 正在分析页面...")
        
        # 尝试匹配数字 (Levtech 页面可能改版了)
        match = re.search(r'p-search-result__count[^>]*>([\d,]+)<', response.text)
        
        if match:
            count = int(match.group(1).replace(',', ''))
            print(f"[{tech}] 成功匹配到数字: {count}")
            
            # 发送给 PHP
            data = {'key': SECRET_KEY, 'tech': tech, 'count': count}
            res = requests.post(API_RECEIVER, data=data, timeout=10)
            print(f"[{tech}] 发送状态: {res.text}")
        else:
            # 如果匹配不到，打印预览，帮我们锁定新位置
            print(f"[{tech}] 错误: 没找到匹配的数字。页面前500字符预览: {response.text[:500]}")
            
    except Exception as e:
        print(f"[{tech}] 异常: {e}")
