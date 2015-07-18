
from Crypto.Cipher import AES

BS = 32		# AES-256
# unpad = lambda s: s[0:-ord(s[-1])]
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[0:-ord(s[-1])]


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def encryptAES(message, aesKey):
    message = pad(message)
    aes = AES.new(aesKey, AES.MODE_ECB)
    return aes.encrypt(message)


def decryptAES(message, aesKey):
    aes = AES.new(aesKey, AES.MODE_ECB)
    return unpad(aes.decrypt(message))
