import numpy as np
from equalizer import match_filter, deconvolution, align_signals
from utils import plot_signal
from scipy.stats import norm

def calculate_snr(signal, noise):
    """计算信噪比（SNR）"""
    signal_power = np.var(signal)
    noise_power = np.var(noise)
    return 10 * np.log10(signal_power / noise_power)


if __name__ == "__main__":
    # 加载数据
    s = np.load("data/transmitted_signal.npy")  # 原始发送信号
    r = np.load("data/received_signal.npy")      # 接收信号
    h = np.load("data/channel_impulse.npy")      # 信道冲激响应

    # 均衡信号
    # equalized = match_filter(r, h) # 匹配滤波
    equalized = deconvolution(r, h) # 逆卷积
    # 对齐信号
    aligned_s, aligned_equalized = align_signals(s, equalized, h)

    # 保存均衡后信号
    np.save("data/equalized_signal.npy", equalized)
    # 绘制均衡前后对比图
    plot_signal(np.arange(len(equalized)), equalized, "Equalized Signal")

    # 计算SNR
    noise_before = r[:len(aligned_s)] - aligned_s  # 接收信号与原始信号的差值
    noise_after = aligned_equalized - aligned_s    # 均衡后信号与原始信号的差值
    snr_before = calculate_snr(aligned_s, noise_before)
    snr_after = calculate_snr(aligned_s, noise_after)
    print(f"Noise before equalization: {10 * np.log10(np.var(noise_before)):.2f} dB")
    print(f"Noise after equalization: {10 * np.log10(np.var(noise_after)):.2f} dB")
    print(f"SNR Before: {snr_before:.2f} dB, After: {snr_after:.2f} dB")