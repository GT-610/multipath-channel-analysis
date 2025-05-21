import numpy as np
from equalizer import match_filter, deconvolution, align_signals
from utils import plot_signal
from scipy.stats import norm

def calculate_snr(signal, noise):
    """Calculate Signal-to-Noise Ratio (SNR)"""
    signal_power = np.var(signal)
    noise_power = np.var(noise)
    return 10 * np.log10(signal_power / noise_power)

if __name__ == "__main__":
    # Load data
    s = np.load("data/transmitted_signal.npy")
    r = np.load("data/received_signal.npy")
    h = np.load("data/channel_impulse.npy")

    aligned_s, aligned_r = align_signals(s, r)  # New signal alignment
    
    # equalized = match_filter(r, h)
    equalized = deconvolution(r, h)  # Use inverse convolution method
    
    # Align signals
    aligned_s, aligned_equalized = align_signals(s, equalized, h)

    # Save equalized signal
    np.save("data/equalized_signal.npy", equalized)
    # Plot comparison before/after equalization
    plot_signal(np.arange(len(equalized)), equalized, "Equalized Signal")

    # Calculate SNR
    noise_before = aligned_r - aligned_s  # Using aligned received signal
    noise_after = aligned_equalized - aligned_s
    
    # Validate signal alignment effectiveness
    print(f"Alignment check - Before length: {len(aligned_r)}, After length: {len(aligned_equalized)}")
    
    snr_before = calculate_snr(aligned_s, noise_before)
    snr_after = calculate_snr(aligned_s, noise_after)
    print(f"Noise before equalization: {10 * np.log10(np.var(noise_before)):.2f} dB")
    print(f"Noise after equalization: {10 * np.log10(np.var(noise_after)):.2f} dB")
    print(f"SNR Before: {snr_before:.2f} dB, After: {snr_after:.2f} dB")