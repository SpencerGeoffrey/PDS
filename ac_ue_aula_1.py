"""
Plot with real values
"""
import numpy as np 
import matplotlib.pyplot as plt

duracao = 1.0
t = np.linspace(0, duracao, 1000)                     # t_sinal é um vetor de 1000 pontos entre 0 e duracao (1 segundo)

amplitude_sinal = 325.26
freq = 50

sinal = amplitude_sinal * np.sin(2 * np.pi * freq * t)        #v(t) = A * sin(2 * pi * f * t) -> A é a amplitude do sinal, f é a frequência, t é o tempo. O resultado é um vetor de valores do sinal AC ao longo do tempo.

plt.figure(figsize=(10, 4))
plt.title(f'Representação do sinal AC de {amplitude_sinal:.2f}V a {freq}Hz')

plt.plot(t, sinal, 'blue', label = 'Sinal Alternado (contínuo)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.show()