# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
from synth.waveforms import Waveform, Saw, Supersaw
import numpy as np
import sounddevice as sd
import time


frequency = 440 
sample_rate = 44100

osc = Supersaw(frequency,1,1)
waveform = osc.get_waveform(n_waves=5,detune=0.01,blend=0.25)
osc.plot(waveform)

sd.play(waveform,samplerate=sample_rate)



# data = Waveform().saw(w,duration=0.1)
# data = np.float32(data)
# stream = sd.Stream(channels=1)

# while True:
    
#     data = Waveform().saw(w,duration=0.1)
#     data = np.float32(data)
#     stream.write(data)
#     time.sleep(0.01)

