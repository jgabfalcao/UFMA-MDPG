def main():
    entrada = input()
    linha, coluna = [int(valor) for valor in entrada.split()]
  
    if(linha <= 0 or linha >= 10000 or coluna <= 0 or coluna >= 10000):
        return 0
  
    matriz = criando_matriz(linha, coluna)
    matriz, conta_rei = preenchendo_matriz(matriz)
       
    print(conta_rei)
    print()
    print("-----MATRIZ-----")
    print()
  
    for linha in matriz:
        for elemento in linha:
            if elemento == "R":
                print("\033[93m" + elemento + "\033[0m", end=" ")
            else:
                print(elemento, end=" ")
        print()  
        
    print()
  
def criando_matriz(linha, coluna):
    matriz = [[0 for _ in range(coluna)] for _ in range(linha)] 
    return matriz

def preenchendo_matriz(matriz):
    conta_rei = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    
    for i in range(linha):
        for j in range(coluna):
            if (i + j) % 2 == 0:
                if not ataca_outro_rei(matriz, i, j):
                    matriz[i][j] = "R" 
                    conta_rei += 1
    return(matriz, conta_rei)

def ataca_outro_rei(matriz, linha, coluna):
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
                if matriz[i][j] == "R":
                    return True
    return False

main()