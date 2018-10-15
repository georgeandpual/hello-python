import hashlib



def make_md5(passworwd):
    md5=hashlib.md5
    md5.update(passworwd.encode('utf-8'))

    return md5.hexdigest()

make_md5(123456)
