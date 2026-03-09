"""
Sub plots
"""

import numpy as np
import matplotlib.pyplot as plt

duracao = 1.0 
t = np.linspace(0, duracao, 1000)
"""
Sinal europeu de 50Hz e amplitude de 325.26V (tensão eficaz de 230V)
"""
freq_ue = 50.0
amplitude_ue = 325.26
sinal_ue = amplitude_ue * np.sin(2 * np.pi * freq_ue * t)

"""
Sinal americano de 60Hz e amplitude de 339.41V (tensão eficaz de 240V)_summary_
"""
freq_usa = 60.0
amplitude_usa = 120.0 * np.sqrt(2)
sinal_usa = amplitude_usa * np.sin(2 * np.pi * freq_usa * t)

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)                            # 2 linhas, 1 coluna, primeiro subplot 
plt.plot(t, sinal_ue, 'b', label='Sinal AC Europeu (50Hz, 230V RMS)')
plt.title('Sinal AC Europeu')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
#plt.legend()


plt.subplot(2, 2, 2)                            # 2 linhas, 1 coluna, segundo subplot
plt.plot(t, sinal_usa, 'r', label='Sinal AC Americano (60Hz, 120V RMS)')
plt.title('Sinal AC Americano')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
#plt.legend()

plt.subplot(2, 2, 3)                            # 2 linhas, 1 coluna, segundo subplot
plt.plot(t, sinal_usa, 'r', label='Sinal AC Americano (60Hz, 120V RMS)')
plt.title('AMERICAN AC SIGNAL')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
#plt.legend()

plt.subplot(2, 2, 4)                            # 2 linhas, 1 coluna, primeiro subplot 
plt.plot(t, sinal_ue, 'b', label='Sinal AC Europeu (50Hz, 230V RMS)')
plt.title('EUROPEAN AC SIGNAL')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid()
#plt.legend()

plt.tight_layout()                              # Ajusta o layout para evitar sobreposição de títulos e rótulos
plt.show()