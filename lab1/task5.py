import matplotlib.pyplot as plt
import numpy as np

PI = np.pi

def harmonic_period(A, f, N, fi, period):
    ns = np.arange(0, N-1)
    coef = np.linspace(0, 0.5 * period, N - 1)
    a_i = A + (A * coef)
    f_i = f + (f * coef)
    fi_i = fi + (fi * coef)
    return a_i * np.sin((2 * np.pi * f_i * ns) / N + fi_i)

def polyharmoic_increasing(AArr, fArr, N, fiArr, period):
    y = [harmonic_period(AArr[i], fArr[i], N, fiArr[i], period) for i in range(0, len(fArr))]
    return np.sum(y, axis=0)


A = 10
f = 2
N = 10000
fi1 = 0
fi2 = np.pi / 6
fi3 = np.pi / 4
fi4 = np.pi / 2
fi5 = np.pi

#AArr = [1, 1, 1, 1, 1]
AArr = [9,9,9,9,9]
fArr = [1, 2, 3, 4, 5]
#fiArr = [fi1, fi2, fi3, fi4, fi5]
fiArr = [PI/2, 0, PI/4, PI/3, PI/6]


def plot_task_4():
    plt.plot(range(0, N - 1), polyharmoic_increasing(AArr, fArr, N, fiArr, 10))
    plt.show()


if __name__ == "__main__":
    plot_task_4()