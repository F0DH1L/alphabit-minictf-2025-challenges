#usr/bin/env python3 

from Crypto.Util.number import long_to_bytes,bytes_to_long,inverse,getPrime

flag = b'Congratulations! You have solved all the Unpadded RSA challenges,you are now an RSA master. This is you reward : Alphabit{Th0se_chin1s3_p30pl3_ruin3d_4ll_my_plan5}'

m = bytes_to_long(flag)

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3
c = pow(m,e,n)
print(f"{n=}\n{e=}\n{c=}")
x = bytes_to_long(input("Give some text to encrypt : ").encode())
print(pow(x,e,n))