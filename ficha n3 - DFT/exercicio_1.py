import numpy as np
import matplotlib.pyplot as plt

N = 4
x_n = [0, 1, 2, 3]

n   = np.arange(-8, 9)          
x_n = np.take(x_n, n % N)

#reoresentacao da onda...
plt.figure(figsize=(12, 4))
plt.stem(n, x_n)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title(f'Sinal periódico x[n] com N={N} (n = -8 a 8)')
plt.grid(False)
plt.show()

#claculo coeficientes 

Omega0 = 2 * np.pi / N
n = np.arange(N)          
x_period = np.array([0, 1, 2, 3]) 

ck = np.zeros(N, dtype=complex)

for k_val in range(N):
    ck[k_val] = (1/N) * np.sum(x_period * np.exp(-1j * k_val * Omega0 * n))
    print(f'c[{k_val}] = {ck[k_val]:.4f}')
#print(ck)