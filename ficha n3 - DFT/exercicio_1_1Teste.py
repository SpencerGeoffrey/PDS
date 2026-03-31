import numpy as np
import matplotlib.pyplot as plt

N = 4 
Omega = (2 *np.pi)/N
print(f'Omega: {Omega}')

n = np.arange(0, N)
x_n = [0, 1, 2, 3]

for k in range(N):
    ck = (1/N) * np.sum(x_n * np.exp(-1j * k * Omega * n))
    print(f'c[{k}] = {ck:.4f}')
    
plt.figure(figsize=(12, 4))
plt.stem(n, x_n)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title(f'Sinal periódico x[n] com N={N} (n = {n[0]} a {N-1})')
plt.grid(False)
plt.show()