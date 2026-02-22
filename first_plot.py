"""
First plot with matplotlib sine wave
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

sinx = np.sin(x)                        # calcula o seno de cada valor de x e armazena em sinx
plt.plot(x, sinx)                       # plota os valores de x no eixo horizontal e os valores de sinx no eixo vertical
plt.title("Sine wave")                  # adiciona um título ao gráfico
plt.show()                              # mostra o gráfico
