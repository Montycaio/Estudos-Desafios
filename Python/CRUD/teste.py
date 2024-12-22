import requests

try:
    req = requests.get('https://solyd.com.br/')
except:
    print("Erro na conexao.")

print(req)