import json
import requests

# Lendo arquivo json
with open('path/to/json/file.json', 'r') as file:
    data = json.load(file)

# Validando
if 'firstName' not in data or 'lastName' not in data or 'CPF' not in data:
    print('Erro: Arquivo JSON esta sem um dos campos')
elif len(data['firstName']) < 2 or len(data['lastName']) < 2:
    print('Erro: Um dos nomes apresenta menos que 2 caracteres')
elif len(data['CPF']) != 11:
    print('Erro: CPF não contém 11 digitos')
else:
    # Criando o campo fullName
    data['fullName'] = data['firstName'] + ' ' + data['lastName']
    # Removendo o firstName e LastName
    del data['firstName']
    del data['lastName']
    # Tirando pontos e traço do CPF
    data['CPF'] = data['CPF'].replace('.', '').replace('-', '')

    # Enviar payload
    url = "http://localhost:8080"
    r = requests.post(url, data=json.dumps(data))