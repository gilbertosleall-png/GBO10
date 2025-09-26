# Balanceador de Operadores — Protótipo

Este é um protótipo de software para **balanceamento de operadores em linhas de produção**.

## Passo 1 — Instalar o Python
- Baixe o Python 3.10+ em: https://www.python.org/downloads/
- Marque a opção **Add Python to PATH** (Windows).

## Passo 2 — Preparar ambiente
Abra o terminal (Prompt de Comando ou PowerShell no Windows, Terminal no mac/Linux).

Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

Atualize o pip:
```bash
python -m pip install --upgrade pip
```

## Passo 3 — Instalar dependências
Na pasta do projeto (onde está este README e os arquivos):
```bash
pip install -r requirements.txt
```

## Passo 4 — Rodar o app Streamlit
```bash
streamlit run balanceador_streamlit.py
```
Abra o link `http://localhost:8501` no navegador.

## Passo 5 — Testar com planilha
Crie um arquivo CSV (exemplo: `tarefas.csv`):
```csv
TaskID,TaskName,Time,Predecessors
T1,Cortar,30,
T2,Costurar,45,T1
T3,Acabamento,20,T2
T4,Embalagem,15,T3
```

No app, faça upload do arquivo e veja os resultados:
- Atribuição de tarefas por operador
- Gráfico de Gantt
- Indicadores de eficiência
- Exportação em Excel/PDF

## Passo 6 — Deploy no Streamlit Cloud (opcional)
1. Suba estes arquivos no GitHub.
2. Vá em https://streamlit.io/cloud → New App.
3. Selecione o repositório e o arquivo `balanceador_streamlit.py`.
4. O app ficará disponível online.

---
Este é um **protótipo educacional**. Para uso real, seria preciso ajustar heurísticas, incluir qualificadores de operador e integrar com ERP/MES.
