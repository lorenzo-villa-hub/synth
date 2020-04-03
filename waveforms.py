
import numpy as np
import matplotlib.pyplot as plt


class Waveform:
    
    def __init__(self,frequency,amplitude,duration,sampling_rate=44100):
        
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.time_array = np.arange(self.sampling_rate*self.duration)
        
    def plot(self,waveform):
        
        x = self.time_array
        y = waveform
        plt.plot(x,y)
        plt.xlim(0,200)
        
        return plt
        
              


class Noise(Waveform):

    def get_waveform(self):
        
        waveform = np.random.rand(self.sampling_rate*self.duration)
        waveform = self.amplitude*waveform                
        return waveform


class Saw(Waveform):
        
    def get_waveform(self, k_max=100):
                
        waveform = np.zeros(len(self.time_array))       
        for k in range(1,k_max):           
            series_element = (((-1)**k)/k) * np.sin(2*np.pi*(self.time_array/self.sampling_rate)*self.frequency * k )
            waveform = np.add(waveform,series_element)
        
        waveform = 2*self.amplitude/np.pi * waveform            
        return waveform 
        

class Sine(Waveform):
    
    def get_waveform(self):
         
        waveform = self.amplitude*np.sin(2*np.pi*(self.time_array/self.sampling_rate)* self.frequency)               
        return waveform
    
    
class Square(Waveform):

    def get_waveform(self,k_max=100):
        
        waveform = np.zeros(len(self.time_array))
        
        for k in range(1,k_max*2,2):            
            series_element = (1/k) * np.sin(2*np.pi*(self.time_array/self.sampling_rate)*self.frequency * k)
            waveform = np.add(waveform,series_element)
                
        waveform = 4*self.amplitude/np.pi * waveform           
        return waveform      
    
        
class Supersaw(Waveform):
    
    def get_waveform(self, n_waves=5, detune=0.01, blend=0.25):
       
        # there must be a better way of doing this
        saw = Saw(self.frequency,self.amplitude,self.duration)

        waveform = saw.get_waveform(k_max=100)
        delta_frequency = int(detune*self.frequency)
        if n_waves != 1:           
            interval = 2*delta_frequency/(n_waves -1)            
            for i in np.arange(-1*delta_frequency,delta_frequency,interval):
                saw.frequency =  saw.frequency + i
                saw.amplitude = saw.amplitude*blend
                saw_wave = saw.get_waveform(k_max=100)
                waveform = np.add(waveform,saw_wave)
               
        return waveform
    

class Triangle(Waveform):

    def get_waveform(self,k_max=100):
        
        waveform = np.zeros(len(self.time_array))        
        for k in range(1,k_max*2,2):            
            series_element = (((-1)**((k-1)/2))/(k**2)) * np.sin(2*np.pi*(self.time_array/self.sampling_rate)*self.frequency * k)
            waveform = np.add(waveform,series_element)
                
        waveform = 8*self.amplitude/np.pi**2 * waveform            
        return waveform        