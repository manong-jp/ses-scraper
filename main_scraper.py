# ... 前面代码不变 ...
        if match:
            count = int(match.group(1).replace(',', ''))
            payload = {'key': SECRET_KEY, 'tech': tech, 'count': count}
            
            # 加上这几行监控代码
            print(f"准备发送数据到: {API_RECEIVER}")
            try:
                res = requests.post(API_RECEIVER, data=payload, timeout=10)
                print(f"服务器返回状态码: {res.status_code}")
                print(f"服务器返回内容: {res.text}")
            except Exception as net_err:
                print(f"网络连接失败: {net_err}")
