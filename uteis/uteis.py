import json
import os
import pandas as pd
from datetime import date

def salvar_tarefa(nome_arquivo, minha_tarefa):
    nome_arquivo = 'JSON/tarefas.json'
    
    if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            lista_de_tarefas = json.load(arquivo)
    else:
        lista_de_tarefas = []
    


    lista_de_tarefas.append(minha_tarefa)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(lista_de_tarefas, arquivo, indent=4, ensure_ascii=False)


def exibir_tarefa():
    nome_arquivo = 'JSON/tarefas.json'

    if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
        df = pd.read_json(nome_arquivo, encoding='utf-8')

        for index, linha in df.iterrows():
            print(f'\nID: {linha['ID']}')
            print(f'tarefa: {linha['tarefa']}')
            print(f'importancia: {linha['importancia']}')
            print(f'descricao: {linha['descricao']}')
            print(f'data: {linha['data']}')
            print('-' * 30)

    else:
        print('Nehuma tarefa encontrada')

def retirar_tarefa():
    nome_arquivo = 'JSON/tarefas.json'
    
    if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:

        df = pd.read_json(nome_arquivo, encoding='utf-8')
        
        id_para_deletar = input('\nDigite o ID da tarefa que deseja remover: ').strip()
    
        if id_para_deletar in df['ID'].values:
            
            df_atualizado = df[df['ID'] != id_para_deletar]
            
            df_atualizado.to_json(nome_arquivo, orient='records', indent=4, force_ascii=False)
            
            print('\nTarefa removida com sucesso!')
        else:
            print('\nAviso: Nenhum item com esse ID foi encontrado.')
            
    else:
        print("\nNenhuma tarefa cadastrada para ser removida.")

def retirar_tarefa_api(ID):
    nome_arquivo = 'JSON/tarefas.json'
    
    if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
        df = pd.read_json(nome_arquivo, encoding='utf-8')
        
        
        id_para_deletar = str(id_para_deletar).strip()
   
        if id_para_deletar in df['ID'].values:
            
           
            df_atualizado = df[df['ID'] != id_para_deletar]
            
            # Salva de volta formatado
            df_atualizado.to_json(nome_arquivo, orient='records', indent=4, force_ascii=False)
            print(f'\nTarefa {id_para_deletar} removida com sucesso!')
            return True
        else:
            print('\nAviso: Nenhum item com esse ID foi encontrado.')
            return False
    else:
        print("\nNenhuma tarefa cadastrada para ser removida.")
        return False

def data():
    hoje = date.today()

    return hoje.strftime('%d/%m/%Y')




        
        

