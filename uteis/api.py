from fastapi import APIRouter, FastAPI  
from pydantic import BaseModel
import os
import pandas as pd
from uteis.uteis import salvar_tarefa
from uteis.uteis import retirar_tarefa_api

router = APIRouter()

class Tarefaapi(BaseModel):
    tarefa: str
    importancia: str
    descricao: str
     


@router.get("/")
def boa_vindas():
    return {"mensagem": "Organizador de tarefas"}

@router.post("/tarefas")
def criar_tarefa(dados: Tarefaapi):
    nova_tarefa_dict = dados.model_dump() 
    
    salvar_tarefa("tarefas.json", nova_tarefa_dict)
    
    return {"status": "Enviado ao main e salvo no JSON!", "tarefa": nova_tarefa_dict}

@router.get("/exibirtarefas")
def visualizar_tarefas():
    nome_arquivo = 'JSON/tarefas.json'

    if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
        df = pd.read_json(nome_arquivo, encoding='utf-8')

        dados_para_front = df.to_dict(orient='records')
        return dados_para_front
    else:
        return {"mensagem": "Não existem tarefas"}
    
@router.delete("/retirartarefas/{id_tarefa}")
def api_retirar_tarefa(id_tarefa: str):
    sucesso = retirar_tarefa_api(id_tarefa)
    
    if sucesso:
        return {"status": "Sucesso", "mensagem": f"Tarefa com ID {id_tarefa} excluída."}
    else:
        return {"status": "Erro", "mensagem": "Tarefa não encontrada ou arquivo vazio."}
    


