# coding=utf-8

import codecs
import binascii

# 一个二进制数 = 1 bit    0
# 一个八进制数 = 3 bit    000
# 一个十六进制数 = 4 bit  0000
# 一个字节 = 8 bit       00000000
# 一个中文 = 24 bit = 三个字节


# --------------------------------------------------------------
# 数字转换，主要利用bin oct int hex 等内置方法
# 十进制转换成其他进制
def inttoO(number):
    number_10 = int(number)
    number_2 = bin(number_10)
    number_8 = oct(number_10)
    number_16 = hex(number_10)
    print("| 二进制：{} | 八进制：{} | 十进制数：{} | 十六进制：{} |".format(number_2,number_8,number_10,number_16))
# --------------------------------------------------------------
# 二进制换成其他进制
def bintoO(number):
    number_2 = '0b' + number
    number_10 = int(number_2,2)
    number_8 = oct(int(number_2,2))
    number_16 = hex(int(number_2,2))
    print("| 二进制：{} | 八进制：{} | 十进制数：{} | 十六进制：{} |".format(number_2, number_8, number_10, number_16))
# --------------------------------------------------------------
# 十六进制换成其他进制
def hextoO(number):
    number_16 = '0x'+number
    number_10 = int(number_16,16)
    number_2 = bin(int(number_16,16))
    number_8 = oct(int(number_16,16))
    print("| 二进制：{} | 八进制：{} | 十进制数：{} | 十六进制：{} |".format(number_2,number_8,number_10,number_16))
# --------------------------------------------------------------
# 八进制换成其他进制
def octtoO(number):
    number_8 = '0o'+number
    number_10 = int(number_8,8)
    number_2 = bin(int(number_8,8))
    number_16 = hex(int(number_8,8))
    print("| 二进制：{} | 八进制：{} | 十进制数：{} | 十六进制：{} |".format(number_2, number_8, number_10, number_16))
# --------------------------------------------------------------
# 进制转换入口
def Conver():
    number = int(input("请选择需要转换的进制类型（1.bin|2.oct|3.int|4.hex）："))
    content = input("请输入内容：")
    if number == 1:
        inttoO(content)
    elif number == 2:
        octtoO(content)
    elif number == 3:
        inttoO(content)
    elif number == 4:
        hextoO(content)
# --------------------------------------------------------------
# 字符串转化为十六进制
def strtoH(content):
    print(binascii.b2a_hex(content.encode('utf-8')))                                        # 将字符串类型转换成字节型十六进制
    print(binascii.a2b_hex(binascii.b2a_hex(content.encode('utf-8'))).decode('utf-8'))      # 将字节型十六进制转换成字符串
    print(binascii.hexlify(content.encode('utf-8')))                                        # 将字符串类型转换成字节型十六进制
    print(bytes(content,'utf-8'))                                                           # 将字符串的unicode编码转换成utf-8编码
    print(codecs.encode(bytes(content,'utf-8'),'hex_codec'))                                # 将字符串类型转换成字节型十六进制

# --------------------------------------------------------------
if __name__ == "__main__":
    # Conver()
    # strtoH('hello world,你好世界！')