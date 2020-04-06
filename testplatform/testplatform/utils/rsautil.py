import rsa as rsa


def encrypt():  # 用公钥加密
    with open('public.pem', 'rb') as publickfile:
        p = publickfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(p)
    original_text = 'have a good time'.encode('utf8')
    crypt_text = rsa.encrypt(original_text, pubkey)
    print(crypt_text)
    return crypt_text  # 加密后的密文


def decrypt(crypt_text):  # 用私钥解密
    with open('private.pem', 'rb') as privatefile:
        p = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)
    lase_text = rsa.decrypt(crypt_text, privkey).decode()  # 注意，这里如果结果是bytes类型，就需要进行decode()转化为str

    print(lase_text)


if __name__ == '__main__':
    crypt_text = encrypt()
    lase_text =  decrypt(crypt_text)