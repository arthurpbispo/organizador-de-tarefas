import json
import os

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

if __name__ == "__main__":
    tarefa = input('Digite uma tarefa: ')
    grau_de_importancia = input('Qual é o grau de importancia: ')
    descricao = input('Qual e a sua descricao: ')

    minha_tarefa = Tarefa(tarefa, grau_de_importancia, descricao)
    salvar_tarefa("tarefas.json", minha_tarefa.para_dict())
    print('Tarefa salva com sucesso pelo terminal!')




        