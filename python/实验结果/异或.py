# 加密解密
def xor_encrypt_decrypt(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

message = "hello"
key = 7
cipher = xor_encrypt_decrypt(message, key)
print("加密后：", cipher)

original = xor_encrypt_decrypt(cipher, key)
print("解密后：", original)

# 找唯一数
def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4, 1, 2, 1, 2]
print("唯一数：", find_single_number(nums))

# 交换两数
a, b = 5, 3
a = a ^ b
b = a ^ b
a = a ^ b
print("交换后：a =", a, ", b =", b)
