from matplotlib import pyplot as plt
import numpy as np

A = 8
fArray= [2,4,3,7,5]
fi = np.pi/4
N = 512
n = np.linspace(0, N-1)


def plot_task_2b():
    plt.figure(figsize=(13,5))

    for f in fArray:
        y = A * np.sin(2 * np.pi * f * n/N + fi)
        plt.plot(n, y)
    plt.legend(fArray, loc='upper right')
    plt.show()

if __name__ == "__main__":
    plot_task_2b()