import numpy as np
from utils import save_data, plot_signal

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

if __name__ == "__main__":
    s = generate_bpsk_signal()