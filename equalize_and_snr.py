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
    s = np.load("data/transmitted_signal.npy")
    r = np.load("data/received_signal.npy")
    h = np.load("data/channel_impulse.npy")

    # 修改1：先对齐原始接收信号
    aligned_s, aligned_r = align_signals(s, r)  # 新增接收信号对齐
    
    # 修改2：统一使用改进后的对齐方法
    # equalized = match_filter(r, h)
    equalized = deconvolution(r, h)  # 改用逆卷积法
    
    # 对齐信号
    aligned_s, aligned_equalized = align_signals(s, equalized, h)

    # 保存均衡后信号
    np.save("data/equalized_signal.npy", equalized)
    # 绘制均衡前后对比图
    plot_signal(np.arange(len(equalized)), equalized, "Equalized Signal")

    # 计算SNR
    noise_before = aligned_r - aligned_s  # 使用对齐后的接收信号
    noise_after = aligned_equalized - aligned_s
    
    # 新增：验证信号对齐效果
    print(f"Alignment check - Before length: {len(aligned_r)}, After length: {len(aligned_equalized)}")
    
    snr_before = calculate_snr(aligned_s, noise_before)
    snr_after = calculate_snr(aligned_s, noise_after)
    print(f"Noise before equalization: {10 * np.log10(np.var(noise_before)):.2f} dB")
    print(f"Noise after equalization: {10 * np.log10(np.var(noise_after)):.2f} dB")
    print(f"SNR Before: {snr_before:.2f} dB, After: {snr_after:.2f} dB")