
import numpy as np


class Waveform:
    
    def __init__(self,sampling_rate=44100):
        
        self.sampling_rate = sampling_rate
        #self.frequency = frequency
        
#    def plot()
        

    def noise(self,amplitude=1, duration=1):
        
        waveform = np.random.rand(self.sampling_rate*duration)
        waveform = amplitude*waveform
        
        return waveform


    def saw(self, frequency, k_max=100, amplitude=1, duration=1):
        
        time_array = np.arange(self.sampling_rate*duration)
        waveform = np.zeros(len(time_array))
        
        for k in range(1,k_max):
            
            series_element = (((-1)**k)/k) * np.sin(2*np.pi*(time_array/self.sampling_rate)*frequency * k )
            waveform = np.add(waveform,series_element)
        
        waveform = 2*amplitude/np.pi * waveform
            
        return waveform 

       
    def sine(self, frequency, amplitude=1, duration=1):
 
        time_array = np.arange(self.sampling_rate*duration)
        
        waveform = amplitude*np.sin(2*np.pi*(time_array/self.sampling_rate)* frequency)       
        
        return waveform
        
 
    def square(self,frequency, k_max=100,amplitude=1, duration=1):
        
        time_array = np.arange(self.sampling_rate*duration)
        waveform = np.zeros(len(time_array))
        
        for k in range(1,k_max*2,2):
            
            series_element = (1/k) * np.sin(2*np.pi*(time_array/self.sampling_rate)*frequency * k)
            waveform = np.add(waveform,series_element)
                
        waveform = 4*amplitude/np.pi * waveform
            
        return waveform    
    
    
    def supersaw(self, frequency, n_waves=5, detune=0.01, blend=0.25, amplitude=1, duration=1):
       
        waveform = self.saw(frequency,k_max=100,amplitude=amplitude,duration=duration)
        delta_frequency = int(detune*frequency)
        
        for i in range(-1*delta_frequency,delta_frequency):
            saw_wave = self.saw(frequency= frequency + i ,k_max=100,amplitude=amplitude*blend,duration=duration)
            waveform = np.add(waveform,saw_wave)
               
        return waveform
    
    
    def triangle(self,frequency, k_max=100,amplitude=1, duration=1):
        
        time_array = np.arange(self.sampling_rate*duration)
        waveform = np.zeros(len(time_array))
        
        for k in range(1,k_max*2,2):
            
            series_element = (((-1)**((k-1)/2))/(k**2)) * np.sin(2*np.pi*(time_array/self.sampling_rate)*frequency * k)
            waveform = np.add(waveform,series_element)
                
        waveform = 8*amplitude/np.pi**2 * waveform
            
        return waveform    

#class Saw(Waveforms)
        
    
        