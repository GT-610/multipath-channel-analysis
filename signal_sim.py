import numpy as np
from utils import save_data, plot_signal
from scipy.signal import convolve
from channel_model import generate_channel

def generate_bpsk_signal(num_bits=100, sps=10):
    """
    Generate BPSK modulated signal
    num_bits: Number of binary bits
    sps: Samples per symbol
    """
    # Generate random bit stream
    bits = np.random.randint(0, 2, num_bits)
    # BPSK mapping (0→-1, 1→1)
    bpsk_symbols = 2 * bits - 1
    # Insert sps-1 zeros for upsampling (pulse shaping simulation)
    s = np.zeros(num_bits * sps)
    s[::sps] = bpsk_symbols
    save_data(s, "transmitted_signal")
    plot_signal(np.arange(len(s)), s, "Transmitted BPSK Signal")
    return s

def simulate_transmission(s, h, add_noise_flag=False):
    """
    Simulate signal transmission: r(t) = s(t) * h(t)
    s: Transmitted signal
    h: Channel impulse response
    """
    r = convolve(s, h, mode='full')  # Convolution to simulate multipath propagation
    if add_noise_flag:
        r = add_noise(r, snr_dB=10)  # Optional: Add noise
    save_data(r, "received_signal")
    plot_signal(np.arange(len(r)), r, "Received Signal")
    return r

if __name__ == "__main__":
    s = generate_bpsk_signal()
    h = generate_channel()
    r = simulate_transmission(s, h)