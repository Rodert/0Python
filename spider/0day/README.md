request



### 安装request

```bash
pip install requests

```

### 导包

```Python
# Python
import requests
```



### 爬取开始


```Python
import requests

res = requests.get("https://www.baidu.com")

print(res.text)
```

### 设置请求头

```Python

import requests

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

res = requests.get("https://www.baidu.com", headers=head)

print(res.text)

print(res.status_code)
```

![image](https://tvax4.sinaimg.cn/large/007F3CC8ly1h3h5lc10rqj313v0r6tkz.jpg)


[GitHub](https://github.com/Rodert/0Python) | [Gitee](https://gitee.com/rodert/Python)

