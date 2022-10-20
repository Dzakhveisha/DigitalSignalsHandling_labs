from matplotlib import pyplot as plt
import numpy as np

ArrayA = [2,4,8,3,1]
f=5
fi = np.pi/4
N = 1024
n = np.linspace(0, N-1)

def plot_task_2v():
    for A in ArrayA:
        y = A * np.sin(2 * np.pi * f * n/N + fi)
        plt.plot(n, y)
    plt.legend(ArrayA, loc='upper right')
    plt.show()

if __name__ == "__main__":
    plot_task_2v()