"""
Plot with real values
"""
import numpy as np 
import matplotlib.pyplot as plt

duracao = 1.0
t = np.linspace(0, duracao, 1000)                     # t_sinal é um vetor de 1000 pontos entre 0 e duracao (1 segundo)

amplitude_sinal_ue = 230 * np.sqrt(2)                                # 120V RMS -> 120 * sqrt(2) V de amplitude
freq_ue = 50
sinal_ue = amplitude_sinal_ue * np.sin(2 * np.pi * freq_ue * t)

amplitude_sinal_usa = 120.0 * np.sqrt(2)                                # 120V RMS -> 120 * sqrt(2) V de amplitude
freq_usa = 60
sinal_usa = amplitude_sinal_usa * np.sin(2 * np.pi * freq_usa * t)

plt.figure(figsize=(10, 4))
plt.title(f'Representação do sinal AC UE vs USA')

plt.plot(t, sinal_ue, 'blue', label = f'Sinal Alternado UE ({freq_ue}Hz)')
plt.plot(t, sinal_usa, 'red', label = f'Sinal Alternado USA ({freq_usa}Hz)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.show()