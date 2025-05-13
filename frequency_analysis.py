from scipy.fft import fft, fftfreq
import numpy as np
from utils import plot_signal

def analyze_frequency(s, r, fs=1e6):
    """
    频域分析：比较发送与接收信号频谱
    s: 发送信号
    r: 接收信号
    fs: 采样率
    """
    S = fft(s)
    R = fft(r)
    f = fftfreq(len(s), d=1/fs)
    plot_signal(f[:len(f)//2], np.abs(S)[:len(f)//2], "Transmitted Signal Spectrum")
    plot_signal(f[:len(f)//2], np.abs(R)[:len(f)//2], "Received Signal Spectrum")

if __name__ == "__main__":
    s = np.load("data/transmitted_signal.npy")
    r = np.load("data/received_signal.npy")
    analyze_frequency(s, r)