import base64

# 自定义解密函数
def decode_jwt(token):
    # 将JWT拆分为头部，载荷和签名
    parts = token.split('.')
    if len(parts) < 2:
        raise ValueError('Incorrect JWT format')
    elif len(parts) <= 3:
        header = parts[0]
        payload = parts[1]
        # 解码头部和载荷
        header_decoded = base64.b64decode(header + '=' * (-len(header) % 4)).decode('utf-8')
        payload_decoded = base64.b64decode(payload + '=' * (-len(payload) % 4)).decode('utf-8')

        # 返回头部和载荷
        return header_decoded, payload_decoded
    else:
        raise ValueError('Incorrect JWT format')
    

if __name__ == '__main__':
    # 示例JWT，请替换为实际JWT
    jwt_token = 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.O-Y6rMecB_F3U0KMXPHhnTqz5tUbKN11265GMzKDosRebf5U4888JW8p3k1B0L2B'

    # 调用自定义解密函数
    header, payload = decode_jwt(jwt_token)

    # 打印头部和载荷
    print("Header:", header)
    print("Payload:", payload)
