import numpy as np
from scipy.io import wavfile as wav


#start by getting the sampling rate and the audio data (samples values) from the audio file using scipy library  : 
sr, y = wav.read("sound.wav")
#sr : contains the sampling rate which is the number of samples (amplitude value in a specific time) per second in pur audio file the sr is 44100 samples/second 
duration = 1
# duration is equal to 1 bc we are going to extract the frequency of each 1 sec  
chunk = int(sr * duration)
# chunk or a segment of data from the audio data calculated by (sampling rate * duration )= 44100 
chars = int(len(y) / chunk)
# deducing the number of chars means the (flag length) by dividing len(y)/chunk =37 char 
# len(y)/(sampling rate)="audio time" as we have each 1 sec represent 1 freq which is a special char so we found that : duration = number of flag chars 

def get_freq(char):
    # starting audio data index 
    start = chunk * char
    #ending audio data index
    end = start + chunk
    #slicing it from the whol audio signal data
    sliced = y[start:end]
    # here np.fft.fft stands for fast fourier transform is a famous algorithm that used to transform a sequence of (time domain signal values) to frequency doamin signal means we are going to do a transition from amplitude values over time y(t) to amplitude values over frenquency y(freq)  
    w = np.fft.fft(sliced) #each element of w is a complex number exp : 1+0.0002j :=> 1 is the amplitude of the signal and the 0.0002 is the phase at a specific frequency 
    #purpose is the identify the 'dominant' frequency in a specific part of the signal which is our goal (flag chars)
    freqs = np.fft.fftfreq(len(w)) #to get the freq of each frequency bins (F(freq bin)=1+0.003j)
    idx = np.argmax(np.abs(w))# return  the index of dominated frequency in this audio segment exp : 485hz
    freq = freqs[idx]
    freq_in_hertz = abs(freq * sr)
    return freq_in_hertz

# just casting the type from floting nums freq to int and then substract the starting freq A 440 from each value to get the char code 
decoded_freqs = []
for char in range(chars):
    decoded_freqs.append(get_freq(char))
freqs_casted = np.array(decoded_freqs)
freqs = freqs_casted.astype(int)
flag = ""
for i in range(len(freqs)):
    freqs[i] = freqs[i] - 440
    flag = flag + chr(freqs[i])
print(flag)
