import hashlib

def sha512(message):
    hash_object=hashlib.sha512(message.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

if __name__ == "__main__":
    s = "GeeksForGeeks"

    print( s + " : " + sha512(s))
