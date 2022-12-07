# finalized xor cipher
def modifiedXOR(pt, key):
    # xor the plaintext with the key and store the result in ciphertext
    # pt is the plaintext
    # key is the key
    # ct is the ciphertext
    ct = ""
    for i in range(len(pt)):
        temp = ord(pt[i]) ^ ord(key[i % len(key)])
        temp %= 94 #ensures we stay in the printable ascii range
        temp += 33 #shifts the ascii range to the printable range and avoids the space character
        ct += chr(temp)
    return ct


#testing grounds
# def main():
#     pt = "password1"
#     key = "hds"
#     ct = modifiedXOR(pt, key)
#     print(ct)


# main()
