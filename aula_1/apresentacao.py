import numpy as np
import matplotlib.pyplot as plt
import apresentacao2 as pds

def main():
    n = np.arange(31)
    w0 = np.pi / 10
    x = np.cos(w0 * n)
    plt.figure()
    plt.stem(n, pds.delta(n))
    plt.show()

if __name__ == "__main__":
    main()