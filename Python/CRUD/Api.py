import requests

def consultar_tempo(cidade, api_key):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
    
    try:
        
        resposta = requests.get(url)
        
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            
            temperatura = dados['main']['temp']
            sensacao = dados['main']['feels_like']
            descricao = dados['weather'][0]['description']
            umidade = dados['main']['humidity']
            
        
            print(f"Temperatura em {cidade}: {temperatura}°C")
            print(f"Sensação térmica: {sensacao}°C")
            print(f"Descrição: {descricao}")
            print(f"Umidade: {umidade}%")
        
        else:
            print("Erro ao consultar a API. Verifique a cidade ou sua chave de API.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na conexão: {e}")


SUA_CHAVE_API = "7b4219dbdac9f642a977430fa31f750e"
consultar_tempo(input("Digite a cidade: "), SUA_CHAVE_API)