import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

simpling_rate = 44100
fake_flag = [102 ,97 ,107 ,101 ,95 ,102 ,108 ,97 ,103]
duration = len(fake_flag) #one sec foreach 
frequences = [(num + 440) for num in fake_flag] # initial freq : A 440 
time = np.linspace(0, duration, int(simpling_rate * duration), endpoint=False)
print(len(time))
x = -1
audio_data = []
for i in range(duration):
    for j in range(simpling_rate):
        x = x + 1
        audio_data.append(np.sin(2 * np.pi * frequences[i] * time[x]))
audio_data = np.int16(np.array(audio_data) * 32767)
write("sound.wav", simpling_rate, audio_data)
