import numpy as np
import matplotlib.pyplot as plt

def save_data(data, filename):
    """保存数据到data目录"""
    np.save(f"data/{filename}.npy", data)

def plot_signal(t, s, title, xlabel="Time", ylabel="Amplitude"):
    """绘制信号波形图"""
    plt.figure(figsize=(10, 4))
    plt.plot(t, s)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f"figures/{title.replace(' ', '_')}.png")
    plt.close()

def add_noise(signal, snr_dB):
    """添加高斯白噪声（可选功能）"""
    noise = np.random.randn(*signal.shape) * 10**(-snr_dB/20)
    return signal + noise