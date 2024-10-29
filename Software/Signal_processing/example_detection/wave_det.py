import scipy.io
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo .mat
mat_data = scipy.io.loadmat('100m.mat')
print("Claves disponibles en el archivo .mat:", mat_data.keys())

# Cargar la señal ECG (ajusta 'val' según sea necesario)
ecg_signal = mat_data['val'].flatten()  
print("Señal ECG cargada:", ecg_signal[:10])

# Definir la frecuencia de muestreo
sampling_rate = 360  # Cambia este valor si es necesario

# Preprocesar la señal ECG
cleaned_ecg = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)

# Procesar la señal para encontrar picos y ondas PQRST
ecg_signals, info = nk.ecg_process(cleaned_ecg, sampling_rate=sampling_rate)

# Encontrar los picos (incluyendo P, Q, R, S y T)
peaks = nk.ecg_findpeaks(ecg_signals, sampling_rate=sampling_rate)

# Definir los índices para graficar (ajustar según sea necesario)
start_index = 0          # Índice de inicio
end_index = start_index + (sampling_rate * 5)  # Mostrar 5 segundos de datos

# Ploteo de la señal ECG y las ondas PQRST
plt.figure(figsize=(12, 6))

# Graficar la señal limpia
plt.plot(ecg_signals['ECG_Clean'][start_index:end_index], label='ECG Limpio', color='blue')

# Graficar los picos detectados (P, Q, R, S y T)
plt.scatter(peaks['ECG_R_Peaks'], ecg_signals['ECG_Clean'][peaks['ECG_R_Peaks']], color='red', label='Picos R', zorder=5)

# Verificar si hay picos P y T
if 'ECG_P_Peaks' in peaks:
    plt.scatter(peaks['ECG_P_Peaks'], ecg_signals['ECG_Clean'][peaks['ECG_P_Peaks']], color='green', label='Picos P', zorder=5)

if 'ECG_T_Peaks' in peaks:
    plt.scatter(peaks['ECG_T_Peaks'], ecg_signals['ECG_Clean'][peaks['ECG_T_Peaks']], color='orange', label='Picos T', zorder=5)

# Etiquetas y leyenda
plt.title('Señal ECG y Picos PQRST Detectados')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.xlim(start_index, end_index)  # Ajustar el eje x para mostrar solo el rango deseado
plt.show()
