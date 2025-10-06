from queue import Queue, PriorityQueue

# 1 - Implementação de uma Fila comum

print("=== 1 - Fila comum ===")
fila = Queue()

fila.put("Pessoa 1")
fila.put("Pessoa 2")
fila.put("Pessoa 3")

while not fila.empty():
    pessoa = fila.get()
    print(f"Atendendo: {pessoa}")

# 2 - Implementação de uma Fila Prioritária

print("\n=== 2 - Fila Prioritária ===")


fila_prioritaria = PriorityQueue()

fila_prioritaria.put((3, "Baixa prioridade"))
fila_prioritaria.put((1, "Alta prioridade"))
fila_prioritaria.put((2, "Média prioridade"))

while not fila_prioritaria.empty():
    prioridade, item = fila_prioritaria.get()
    print(f"Atendendo: {item} (Prioridade {prioridade})")

# 3 - Teste com múltiplos itens de diferentes prioridades

print("\n=== 3 - Teste com 5 itens de cada prioridade ===")

fila_prioritaria = PriorityQueue()

for i in range(1, 6):
    fila_prioritaria.put((1, f"Alta {i}"))
for i in range(1, 6):
    fila_prioritaria.put((2, f"Média {i}"))
for i in range(1, 6):
    fila_prioritaria.put((3, f"Baixa {i}"))

while not fila_prioritaria.empty():
    prioridade, item = fila_prioritaria.get()
    print(f"Atendendo: {item} (Prioridade {prioridade})")

print("\nObservação:")
print("- Os itens de alta prioridade foram atendidos primeiro.")
print("- Depois vieram os de prioridade média.")
print("- Por último, os de prioridade baixa.")
print("- Dentro de cada prioridade, foi mantida a ordem de chegada.")

# 4 - Simulação de Round Robin

print("\n=== 4 - Simulação Round Robin ===")

processos = [
    {"id": "P1", "tempo": 5},
    {"id": "P2", "tempo": 7},
    {"id": "P3", "tempo": 3}
]

quantum = 2

fila = Queue()
for p in processos:
    fila.put(p)

while not fila.empty():
    processo = fila.get()
    id_proc = processo["id"]
    tempo_restante = processo["tempo"]

    tempo_executado = min(quantum, tempo_restante)
    tempo_restante -= tempo_executado

    print(f"{id_proc} executou {tempo_executado} unidades (restam {tempo_restante})")
    if tempo_restante > 0:
        processo["tempo"] = tempo_restante
        fila.put(processo)

print("\nTodos os processos foram concluídos!")
