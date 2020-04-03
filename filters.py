
"""
Created on Fri Jan  3 17:38:54 2020

@author: lorenzo
"""
from scipy import signal


class Filters:
    
    def __init__(self,waveform,cutoff,sampling_rate=44100): #remember to add resonance
        
        self.waveform = waveform
        self.cutoff = cutoff
        self.sampling_rate = sampling_rate
    
    def lowpass(self):
        
        nyq = 0.5 * self.sampling_rate
        N  = 6    # Filter order
        fc = self.cutoff / nyq # Cutoff frequency normal
        b, a = signal.butter(N, fc)
        
        #Apply the filter
        waveform = signal.filtfilt(b,a,self.waveform)
        
        return waveform
