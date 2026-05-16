import json
import os
import pandas as pd
import sys

def salvar_tarefa(nome_arquivo, minha_tarefa):
    nome_arquivo = "tarefas.json"
    
    if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            lista_de_tarefas = json.load(arquivo)
    else:
        lista_de_tarefas = []


    lista_de_tarefas.append(minha_tarefa)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista_de_tarefas, arquivo, indent=4, ensure_ascii=False)


def exibir_tarefa():
    if os.path.exists('tarefas.json') and os.path.getsize('tarefas.json') > 0:
        df = pd.read_json('tarefas.json', encoding='utf-8')

        for index, linha in df.iterrows():
            print(f'\ntarefa: {linha['tarefa']}')
            print(f'importancia: {linha['importancia']}')
            print(f'descricao: {linha['descricao']}')
            print('-' * 30)

    else:
        print('Nehuma tarefa encontrada')

def sair_programa():
    print('\nOok, sem problemas')
    sys.exit()
    