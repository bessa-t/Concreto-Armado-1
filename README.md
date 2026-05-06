# Dimensionamento de Concreto Armado - NBR 6118:2023

Este repositório contém uma ferramenta modular em Python desenvolvida para automatizar o dimensionamento e a verificação de elementos estruturais de concreto armado (vigas), com foco total na conformidade normativa brasileira.

## 🚀 Diferenciais do Projeto

*   **Memorial de Cálculo Dinâmico:** Utiliza a biblioteca `handcalcs` para gerar resoluções passo a passo, facilitando a transcrição e auditoria dos resultados.
*   **Arquitetura Data-Driven:** As propriedades das armaduras são gerenciadas via arquivos externos (`anexos/bitolas.csv`), permitindo atualizações sem alteração no motor de cálculo.
*   **Visualização Técnica:** Geração automática de croquis da seção transversal com `matplotlib`.
*   **Modularização:** Separação clara entre modelos constitutivos de materiais, lógica de dimensionamento e pós-processamento gráfico.

## 📁 Estrutura do Repositório

*   `calculos/`: Motor principal com as rotinas de flexão, cisalhamento e propriedades de materiais.
*   `anexos/`: Dados externos para consulta de bitolas comerciais.
*   `visualizacao/`: Scripts para geração de gráficos e figuras das seções transversais.
*   `notebooks/`: Ambiente interativo (Jupyter) para execução dos cálculos e resolução de casos práticos.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.10+** (Ambiente WSL/Linux)
*   **NumPy & Pandas**: Processamento numérico e manipulação de dados.
*   **Matplotlib**: Representação gráfica das seções.
*   **Handcalcs**: Renderização de fórmulas em LaTeX para memoriais de cálculo.

---
Desenvolvido como parte das atividades acadêmicas de Engenharia Civil na **Universidade de Brasília (UnB)**.
