import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
N = 3
n = np.arange(0, N)
x_n = 1 + 3 * np.cos((2 * np.pi)/N * n) + np.cos((4 * np.pi)/N * n + np.pi/2) # Sinal x[n]

for k in range(N):
    ck = (1/N) * np.sum(x_n * np.exp(-1j * (2 * np.pi * k / N) * n))
    print(f'c[{k}] = {ck:.4f}')
    
plt.figure(figsize=(12, 4))
plt.stem(n, x_n)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title(f'Sinal periódico x[n] com N={N} (n = 0 a {N-1})')
plt.grid(False)
plt.show()