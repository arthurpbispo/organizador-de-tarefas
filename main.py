from fastapi import FastAPI
from api import router as api_router
from uteis import salvar_tarefa
from uteis import exibir_tarefa
from uteis import sair_programa


app = FastAPI()
app.include_router(api_router)



class Tarefa:
    def __init__(self, tarefa, importancia, descricao):
        self.tarefa = tarefa
        self.importancia = importancia
        self.descricao = descricao
    
    def __str__(self):
        return f"[{self.tarefa}] {self.importancia}: {self.descricao}"

    def para_dict(self):
        return {
            "tarefa": self.tarefa,
            "importancia": self.importancia,
            "descricao": self.descricao
        }
    

    

if __name__ == "__main__":
    while True:     
        escolha_usuario = int(input('\nO que voce deseja escolher ? \n(1) Salvar Tarefa \n(2) Ver tarefas \n(3) Sair do programa'))

        if escolha_usuario == 1:
            tarefa = input('\nDigite uma tarefa: ')
            grau_de_importancia = input('\nQual é o grau de importancia: ')
            descricao = input('\nQual e a sua descricao: ')

            minha_tarefa = Tarefa(tarefa, grau_de_importancia, descricao)
            salvar_tarefa("tarefas.json", minha_tarefa.para_dict())
            print('Tarefa salva com sucesso pelo terminal!')
        
        elif escolha_usuario == 2:
            exibir_tarefa()
        
        elif escolha_usuario == 3:
            sair_programa()
    
    
    
    





        