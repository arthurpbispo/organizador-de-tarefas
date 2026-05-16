from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from typing import List
from uteis import salvar_tarefa

router = APIRouter()

class Tarefaapi(BaseModel):
    tarefa: str
    importancia: str
    descricao: str
     


@router.get("/")
def boa_vindas():
    return {"mensagem": "Organizador de tarefas"}

@router.post("/tarefas")
#Envia a tarefa ao main
def criar_tarefa(dados: Tarefaapi):
    nova_tarefa_dict = dados.model_dump() 
    
    # 2. Envia para a função do main.py salvar no JSON
    salvar_tarefa("tarefas.json", nova_tarefa_dict)
    
    return {"status": "Enviado ao main e salvo no JSON!", "tarefa": nova_tarefa_dict}

