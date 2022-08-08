#Carregando um arquivo de áudio usando a biblioteca Librosa

import librosa                   # Processamento de áudio
import librosa.display           # Plot de gráficos
import matplotlib.pyplot as plt  # Plot de gráficos

import IPython  # Para tocar o áudio no Jupyter

sinal, sr = librosa.load('dados_topico1/aeiou_ruido.wav', sr=44100) # Carregando

type(sinal) # O librosa usa o numpy para guardar o sinal de áudio

sinal # O sinal é um array numpy de uma dimensão onde cada valor é um float de 32 bits

sinal[0] # Sinal é normalizado para ficar entre -1 a 1

sinal[1]

len(sinal)

len(sinal)/44100

max(sinal), min(sinal)

len(sinal)/sr # Logo o tempo total do áudio é de 4.7 segundos aproximadamente

librosa.display.waveshow(sinal, sr=sr,color='r')
plt.grid(color='k', linestyle='-', linewidth=0.3)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Amplitude (a.u.)', fontsize=14)

#Arquivos no formato WAV são os mais fáceis de entender pois não possuem compressão. 
# Já mp3 e .opus (.ogg) possuem compressão cuja especificação precisa ser estudada.
#Uma propriedade física bem comum no áudio é a frequência do som.
#Para ver isso, vamos plotar um gráfico diferente chamado de Espectrograma

import numpy as np

D = librosa.amplitude_to_db(np.abs(librosa.stft(sinal)), ref=np.max)
librosa.display.specshow(D, y_axis='log',x_axis='time')

plt.colorbar(format='%+2.0f dB')
plt.xlabel('Tempo (s)', fontsize=14)
plt.ylabel('Frequência (Hz)', fontsize=14)

0.55*44100

sinal2 = sinal.copy()
for i in range(0,24255):
    sinal2[i] = 0

type(sinal2)

librosa.display.waveshow(sinal2, sr=sr,color='b')
plt.grid(color='k', linestyle='-', linewidth=0.3)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Amplitude (a.u.)', fontsize=14)

import soundfile as sf

sf.write('dados_topico1/aeiou2.wav', sinal2, samplerate=44100, format='wav')

IPython.display.Audio('dados_topico1/aeiou2.wav')
