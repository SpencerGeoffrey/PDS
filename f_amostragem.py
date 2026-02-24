import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
f = 5.0                                             # Hz  — frequência real do fenómeno

fa = 500.0                                           # Hz  — frequência de amostragem (fa >= 2*f para evitar aliasing))
T_amostras = 1 / fa                                          # intervalo entre amostras (segundos)
print(f'T_amostras{T_amostras:.4f} segundos')


#criacao do eixo do tepo discreto (ou seja, das amostras)
duracao = 1.0                                       # segundos que queremos observar
n = np.arange(0, int(duracao * fa))                 # lista de indicies interiros [0, 1, 2, ..., N-1] (representa o número de amostras, N = fa * duracao)

# Tempo real associado a cada amostra
t = n * T_amostras                                  # t[0] = 0, t[1] = T, t[2] = 2*T, ..., t[N-1] = (N-1)*T
sinal = 5* np.sin(2 * np.pi * f * t)                # Sinal amostrado

# gerar o sinal contínuo que de seguida será amostrado (para comparação visual)
t_cont = np.linspace(0, duracao, 1000)
sinal_cont = 5 * np.sin(2 * np.pi * f * t_cont)

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