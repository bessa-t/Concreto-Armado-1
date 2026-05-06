#TESTE
import matplotlib.pyplot as plt

def plotar_secao(bw, h, as_escolhido, n_barras, bitola):
    fig, ax = plt.subplots()
    
    # 1. Desenha o contorno da viga (Retângulo)
    secao = plt.Rectangle((0, 0), bw, h, fill=False, color='black', linewidth=2)
    ax.add_patch(secao)
    
    # 2. Desenha os estribos (Baseado no cobrimento c)
    # c = 4.0 conforme sua prova [cite: 165]
    
    # 3. Desenha as barras de aço (Círculos)
    # Aqui você usa a lógica de espaçamento que você calculou no papel [cite: 176, 210]
    for i in range(n_barras):
        # Calcula a posição x_pos de cada barra
        circulo = plt.Circle((x_pos, y_pos), radius=bitola/20, color='blue')
        ax.add_patch(circulo)
        
    plt.title(f"Detalhamento da Seção: {n_barras} Φ {bitola}")
    plt.axis('equal')
    plt.show()