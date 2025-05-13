import numpy as np
from utils import save_data, plot_signal

def generate_channel(gains=[0.8, 0.5, 0.3], delays=[0, 2, 5], max_delay=10):
    """
    多径信道建模：h(t) = Σ α_i * δ(t - τ_i)
    gains: 路径增益列表
    delays: 路径时延列表（采样点数）
    max_delay: 最大时延（决定冲激响应长度）
    """
    h = np.zeros(max_delay)
    for gain, delay in zip(gains, delays):
        if delay < max_delay:
            h[delay] += gain
    save_data(h, "channel_impulse")
    plot_signal(np.arange(len(h)), h, "Channel Impulse Response")
    return h

if __name__ == "__main__":
    h = generate_channel()