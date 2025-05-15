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

def align_signals(s, equalized, h=None):
    """
    改进后的信号对齐方法，使用互相关寻找最佳延迟
    """
    # 计算互相关寻找最佳对齐位置
    corr = np.correlate(equalized, s, mode='valid')
    delay = np.argmax(corr)
    
    # 确保截取长度不超过信号长度
    valid_length = min(len(s), len(equalized) - delay)
    aligned_equalized = equalized[delay:delay+valid_length]
    aligned_s = s[:valid_length]
    return aligned_s, aligned_equalized
