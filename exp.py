import math
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_exponential(lambda_rate, N):
    """
    Generate N samples from Exponential(lambda = lambda_rate),
    using the inverse transform method (or Python’s random.expovariate).
    """
    # Method 1: use random.expovariate
    samples = [random.expovariate(lambda_rate) for _ in range(N)]
    return samples

def compute_stats(samples):
    n = len(samples)
    mean = sum(samples) / n
    ss = sum((x - mean)**2 for x in samples)
    variance = ss / n
    std = math.sqrt(variance)
    return mean, std
def plot_histogram(samples, lambda_rate, bins=30):
    plt.figure(figsize=(8,5))
    # Use density=True so the y-axis is a probability density
    plt.hist(samples, bins=bins, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    # Also overlay the theoretical PDF of Exponential(lambda)
    xs = np.linspace(0, max(samples), 200)
    pdf = lambda_rate * np.exp(-lambda_rate * xs)
    plt.plot(xs, pdf, 'r-', lw=2, label=f"Theoretical PDF (λ={lambda_rate})")
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title(f"Histogram of Exponential(λ = {lambda_rate}), N = {len(samples)}")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
def main():
    lambda_rate = 10.0
    N = 1000

    samples = generate_exponential(lambda_rate, N)
    mean, std = compute_stats(samples)

    print(f"Generated {N} exponential samples (λ = {lambda_rate})")
    print(f"Sample mean = {mean:.6f}")
    print(f"Sample standard deviation = {std:.6f}")


    plot_histogram(samples, lambda_rate, bins=40)

if __name__ == "__main__":
    main()
