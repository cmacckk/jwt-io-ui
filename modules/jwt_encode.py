import jwt

# 自定义加密函数
def encode_jwt(payload, header=None, secret='', algorithm='HS256'):
    """
    生成JWT

    :param payload: JWT载荷,是一个字典
    :param secret: 加密密钥
    :param algorithm: 加密算法
    :return: JWT字符串
    """

    if header is None:
        if secret.strip() == '':
            jwt_token = jwt.encode(payload, key='', algorithm=algorithm)
        else:
            jwt_token = jwt.encode(payload, secret, algorithm=algorithm)
    else:
        jwt_token = jwt.encode(payload, secret, headers=header, algorithm=algorithm)

    return jwt_token


if __name__ == '__main__':
    # 示例JWT载荷，请替换为实际载荷
    payload = {"sub": "1234567890", "name": "John Doe"}

    # 示例加密密钥，请替换为实际密钥
    secret = "cc"

    # 使用HS256算法生成JWT
    jwt_token = encode_jwt(payload, secret='', algorithm='HS256', header={"alg": "none","typ": "JWT"})
    print("JWT with HS256 algorithm:", jwt_token)