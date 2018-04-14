import hashlib

# msg为待加密信息
# MD5为安全散列算法，不可逆，常做报文摘要使用

def md5(msg):
    # 创建md5对象
    m = hashlib.md5()
    try:
        # Tips
        # 此处必须声明encode
        # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
        m.update(msg.encode(encoding="utf-8"))
        print("MD5加密前：{}".format(msg))
        print("MD5加密后：{}".format(m.hexdigest()))
    except Exception as e:
        print("Update error:{}".format(e))

md5("hello world")