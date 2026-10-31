from pathlib import Path

from anotador import anotar, saida


def main():
    while True:
        try:
            caminho_textos = input('Informe o caminho do arquivo de textos: ').strip()
            break
        except (EOFError, KeyboardInterrupt) as erro:
            print('  ')
            print(f'\U0001F539 Operação interrompida: {erro}')
            return

    if not Path(caminho_textos).exists():
        print(f'Arquivo não encontrado: {caminho_textos}')
        return

    while True:
        print()
        print('1 - anotar')
        print('0 - sair')
        try:
            opcao = input('Escolha uma opção: ').strip()
        except (EOFError, KeyboardInterrupt):
            print('Interrompido. Até a próxima.')
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