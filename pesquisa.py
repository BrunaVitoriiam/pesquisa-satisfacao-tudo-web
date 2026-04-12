excelente = 0
bom = 0
ruim = 0

entrevistados = [
    {"nome": "Alberto", "idade": 60, "opiniao": 1},
    {"nome": "Jandira", "idade": 20, "opiniao": 2},
    {"nome": "Claudia", "idade": 26, "opiniao": 1},
    {"nome": "Bruna", "idade": 25, "opiniao": 2},
    {"nome": "Doanto", "idade": 37, "opiniao": 3},
]

for pessoa in entrevistados:
    if pessoa["opiniao"] == 1:
        excelente += 1
    elif pessoa["opiniao"] == 2:
        bom += 1
    elif pessoa["opiniao"] == 3:
        ruim += 1

total = len(entrevistados)

print("RESULTADO FINAL")
print("EXCELENTE:", excelente)
print("BOM:", bom)
print("RUIM:", ruim)
