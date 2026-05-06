#TESTE
import matplotlib.pyplot as plt

def desenhar_detalhamento(bw, h, n_barras, bitola_mm, c_cm, diam_est_mm):
    fig, ax = plt.subplots(figsize=(6, 10))
    
    # Conversões para cm (unidade padrão do gráfico)
    phi_barra = bitola_mm / 10
    phi_est = diam_est_mm / 10
    
    # 1. Contorno da viga
    viga = plt.Rectangle((0, 0), bw, h, fill=False, color='black', linewidth=3)
    ax.add_patch(viga)
    
    # 2. Estribo (Cobrimento interno)
    estribo = plt.Rectangle((c_cm, c_cm), bw - 2*c_cm, h - 2*c_cm, 
                             fill=False, color='gray', linestyle='--', linewidth=1.5)
    ax.add_patch(estribo)
    
    # 3. Lógica de Camadas (Pulo do gato para a Questão 11)
    # Espaço horizontal livre entre estribos
    largura_util = bw - 2*c_cm - 2*phi_est
    espacamento_min = max(2.0, phi_barra) # NBR 6118 [cite: 213, 301]
    
    # Quantas barras cabem por camada?
    n_por_camada = int((largura_util + espacamento_min) // (phi_barra + espacamento_min))
    
    # Plotagem das barras
    barras_desenhadas = 0
    camada = 0
    
    while barras_desenhadas < n_barras:
        barras_nesta_camada = min(n_barras - barras_desenhadas, n_por_camada)
        
        # Ajusta o espaçamento para centralizar as barras na camada
        if barras_nesta_camada > 1:
            e_h_real = (largura_util - barras_nesta_camada * phi_barra) / (barras_nesta_camada - 1)
        else:
            e_h_real = 0
            
        x_inicial = c_cm + phi_est + phi_barra/2
        if barras_nesta_camada == 1: x_inicial = bw / 2 # Centraliza barra única
            
        for i in range(barras_nesta_camada):
            x = x_inicial + i * (phi_barra + e_h_real)
            y = c_cm + phi_est + phi_barra/2 + camada * (phi_barra + 2.0) # 2cm de ev [cite: 227]
            
            circ = plt.Circle((x, y), radius=phi_barra/2, color='blue')
            ax.add_patch(circ)
            barras_desenhadas += 1
            
        camada += 1

    # Configurações do Gráfico
    ax.set_xlim(-5, bw + 5)
    ax.set_ylim(-5, h + 5)
    ax.set_aspect('equal')
    plt.title(f"Detalhamento: {n_barras}Φ{bitola_mm}mm\n(Passo a passo NBR 6118)", fontsize=12)
    plt.xlabel("Largura bw (cm)")
    plt.ylabel("Altura h (cm)")
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.show() # <--- ESSENCIAL para mostrar na tela!
    # Em vez de plt.show(), salve um arquivo na pasta
    plt.savefig('visualizacao/detalhamento_viga.png', dpi=300)
    print("Imagem salva em visualizacao/detalhamento_viga.png")

# Teste com os dados da sua Prova (Questão 11)
# bw=20, h=70, 7 barras de 20mm, cobrimento 4cm, estribo 5mm
desenhar_detalhamento(20, 70, 7, 20, 4, 5)