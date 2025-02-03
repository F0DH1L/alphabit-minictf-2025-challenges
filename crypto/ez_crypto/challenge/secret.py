FLAG="Alphabit{D0_p30pl3_st1ll_us3_th1s_k1nd_0f_3ncrypt10ns?}"
def encrypt(pt):
    ct = ''
    for i in range(len(pt)-1):
        ct+=chr(ord(pt[i])^ord(pt[i+1])+5)
    return ct.encode().hex()

