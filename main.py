from pathlib import Path

from anotador import anotar, saida


def main():
    while True:
        try:
            caminho_textos = input('Informe o caminho do arquivo de textos: ').strip()
            if not Path(caminho_textos).is_file():
                print(f'\U0001F539 Arquivo não encontrado: {caminho_textos}')
                continue
            break
        except (EOFError, KeyboardInterrupt):
            print('  ')
            print(f'\U0001F539 Operação interrompida: ')

        

    while True:
        print()
        print('1 - anotar')
        print('0 - sair')
        try:
            opcao = input('Escolha uma opção: ').strip()
        except (EOFError, KeyboardInterrupt):
            print(' ')
            print(f'\U0001F539 Interrompido. Até a próxima.')
            break

        if opcao == '1':
            anotar(caminho_textos)
        elif opcao == '0':
            print('\U0001F539 Até a próxima.')
            break
        else:
            print('Opção inválida.')


if __name__ == '__main__':
    main()