import scipy.io
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo .mat
mat_data = scipy.io.loadmat('100m.mat')
print("Claves disponibles en el archivo .mat:", mat_data.keys())

# Verificar si 'val' está en las claves del archivo
if 'val' in mat_data:
    # Cargar la señal ECG
    ecg_signal = mat_data['val'].flatten()  
    print("Señal ECG cargada:", ecg_signal[:10])
else:
    print("La clave 'val' no se encontró en el archivo .mat.")
    exit()

# Preprocesar la señal ECG
cleaned_ecg = nk.ecg_clean(ecg_signal, sampling_rate=360)

# Procesar la señal para encontrar picos
ecg_signals, info = nk.ecg_process(cleaned_ecg, sampling_rate=360)

# Encontrar los picos R
peaks = nk.ecg_findpeaks(ecg_signals['ECG_Clean'], sampling_rate=360)

# Verificar las claves disponibles en peaks
print("Claves disponibles en peaks:", peaks.keys())

# Usar los picos R para inferir picos P y T (si no se detectan directamente)
r_peaks = peaks['ECG_R_Peaks']
p_peaks = r_peaks - 30  # Aproximación de la posición de P (ajusta según sea necesario)
t_peaks = r_peaks + 30  # Aproximación de la posición de T (ajusta según sea necesario)

# Asegúrate de que no se salgan del rango de la señal
p_peaks = p_peaks[(p_peaks >= 0) & (p_peaks < len(ecg_signals['ECG_Clean']))]
t_peaks = t_peaks[(t_peaks >= 0) & (t_peaks < len(ecg_signals['ECG_Clean']))]

# Ploteo de la señal ECG y los picos
plt.figure(figsize=(12, 6))

# Graficar la señal limpia
plt.plot(ecg_signals['ECG_Clean'], label='ECG Limpio', color='blue')

# Graficar los picos detectados
plt.scatter(r_peaks, ecg_signals['ECG_Clean'][r_peaks], color='red', label='Picos R', zorder=5)
plt.scatter(p_peaks, ecg_signals['ECG_Clean'][p_peaks], color='green', label='Picos P', zorder=5)
plt.scatter(t_peaks, ecg_signals['ECG_Clean'][t_peaks], color='purple', label='Picos T', zorder=5)

# Etiquetas y leyenda
plt.title('Señal ECG y Picos P, QRS, T Detectados')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()
