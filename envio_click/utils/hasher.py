import hashlib as hasher


def sha1_encrypt(plain_text):
    res = hasher.sha1()
    res.update(plain_text.encode("utf-8"))
    return res.hexdigest()


def sha1_compare(plain_text, sha1_text):
    pt_sha1 = sha1_encrypt(plain_text)
    return pt_sha1 == sha1_text
