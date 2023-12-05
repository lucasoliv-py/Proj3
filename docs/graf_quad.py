# Getting Started Matplotlib

# Importação das bibliotecas de geração de gráficos
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Definição de funções
def quadratica(x):
    return x*x

# Atribuição de variáveis
x = np.linspace(-5, 5, 100)
y = quadratica(x)

# Processamento de dados
fig, ax = plt.subplots()
ax.plot(x,y)

# Saída de dados
plt.show()