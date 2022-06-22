
import requests

# 请求头
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

res = requests.get("https://www.baidu.com", headers=head)

print(res.text)

# 状态码
print(res.status_code)