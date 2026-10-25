# anotador

Ferramenta de terminal para rotular textos e guardar os rótulos em JSON. 

## Status

Em desenvolvimento. Por enquanto o projeto lê e grava arquivos JSON. O loop de anotação, as estatísticas e a exportação para CSV ainda não existem.

## Como rodar

Precisa de Python 3.10 ou superior.

```bash
git clone <url-do-repositorio>
cd anotador
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Formato dos dados

A entrada é uma lista de textos com id (veja `dados/texto_teste.json`):

```json
[
  {"id": 1, "texto": "Adorei o atendimento, super rápido."},
  {"id": 2, "texto": "O produto chegou quebrado."}
]
```

As anotações vão para `saida/anotacoes.json`, com os mesmos campos mais o `rotulo`. Os atalhos de rótulo são `p` (positivo), `n` (negativo) e `ne` (neutro).

## Próximos passos

- loop de anotação que continua de onde parou
- comando de estatísticas
- exportação para CSV
- testes com pytest


