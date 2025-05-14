import numpy as np
from scipy.signal import convolve
from scipy.fft import fft, ifft

def match_filter(r, h):
    """
    匹配滤波器设计：h_match(t) = h*(-t)
    r: 接收信号
    h: 信道冲激响应
    """
    h_match = np.conj(h[::-1])  # 匹配滤波器冲激响应
    equalized = convolve(r, h_match, mode='same')
    return equalized


def deconvolution(r, h, epsilon=1e-3):
    R = fft(r)
    H = fft(h, n=len(r))  # 扩展h长度与r一致
    S_recover = R / (H + epsilon)  # 频域除法
    return np.real(ifft(S_recover))  # 逆FFT恢复时域信号

def align_signals(s, equalized, h):
    """
    对齐均衡后信号与原始发送信号
    s: 发送信号
    equalized: 均衡后信号
    h: 信道冲激响应
    """
    delay = len(h) // 2  # 匹配滤波器的固定延迟
    aligned_equalized = equalized[delay:delay + len(s)]  # 截取有效信号段
    aligned_s = s[:len(aligned_equalized)]  # 截取等长的发送信号
    return aligned_s, aligned_equalized