"""
Multiple plots in same windoeww
"""
import matplotlib.pyplot as plt
import numpy as np

duracao = 1.0
t_sinal = np.linspace(0, duracao, 1000)
""" Sinal europeu de 50Hz e amplitude de 325.26V (tensão eficaz de 230V) """
freq_ue = 50 
amplitude_sinal_ue = 325.26
sinal_ue = amplitude_sinal_ue * np.sin(2 * np.pi * freq_ue * t_sinal) 


""" sinal americano de 60Hz e amplitude de 339.41V (tensão eficaz de 240V) """
freq_usa = 60
amplitude_sinal_usa = 120.0 * np.sqrt(2)                                # 120V RMS -> 120 * sqrt(2) V de amplitude
sinal_usa = amplitude_sinal_usa * np.sin(2 * np.pi * freq_usa * t_sinal)

plt.figure(figsize=(10, 4))
plt.plot(t_sinal, sinal_ue, 'b', label='Sinal AC europeu (50Hz, 230V RMS)')
plt.plot(t_sinal, sinal_usa, 'r', label='Sinal AC americano (60Hz, 120V RMS)')
plt.title('Comparação entre sinais AC europeu e americano')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.legend()
plt.show()