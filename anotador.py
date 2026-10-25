import json
from pathlib import Path

rotulos = {'p': 'positivo', 'n': 'negativo', 'ne': 'neutro' }
saida = Path('saida/anotacoes.json')

def trazer(caminho):
    with open (caminho, encoding='utf-8') as f:    # carrega o arquivo solicitado dentro do diretorio
        return json.load(f)

def trazer_anotacoes(caminho):
    caminho = Path(caminho)
    if not caminho.exists():
        return print(f"\U0001F539 arquivo {caminho} não encontrado")    # carrega o arquivo solicitado dentro do diretorio, retorna "arquivo não encontrado" caso não exista
    return trazer(caminho)

def salvar(caminho, dados):
    caminho = Path(caminho)   # converte os dados para path, se ja forem path continua igual
    caminho.parent.mkdir(parents=True, exist_ok=True)     # cria uma pasta saida se não existir, não faz nada caso exista 
    with open(caminho, 'w', encoding='utf-8') as f:
      json.dump(dados, f, ensure_ascii=False, indent=2)


