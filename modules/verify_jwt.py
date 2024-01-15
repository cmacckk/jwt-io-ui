import jwt

# 自定义签名验证函数
def verify_signature(token, secret, algorithm='HS256'):
    """
    验证JWT签名

    :param token: JWT字符串
    :param secret: 加密密钥
    :param algorithm: 加密算法
    :return: True/False
    """
    try:
        # 解码JWT，并验证签名
        jwt.decode(token, secret, algorithms=[algorithm])
        return True
    except jwt.InvalidSignatureError:
        # 签名无效
        return False
    except jwt.ExpiredSignatureError:
        # JWT已过期
        return False
    except jwt.InvalidTokenError:
        # JWT无效
        return False


if __name__ == '__main__':
    jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXBvIjoiaHR0cHM6Ly9naXRodWIuY29tL2NtYWNja2svand0LWlvLXVpIn0.Io97SU9pDHBH1UCCAEfWYuItlbocmhcYEifqVLqhVN4'

    secret = "123456"

    # 使用HS256算法验证签名
    is_valid = verify_signature(jwt_token, secret)
    print("Signature valid (HS256):", is_valid)