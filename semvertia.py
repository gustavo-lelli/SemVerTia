import numpy as np

def rotacao(theta):
    rad = np.radians(theta)
    return np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

def escalamento(sx, sy):
    return np.array([[sx, 0], [0, sy]])

def aplicar_transformacoes(transformacoes):
    A = np.identity(2)
    for t in transformacoes:
        if t[0] == 'R':
            A = np.dot(rotacao(t[1]), A)
        elif t[0] == 'E':
            A = np.dot(escalamento(t[1], t[2]), A)
    return A

def verificar_matriz(A):
    if np.linalg.det(A) == 0:
        return "SemVerTia"
    else:
        return "SimTia, te vejo!"

# Leitura da entrada
n = int(input())
transformacoes = []
for _ in range(n):
    entrada = input().split()
    if entrada[0] == 'R':
        transformacoes.append(('R', float(entrada[1])))
    elif entrada[0] == 'E':
        transformacoes.append(('E', float(entrada[1]), float(entrada[2])))

# Aplicar transformações e verificar a matriz resultante
A = aplicar_transformacoes(transformacoes)
resultado = verificar_matriz(A)
print(resultado)