ct = "b0ae02d4abe5658051536adbb4372f2031a20681b0581f87cf51f073022d9d23c0041b53b023dcae6a3a71d49e9f8195"
iv = "e5faa2b251e28cf2b9a9eb6c146f22f9"
block_size = 16


from Crypto.Cipher import AES

ct = bytes.fromhex(ct)
iv = bytes.fromhex(iv)



for block in range(0, len(ct), block_size):
    print(ct[block:block+block_size])


    
# decrypt = AES.new(iv, AES.MODE_CBC, iv)

# decrypted = decrypt.decrypt(ct)
# print(decrypted)