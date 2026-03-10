"""
Plot with real values
"""
import numpy as np 
import matplotlib.pyplot as plt

duracao = 1.0
t = np.linspace(0, duracao, 1000)                     # t_sinal é um vetor de 1000 pontos entre 0 e duracao (1 segundo)

sinal_1 = 5 * np.cos(2 * np.pi * 1000 * t) 
sinal_2 = 3 * np.sin(2 * np.pi * 4000 * t)

sinal = sinal_1 + sinal_2

plt.figure(figsize=(10, 4))
plt.title(f'Representação do sinal AC de {sinal_1.max():.2f}V a 1000Hz + {sinal_2.max():.2f}V a 4000Hz')
plt.subplot(2, 2, 1)
plt.plot(t, sinal_1, 'blue', label = 'Sinal 1 (1000Hz)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(t, sinal_2, 'red', label = 'Sinal 2 (4000Hz)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, sinal, 'purple', label = 'Sinal Combinado (1000Hz + 4000Hz)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()

plt.tight_layout()
plt.show()
