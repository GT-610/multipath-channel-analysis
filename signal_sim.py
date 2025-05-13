import numpy as np
from utils import save_data, plot_signal
from scipy.signal import convolve
from channel_model import generate_channel

def generate_bpsk_signal(num_bits=100, sps=10):
    """
    生成BPSK调制信号
    num_bits: 二进制比特数
    sps: 每个符号的采样点数
    """
    # 生成随机比特流
    bits = np.random.randint(0, 2, num_bits)
    # BPSK映射（0→-1, 1→1）
    bpsk_symbols = 2 * bits - 1
    # 插入sps-1个零进行升采样（模拟脉冲成形）
    s = np.zeros(num_bits * sps)
    s[::sps] = bpsk_symbols
    save_data(s, "transmitted_signal")
    plot_signal(np.arange(len(s)), s, "Transmitted BPSK Signal")
    return s

def simulate_transmission(s, h, add_noise_flag=False):
    """
    模拟信号传输：r(t) = s(t) * h(t)
    s: 发送信号
    h: 信道冲激响应
    """
    r = convolve(s, h, mode='full')  # 卷积模拟多径传播
    if add_noise_flag:
        r = add_noise(r, snr_dB=10)  # 可选：添加噪声
    save_data(r, "received_signal")
    plot_signal(np.arange(len(r)), r, "Received Signal")
    return r

if __name__ == "__main__":
    s = generate_bpsk_signal()
    h = generate_channel()
    r = simulate_transmission(s, h)