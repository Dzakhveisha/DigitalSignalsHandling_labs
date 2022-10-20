from matplotlib import pyplot as plt
import numpy as np

A = 6
fArray=[1,2,3,4,5]
fiArray = [np.pi/6, np.pi/2, np.pi/3, np.pi/9, 0]
N = 1024
n = np.linspace(0, N-1)

def plot_task_3():
    for f in fArray:
        y=0;
        for fi in fiArray:
            y += A * np.sin(2 * np.pi * f * n/N + fi)
        plt.plot(n, y)
    plt.legend(fArray, loc='upper right')
    plt.show()


if __name__ == "__main__":
    plot_task_3()