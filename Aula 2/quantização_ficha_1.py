import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
#duracao = 1.0
#t = np.linspace(0, duracao, 1000)  # Tempo de 0 a 1 segundo, com 1000 amostras
frequencia = 1000  # Frequência do sinal em Hz
T = 1 / frequencia  # Período do sinal
t = np.arange(0, 2*T, T/1000)  # Tempo de 0 a 2 períodos, com 1000 amostras por período
amplitude = 3
sinal = 3*np.cos(2 * np.pi * frequencia * t)  # Sinal original


#####################################daDOS AMOSTRAGEM #############33FA
fa = 10000
T_amostragem = 1 / fa
n_amostras = int(2*T / T_amostragem)  # Número de amostras em 2 períodos
t_amostragem = np.arange(0, 2*T, T_amostragem)  # Tempo de amostragem
sinal_amostrado = 3*np.cos(2 * np.pi * frequencia * t_amostragem)  # Sinal amostrado

######################################################################################
#x_min, x_max = sinal.min(), sinal.max()  
x_min, x_max = -3, 3 # Amplitude do sinal
#print(f'Amplitude do sinal: {x_min:.2f}V a {x_max:.2f}V')

niveis_quantizacao = 4  # Quantização de 4 bits (2^4 = 16 níveis)
n_niveis = 2 ** niveis_quantizacao
delta = (x_min - x_max) / n_niveis  # Passo de quantização
sinal_quantizado = np.round((sinal_amostrado - x_min) / delta) * delta - x_min  # Quantização do sinal amostrado


plt.figure(figsize=(10, 5))
plt.title("Sinal Original")
plt.plot(t, sinal, label="Sinal Original")

plt.stem(t_amostragem, sinal_amostrado, linefmt='C1-', markerfmt='C1o', basefmt=' ', label='Sinal Amostrado')

plt.step(t_amostragem, sinal_quantizado, label="Sinal Quantizado", where="mid", color='r')

plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


