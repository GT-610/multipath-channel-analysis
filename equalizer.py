import numpy as np
from scipy.signal import convolve

def match_filter(r, h):
    """
    匹配滤波器设计：h_match(t) = h*(-t)
    r: 接收信号
    h: 信道冲激响应
    """
    h_match = np.conj(h[::-1])  # 匹配滤波器冲激响应
    equalized = convolve(r, h_match, mode='same')
    return equalized

if __name__ == "__main__":
    r = np.load("data/received_signal.npy")
    h = np.load("data/channel_impulse.npy")
    equalized = match_filter(r, h)
    # 计算SNR改善（简化版）
    snr_before = np.var(r) / np.var(r - s[:len(r)])  # 假设s已截取
    snr_after = np.var(equalized) / np.var(equalized - s[:len(equalized)])
    print(f"SNR Before: {snr_before:.2f} dB, After: {snr_after:.2f} dB")