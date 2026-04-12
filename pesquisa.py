# Programa de Pesquisa de Satisfação - TudoWeb

excelente = 0
bom = 0
ruim = 0

entrevistados = [
    {"nome": "Alberto", "idade": 60, "opiniao": 1},
    {"nome": "Jandira", "idade": 20, "opiniao": 2},
    {"nome": "Claudia", "idade": 26, "opiniao": 1},
    {"nome": "Bruna", "idade": 29, "opiniao": 2},
    {"nome": "Donato", "idade": 37, "opiniao": 3},
    {"nome": "Valentina", "idade": 18, "opiniao": 1},
    {"nome": "Guilherme", "idade": 28, "opiniao": 2},
    {"nome": "Samira", "idade": 34, "opiniao": 3},
    {"nome": "Ferdinando", "idade": 30, "opiniao": 2},
    {"nome": "Claudio", "idade": 30, "opiniao": 1},

    {"nome": "Lucas", "idade": 22, "opiniao": 1},
    {"nome": "Mariana", "idade": 27, "opiniao": 2},
    {"nome": "Roberta", "idade": 35, "opiniao": 3},
    {"nome": "Ana", "idade": 19, "opiniao": 1},
    {"nome": "Rafael", "idade": 40, "opiniao": 2},
    {"nome": "Juliana", "idade": 31, "opiniao": 1},
    {"nome": "Carlos", "idade": 45, "opiniao": 3},
    {"nome": "Fernanda", "idade": 29, "opiniao": 2},
    {"nome": "Ricardo", "idade": 50, "opiniao": 1},
    {"nome": "Patricia", "idade": 33, "opiniao": 2},

    {"nome": "Eduardo", "idade": 38, "opiniao": 3},
    {"nome": "Beatriz", "idade": 24, "opiniao": 1},
    {"nome": "Bruno", "idade": 41, "opiniao": 2},
    {"nome": "Larissa", "idade": 21, "opiniao": 1},
    {"nome": "Roberto", "idade": 55, "opiniao": 3},
    {"nome": "Camila", "idade": 28, "opiniao": 2},
    {"nome": "André", "idade": 36, "opiniao": 1},
    {"nome": "Bianca", "idade": 23, "opiniao": 2},
    {"nome": "Thiago", "idade": 32, "opiniao": 3},
    {"nome": "Vanessa", "idade": 26, "opiniao": 1},

    {"nome": "Leonardo", "idade": 39, "opiniao": 2},
    {"nome": "Aline", "idade": 34, "opiniao": 1},
    {"nome": "Felipe", "idade": 27, "opiniao": 3},
    {"nome": "Tatiane", "idade": 30, "opiniao": 2},
    {"nome": "Bruno", "idade": 42, "opiniao": 1},
    {"nome": "Sabrina", "idade": 25, "opiniao": 2},
    {"nome": "Daniel", "idade": 37, "opiniao": 3},
    {"nome": "Carolina", "idade": 29, "opiniao": 1},
    {"nome": "Marcelo", "idade": 48, "opiniao": 2},
    {"nome": "Renata", "idade": 31, "opiniao": 1},

    {"nome": "Bruna", "idade": 25, "opiniao": 3},
    {"nome": "Simone", "idade": 36, "opiniao": 2},
    {"nome": "Vinicius", "idade": 28, "opiniao": 1},
    {"nome": "Cristiane", "idade": 33, "opiniao": 2},
    {"nome": "Otavio", "idade": 47, "opiniao": 3},
    {"nome": "Helena", "idade": 22, "opiniao": 1},
    {"nome": "Igor", "idade": 35, "opiniao": 2},
    {"nome": "Monica", "idade": 40, "opiniao": 1},
    {"nome": "Rodrigo", "idade": 38, "opiniao": 3},
    {"nome": "Elaine", "idade": 27, "opiniao": 2}
]

for i, pessoa in enumerate(entrevistados):
    opiniao = pessoa["opiniao"]
    
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

total = len(entrevistados)

print("\n====== RESULTADO FINAL ======")
print(f"EXCELENTE: {excelente}")
print(f"BOM: {bom}")
print(f"RUIM: {ruim}")

print("\n--- Percentuais ---")
print(f"EXCELENTE: {excelente / total * 100:.1f}%")
print(f"BOM: {bom / total * 100:.1f}%")
print(f"RUIM: {ruim / total * 100:.1f}%")
