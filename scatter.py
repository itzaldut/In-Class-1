import matplotlib.pyplot as plt
import random

def scatter_using_python_random(N=1000):
    """Generate N points (x,y) by Python’s random.random() and scatter them."""
    xs = [random.random() for _ in range(N)]
    ys = [random.random() for _ in range(N)]
    plt.figure(figsize=(6,6))
    plt.scatter(xs, ys, s=5, alpha=0.5)
    plt.title(f"Scatter of {N} uniform random (0,1) pairs — Python random")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("square")
    plt.show()

def main():
    N = 5000  # you can increase this (e.g. 10000 or 100000), but for visualization smaller is fine
    scatter_using_python_random(N)

if __name__ == "__main__":
    main()


