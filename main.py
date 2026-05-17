from fastapi import FastAPI
from uteis.api import router as api_router
from uteis.uteis import salvar_tarefa
from uteis.uteis import exibir_tarefa
from uteis.uteis import retirar_tarefa
from uteis.uteis import data
import uuid


app = FastAPI()
app.include_router(api_router)



class Tarefa:
    def __init__(self, tarefa, importancia, descricao, id, data):
        self.id = id
        self.tarefa = tarefa
        self.importancia = importancia
        self.descricao = descricao
        self.data = data
    
    def __str__(self):
        return f"[{self.tarefa}] {self.importancia}: {self.descricao} {self.id} {self.data}"

    def para_dict(self):
        return {
            "ID": self.id,
            "tarefa": self.tarefa,
            "importancia": self.importancia,
            "descricao": self.descricao,
            "data": self.data
        }
    

    

if __name__ == "__main__":   
    while True:
        try:
            escolha_usuario = int(input('\nO que voce deseja escolher ? \n(1) Salvar Tarefa \n(2) Ver tarefas \n(3) Sair do programa \n(4) Retirar tarefa: '))
        except ValueError:

            print("Por favor digite apenas numeros validos (1, 2, 3 ou 4).")
            continue  


        if escolha_usuario == 1:
            tarefa = input('\nDigite uma tarefa: ')
            grau_de_importancia = input('\nQual é o grau de importancia: ')
            descricao = input('\nQual e a sua descricao: ')
            id = str(uuid.uuid4())
            data_atual = data()

            minha_tarefa = Tarefa(tarefa, grau_de_importancia, descricao, id, data_atual)
            salvar_tarefa("tarefas.json", minha_tarefa.para_dict())
            print('Tarefa salva com sucesso pelo terminal!')

        elif escolha_usuario == 2:
            exibir_tarefa()

        elif escolha_usuario == 3:
            print("Saindo do programa... Até mais!")
            break 

        elif escolha_usuario == 4:
            retirar_tarefa()
            
        else:
            print("Opção inválida! Escolha um número de 1 a 4.")
    
    
    
    





        