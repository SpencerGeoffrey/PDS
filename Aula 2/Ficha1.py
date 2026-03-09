# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:17:34 2025

@author: PT
"""

#%%  PDS - Ficha de exercícios nº1

import numpy as np
import matplotlib.pyplot as plt

fs = 10000  # Frequência de amostragem (10 kHz)
T = 1       # Duração do sinal em segundos
t = np.linspace(0, T, fs, endpoint=False)  # Vetor de tempo
f = 1000    # Frequência do sinal (1 kHz)
x = 3 * np.cos(2 * np.pi * f * t)

#%% Quantização de 4 bits
n_bits = 4
n_niveis = 2**n_bits
x_min, x_max = -3, 3  # Amplitude do sinal
delta = (x_max - x_min) / n_niveis
x_q = np.round((x - x_min) / delta) * delta + x_min  # Quantização


plt.figure(figsize=(10, 5))
plt.plot(t[:50], x[:50], label="Sinal Original", linestyle="--", alpha=0.7)
plt.step(t[:50], x_q[:50], label="Sinal Quantizado", where="mid", color = 'r')
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Quantização")
plt.grid()
plt.show()
