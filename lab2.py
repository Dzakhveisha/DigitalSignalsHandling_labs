import  numpy as np
import matplotlib.pyplot as plt


def harmonic(N, M, fi):
    ns = np.arange(0, M)
    return np.sin((2 * np.pi * ns) / N + fi)


def plot_task_2(N, fi):
    signals = {}
    K = 3 * N / 4
    ms1 = list(np.arange(start=K+1, stop=2*N + 1, step=N // 20))
    if N - 1 not in ms1:
        ms1.append(N-1)
    if 2*N not in ms1:
        ms1.append(2*N)
    for M in sorted(ms1):
        signals[int(M)] = harmonic(N, M, fi)
    plt.plot(np.arange(0, N-1), signals[N-1], label=f'M = {N - 1}',)
    plt.title(f'Сигналы при N={N}')
    plt.legend(loc='lower right')
    plt.show()
    return signals


def plot_task_2a(signals):
    print('СКЗ по формуле а):')
    residuals = []
    for M, signal in signals.items():
        mean = mean1(signal, M)
        #print(f'При M = {M} СКЗ = {mean}')
        residuals.append(0.707 - mean)
    plt.plot(signals.keys(), residuals)
    plt.title('Погрешность вычисления СКЗ по формуле а) при различных М')
    plt.show()


def plot_task_2b(signals):
    print('СКЗ по формуле б):')
    residuals = []
    for M, signal in signals.items():
        mean = mean2(signal, M)
        #print(f'При M = {M} СКЗ = {mean}')
        residuals.append(0.707 - mean)
    plt.plot(signals.keys(), residuals)
    plt.title('Погрешность вычисления СКЗ по формуле б) при различных М')
    plt.show()


def mean1(signal, M):
    return np.sqrt((signal ** 2).sum() / (M + 1))


def mean2(signal, M):
    return np.sqrt(
        (signal ** 2).sum() / (M + 1) - (signal.sum() / (M + 1)) ** 2
    )


def DFT(signals):
    As = []
    residuals = []
    for M, signal in signals.items():
        if M < N:
            n = np.arange(M)
            cos_ = np.cos(2*np.pi*n/M).reshape(-1, 1)
            sin_ = np.sin(2*np.pi*n/M).reshape(-1, 1)
            A_cos = (signal @ cos_) * 2 / M
            A_sin = (signal @ sin_) * 2 / M
            A = np.sqrt(A_sin**2 + A_cos**2)
            As.append(A)
            residuals.append(1 - A)
    plt.plot(list(signals.keys())[:len(residuals)], residuals)
    plt.title('Погрешность вычисления амплитуды при различных М')
    plt.show()


fi1 = 0
fi2 = np.pi / 8
N = 4096


if __name__ == '__main__':
    signals = plot_task_2(N, fi1)
    plot_task_2a(signals)
    plot_task_2b(signals)
    DFT(signals)

    signals = plot_task_2(N, fi2)
    plot_task_2a(signals)
    plot_task_2b(signals)
    DFT(signals)



