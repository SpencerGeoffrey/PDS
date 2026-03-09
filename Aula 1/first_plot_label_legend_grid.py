"""
Continuing with the same data as before, we can add labels, a legend, and a grid to the plot.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
sinx = np.sin(x)                        # calcula o seno de cada valor de x e armazena em sinx

plt.plot(x, sinx, label='sin(x)')
plt.title("Sine wave")                  # adiciona um título ao gráfico
plt.xlabel("x")                         # adiciona um rótulo ao eixo x
plt.ylabel("sin(x)")                    # adiciona um rótulo ao eixo y
plt.legend()                            # adiciona uma legenda ao gráfico
plt.grid()                              # adiciona uma grade ao gráfico  ---> False para remover a grade
plt.show()                              # mostra o gráfico