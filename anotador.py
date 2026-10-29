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
        print(f"\U0001F539 arquivo {caminho} não encontrado")    # carrega o arquivo solicitado dentro do diretorio, retorna "arquivo não encontrado" caso não exista/ update: agora a função retorna uma lista vazia, para facilitar testes e possiveis alterações, já que somente um print retora None ao resto do programa.
        return [] 
    return trazer(caminho)

def salvar(caminho, dados):
    caminho = Path(caminho)   # converte os dados para path, se ja forem path continua igual
    caminho.parent.mkdir(parents=True, exist_ok=True)     # cria uma pasta saida se não existir, não faz nada caso exista
    with open(caminho, 'w', encoding='utf-8') as f:
      json.dump(dados, f, ensure_ascii=False, indent=2)

def validar_rotulos(entrada):
    return rotulos.get(entrada.strip().lower())           # checa de o comando corresponde a lista disponivel de rotulos 

def itens_pendentes(texto,anotacoes):
    ids_feitos = {a['id'] for a in anotacoes}               # devolve os textos que não aparecem nas anotações 
    return [t for t in texto if t['id'] not in ids_feitos] 

def anotar(caminho_textos, caminho_saida=saida):
    textos = trazer(caminho_textos)
    anotacoes = trazer_anotacoes(caminho_saida)                                     
    pendentes = itens_pendentes(textos, anotacoes)

    if not pendentes:
        print('Nada a anotar: todos os textos já têm rótulo.')
        return
    print(f'{len(pendentes)} texto(s) pendente(s).')
    print('Atalhos: p = positivo, n = negativo, ne = neutro, s = pular, q = sair')

    try:
        for item in pendentes:
            numero = item['id']
            texto = item['texto']
            print()
            print(f'[{numero}] {texto}')
            while True:
                resposta = input('Rótulo (p/n/ne/s/q): ').strip().lower()
                if resposta == 'q':
                    print('Saindo. Progresso salvo.')
                    return
                if resposta == 's':
                    break
                rotulo = validar_rotulos(resposta)
                if rotulo is not None:
                    anotacoes.append({**item, 'rotulo': rotulo})
                    salvar(caminho_saida, anotacoes)
                    break
                print('Opção inválida. Use p, n, ne, s ou q.')
    except (KeyboardInterrupt, EOFError):
        print()
        print('Interrompido. Progresso salvo.')