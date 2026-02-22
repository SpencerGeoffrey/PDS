import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
f = 5.0          # Hz  — frequência real do fenómeno
fa = 50.0        # Hz  — frequência de amostragem (fa >= 2*f para evitar aliasing))
T = 1 / fa       # intervalo entre amostras (segundos)

duracao = 1.0    # segundos que queremos observar
n = np.arange(0, int(duracao * fa))   # 0, 1, 2, ..., N-1

# Tempo real associado a cada amostra
t = n * T        # <--- Esta é a linha mais importante da aula!

# Sinal amostrado
sinal = np.sin(2 * np.pi * f * t)

# Para comparar com o "verdadeiro" contínuo
t_cont = np.linspace(0, duracao, 1000)
sinal_cont = np.sin(2 * np.pi * f * t_cont)

# Gráfico — mostrar as amostras como pontos e stem
plt.figure(figsize=(10, 4))
plt.plot(t_cont, sinal_cont, 'lightblue', label='sinal contínuo (verdadeiro)')
plt.stem(t, sinal, linefmt='C1-', markerfmt='C1o', basefmt=' ', label='amostras (o que temos no PC)')
plt.xlabel('Tempo real t (segundos)')
plt.ylabel('Amplitude')
plt.title(f'Sinal de {f} Hz amostrado a fa = {fa} Hz → {fa/f:.1f} amostras por período')
plt.grid(True)
plt.legend()
plt.show()