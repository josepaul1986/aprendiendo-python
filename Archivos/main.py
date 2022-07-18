import re,os

#print(os.listdir())
os.chdir("Archivos")

file = open(file="sample.txt",mode="rt",encoding="utf-8")

info = file.read()

file.close()

# print(info)
print(re.match(r"RegExr",info)) # busca al inicio de la cadena.
print(re.search(r"includes",info)) # busca en toda la cadena.

matches = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",info)
for match in matches:
    print(match)