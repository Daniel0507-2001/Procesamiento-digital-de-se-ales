# -*- coding: utf-8 -*-
"""sample_rate .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uk0k_euDGuqRg8sjROLUQYqYLDF9SqBv
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
duration = 1.0  # Duración de la señal (segundos)
freq1 = 5       # Frecuencia de la primera componente (Hz)
freq2 = 15      # Frecuencia de la segunda componente (Hz)
sample_rate_high = 1000  # Alta tasa de muestreo (Hz)
sample_rate_low = 30     # Baja tasa de muestreo (Hz)

# Generar señales
t_high = np.linspace(0, duration, int(sample_rate_high * duration), endpoint=False)
t_low = np.linspace(0, duration, int(sample_rate_low * duration), endpoint=False)

signal_high = np.sin(2 * np.pi * freq1 * t_high) + 0.5 * np.sin(2 * np.pi * freq2 * t_high)
signal_low = np.sin(2 * np.pi * freq1 * t_low) + 0.5 * np.sin(2 * np.pi * freq2 * t_low)

# Calcular FFT
fft_high = np.fft.fft(signal_high)
fft_low = np.fft.fft(signal_low)
freqs_high = np.fft.fftfreq(len(fft_high), 1 / sample_rate_high)
freqs_low = np.fft.fftfreq(len(fft_low), 1 / sample_rate_low)

# Graficar señales en el tiempo
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(t_high, signal_high, label="Alta tasa de muestreo")
plt.title("Señal - Alta Tasa de Muestreo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

plt.subplot(2, 2, 2)
plt.stem(t_low, signal_low, label="Baja tasa de muestreo", basefmt=" ")
plt.title("Señal - Baja Tasa de Muestreo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

# Graficar FFT
plt.subplot(2, 2, 3)
plt.plot(freqs_high[:len(freqs_high)//2], np.abs(fft_high)[:len(fft_high)//2], label="Alta tasa de muestreo")
plt.title("Espectro de Frecuencia - Alta Tasa")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()

plt.subplot(2, 2, 4)
plt.stem(freqs_low[:len(freqs_low)//2], np.abs(fft_low)[:len(fft_low)//2], label="Baja tasa de muestreo", basefmt=" ")
plt.title("Espectro de Frecuencia - Baja Tasa")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()

plt.tight_layout()
plt.show()

"""La imagen demuestra la importancia de seleccionar una tasa de muestreo adecuada. Con una tasa alta, la señal se representa fielmente tanto en el tiempo como en la frecuencia. Con una tasa baja, aunque se cumplen las condiciones mínimas, la calidad de la representación se degrada, lo que puede ser crítico en aplicaciones de alta precisión."""