import numpy as np
from utils import save_data, plot_signal

def generate_channel(gains=[0.8, 0.5, 0.3], delays=[0, 2, 5], max_delay=10):
    """
    Multipath channel modeling: h(t) = Σ α_i * δ(t - τ_i)
    gains: Path gain coefficients list
    delays: Path delay values in sampling points
    max_delay: Maximum delay (determines impulse response length)
    """
    h = np.zeros(max_delay)
    # Apply gains at specified delays within channel response window
    for gain, delay in zip(gains, delays):
        if delay < max_delay:
            h[delay] += gain
    save_data(h, "channel_impulse")
    plot_signal(np.arange(len(h)), h, "Channel Impulse Response")
    return h

if __name__ == "__main__":
    h = generate_channel()