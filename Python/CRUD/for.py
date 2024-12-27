tarefas = ["Estudar Python", "Fazer exercícios", "Descansar"]

print("Suas tarefas de hoje:")
for tarefa in tarefas:
    print(f"- {tarefa}")
    resposta = input(f"Você já completou a tarefa '{tarefa}'? (sim/não): ")
    if resposta.lower() == "sim":
        print("Ótimo trabalho!")
    else:
        print("Não esqueça de fazer!")
    print("----")

A = 1

for A in range(3,10):
    print(A)