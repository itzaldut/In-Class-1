import numpy as np
import matplotlib.pyplot as plt

def generate_correlated_normals(rho, N=10000):
    """Generate N pairs of correlated normal random variables."""
    mean = [0, 0]
    cov = [[1, rho], [rho, 4]]  # Variances: 1 and 4 (std devs: 1 and 2)
    samples = np.random.multivariate_normal(mean, cov, size=N)
    return samples[:, 0], samples[:, 1]

def plot_heatmap(x, y, ax,fig, title):
    """Plot a heatmap of the bivariate distribution."""
    hb = ax.hexbin(x, y, gridsize=50, cmap='cividis')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.axis('equal')
    ax.legend()
    cbar = fig.colorbar(hb, ax=ax)
    cbar.set_label('Counts')

def main():
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))

    correlations = [0.5, 0, 1, -1]
    for ax, rho in zip(axs.ravel(), correlations):
        x, y = generate_correlated_normals(rho)
        plot_heatmap(x, y, ax, fig, f'Correlation ρ = {rho}')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

