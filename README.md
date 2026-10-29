# anotador

Ferramenta de terminal para rotular textos e guardar os rótulos em JSON.

## Status

Em desenvolvimento. A anotação funciona e continua de onde parou. As estatísticas, a exportação para CSV e os testes ainda não existem.

## Como rodar

Precisa de Python 3.10 ou superior.

```bash
git clone <url-do-repositorio>
cd anotador
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como usar

```bash
python3 main.py
```

Informe o caminho do arquivo de textos (por exemplo `dados/texto_teste.json`) e escolha anotar no menu. Para cada texto, responda com o atalho do rótulo, `s` para pular ou `q` para sair guardando o progresso. Os textos pulados voltam na próxima vez.

## Formato dos dados

A entrada é uma lista de textos com id (veja `dados/texto_teste.json`):

```json
[
  {"id": 1, "texto": "Adorei o atendimento, super rápido."},
  {"id": 2, "texto": "O produto chegou quebrado."}
]
```

As anotações vão para `saida/anotacoes.json`, com os mesmos campos mais o `rotulo`. Os atalhos de rótulo são `p` (positivo), `n` (negativo) e `ne` (neutro).

## a fazer: 

- comando de estatísticas
- exportação para CSV
- testes com pytest
