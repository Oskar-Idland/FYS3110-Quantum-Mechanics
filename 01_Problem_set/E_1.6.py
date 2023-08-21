import numpy as np
import matplotlib.pyplot as plt
π = np.pi
ϵ = [1, 0.1, 0.01]

def δ(x, ϵ):
    return 1/π * ϵ/(ϵ**2 + x**2)

for n in ϵ:
    x = np.linspace(-1, 1, 1001)
    plt.plot(x, δ(x, n), label=f"ϵ={n}")
    plt.legend()

plt.title("Problem 1.6 c)")
plt.savefig("E_1.6.pdf")
plt.show()