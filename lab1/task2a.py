from matplotlib import pyplot as plt
import numpy as np

A = 6
f= 3
fiArray = [2 * np.pi, np.pi/6, np.pi/2, 0, 3 * np.pi/4]
N = 1024
n = np.linspace(0, N-1)

def plot_task_2a():
    for fi in fiArray:
        y = A * np.sin(2 * np.pi * f * n/N + fi)
        plt.plot(n, y)
    plt.legend(fiArray, loc='upper right')
    plt.show()

if __name__ == "__main__":
    plot_task_2a()