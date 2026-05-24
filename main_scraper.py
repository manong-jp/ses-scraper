# 确保 key 的值完全一样
requests.post(API_RECEIVER, data={
    'tech': tech, 
    'count': count, 
    'key': 'my_secure_secret_key_123'  # 这里必须和 PHP 里的 $secret_key 一模一样
})
