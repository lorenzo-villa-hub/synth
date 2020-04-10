# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
from vibra.waveforms import Waveform, Saw, Supersaw, Sine
from vibra.filters import Lowpass, Bandpass, Highpass
import numpy as np
import sounddevice as sd
import time
from scipy import signal
import matplotlib.pyplot as plt


frequency = 200
samplerate = 44100

osc = Saw(frequency,1,1)
waveform = osc.get_waveform()
osc.plot(waveform,label='raw')

filt = Highpass(cutoff=500,slope='24')
waveform = filt.apply_filter(waveform)
filt.plot()
osc.plot(waveform,label='filtered')

sd.play(waveform,samplerate=samplerate)



# data = Waveform().saw(w,duration=0.1)
# data = np.float32(data)
# stream = sd.Stream(channels=1)

# while True:
    
#     data = Waveform().saw(w,duration=0.1)
#     data = np.float32(data)
#     stream.write(data)
#     time.sleep(0.01)

