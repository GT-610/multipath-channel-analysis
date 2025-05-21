import numpy as np
from scipy.signal import convolve
from scipy.fft import fft, ifft

def match_filter(r, h):
    """
    Match filter design: h_match(t) = h*(-t)
    r: Received signal
    h: Channel impulse response
    """
    h_match = np.conj(h[::-1])  # Match filter impulse response
    equalized = convolve(r, h_match, mode='same')
    return equalized


def deconvolution(r, h, epsilon=1e-3):
    R = fft(r)
    H = fft(h, n=len(r))  # Extend h length to match r
    S_recover = R / (H + epsilon)  # Frequency domain division
    return np.real(ifft(S_recover))  # Inverse FFT to recover time domain signal

def align_signals(s, equalized, h=None):
    """
    Use cross-correlation to find the optimal delay for alignment
    """
    # Calculate cross-correlation to find the best alignment position
    corr = np.correlate(equalized, s, mode='valid')
    delay = np.argmax(corr)
    
    # Ensure the cropped length does not exceed the signal length
    valid_length = min(len(s), len(equalized) - delay)
    aligned_equalized = equalized[delay:delay+valid_length]
    aligned_s = s[:valid_length]
    return aligned_s, aligned_equalized