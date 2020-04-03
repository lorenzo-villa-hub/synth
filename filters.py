#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:38:54 2020

@author: lorenzo
"""
from scipy import signal


class Filters:
    
    def lowpass(wave,cutoff,sampling_rate = 44100):
        
        nyq = 0.5 * sampling_rate
        N  = 6    # Filter order
        fc = cutoff / nyq # Cutoff frequency normal
        b, a = signal.butter(N, fc)
        
        #Apply the filter
        wave = signal.filtfilt(b,a,wave)
        
        return wave