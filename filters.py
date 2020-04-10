
"""
Created on Fri Jan  3 17:38:54 2020

@author: lorenzo
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class Filters:
    
    def __init__(self,cutoff,slope='12',sampling_rate=44100): #remember to add resonance and analog/digital mode
        """
        Abstract class for handling filters

        Parameters
        ----------
        cutoff : (float)
            Cutoff frequency.
        slope : (string)
            Slope of the filter. Options are '12' (12 dB/oct) or '24' (24 dB/oct)
        sampling_rate : (int), optional
            Sampling rate in Hz. The default is 44100.
        """        
        self.cutoff = cutoff
        self.slope = slope
        self.sampling_rate = sampling_rate
        
    
    def plot(self):
        plt.figure()
        """
        Plot filter frequency response

        Returns
        -------
        plt : (Matplotlib object)
        """
        b,a = self.pol_num, self.pol_den
        w, h = signal.freqz(b, a)
        w = w/(2*np.pi)*self.sampling_rate
        plt.semilogx(w, 20 * np.log10(abs(h)))
        
        plt.ylim(-30,10)
        plt.ylabel('Amplitude [dB]')
        plt.xlabel('Frequency [Hz]')
        plt.title('Filter frequency response')
        plt.grid(which='both', linestyle='-', color='grey')
        plt.xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000], 
                   ["20", "50", "100", "200", "500", "1K", "2K", "5K", "10K", "20K"])
        
        return plt
    
    
class Lowpass(Filters):
    
    """Class for applying a lowpass filter"""
        
    def apply_filter(self,waveform):
        """
        Apply filter to a signal

        Parameters
        ----------
        waveform : (Numpy array)
            Signal to apply filter to.

        Returns
        -------
        waveform : (Numpy array)
            Filtered signal.
        """        
        b,a = self.get_filter()
        #Apply the filter
        waveform = signal.filtfilt(b,a,waveform)        
        return waveform
        
    
    def get_filter(self):
        """
        Get numerator (b) and denominator (a) polynomials of the IIR filter.
        """        
        nyq = 0.5 * self.sampling_rate
        if self.slope == '12':
            N = 2 # Filter order
        if self.slope == '24':
            N = 3  
        fc = self.cutoff / nyq # Cutoff frequency normal
        b, a = signal.butter(N, fc,btype='low')
        self.pol_num = b
        self.pol_den = a
        return b,a
    

class Highpass(Filters):
    
    """Class for applying a highpass filter"""
        
    def apply_filter(self,waveform):
        """
        Apply filter to a signal

        Parameters
        ----------
        waveform : (Numpy array)
            Signal to apply filter to.

        Returns
        -------
        waveform : (Numpy array)
            Filtered signal.
        """    
        b,a = self.get_filter()
        #Apply the filter
        waveform = signal.filtfilt(b,a,waveform)        
        return waveform
            
    def get_filter(self):
        """
        Get numerator (b) and denominator (a) polynomials of the IIR filter.
        """        
        nyq = 0.5 * self.sampling_rate
        if self.slope == '12':
            N = 2 # Filter order
        if self.slope == '24':
            N = 3 
        fc = self.cutoff / nyq # Cutoff frequency normal
        b, a = signal.butter(N, fc,btype='high')
        self.pol_num = b
        self.pol_den = a
        return b,a

    
class Bandpass(Filters):
    
    """Class for applying a bandpass filter"""
            
    def apply_filter(self,waveform,Q=1):
        """
        Apply filter to a signal

        Parameters
        ----------
        waveform : (Numpy array)
            Signal to apply filter to.
        Q : (int)
            Widht of peak filter

        Returns
        -------
        waveform : (Numpy array)
            Filtered signal.
        """        
        b,a = self.get_filter(Q=Q)
        waveform = signal.filtfilt(b, a, waveform)
        return waveform
    
    def get_filter(self,Q=1):
        """
        Get numerator (b) and denominator (a) polynomials of the IIR filter.
        """
        # max and min bandwidth
        if Q < 0.1:
            Q = 0.1
        if Q > 10:
            Q = 10
        nyq = 0.5 * self.sampling_rate
        fc = self.cutoff/nyq
        b,a = signal.iirpeak(fc,Q)
        self.pol_num = b
        self.pol_den = a
        return b, a
    
