import numpy as np
import matplotlib.pyplot as plt
import os  # 已导入os模块

def save_data(data, filename):
    """保存数据到data目录"""
    # 检查并创建目标目录
    target_dir = "data"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    np.save(f"{target_dir}/{filename}.npy", data)

def plot_signal(t, s, title, xlabel="Time", ylabel="Amplitude"):
    """绘制信号波形图"""
    # 新增：检查并创建目标目录
    target_dir = "figures"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, s)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f"{target_dir}/{title.replace(' ', '_')}.png")
    plt.close()

def add_noise(signal, snr_dB):
    """添加高斯白噪声（可选功能）"""
    noise = np.random.randn(*signal.shape) * 10**(-snr_dB/20)
    return signal + noise