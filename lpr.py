import math

class LCG:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next_int(self):
        """Return the next integer in [0, m)."""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self):
        """Return next number in [0,1) by dividing by m."""
        return self.next_int() / self.m


def compute_stats(samples):
    n = len(samples)
    mean = sum(samples) / n
    # compute central moments etc.
    m2 = sum((x - mean)**2 for x in samples) / n
    m3 = sum((x - mean)**3 for x in samples) / n
    m4 = sum((x - mean)**4 for x in samples) / n
    std = math.sqrt(m2)
    return mean, std, m2, m3, m4


def run_raw_ints():
    # parameters — choose “good” LCG constants
    # e.g. from Numerical Recipes (32-bit):
    #   m = 2**31, a = 1103515245, c = 12345
    seed = 123456789
    a = 1103515245
    c = 12345
    m = 2**31

    rng = LCG(seed, a, c, m)
    N = 1_000_000
    samples = []
    for _ in range(N):
        samples.append(rng.next_int())

    mean, std, m2, m3, m4 = compute_stats(samples)

    print("Raw-integer version (0 ≤ X < m):")
    print("  N =", N)
    print("  mean = {:.6e}".format(mean))
    print("  std dev = {:.6e}".format(std))
    print("  2nd moment m2 = {:.6e}".format(m2))
    print("  3rd moment m3 = {:.6e}".format(m3))
    print("  4th moment m4 = {:.6e}".format(m4))
    # Note: for raw ints the “expected moments” depend on the uniform integer distribution

def run_unit_interval():
    # same LCG, but we convert to float in [0,1)
    seed = 123456789
    a = 1103515245
    c = 12345
    m = 2**31

    rng = LCG(seed, a, c, m)
    N = 1_000_000
    samples = []
    for _ in range(N):
        samples.append(rng.next_float())

    mean, std, m2, m3, m4 = compute_stats(samples)

    print("Unit-interval version (0 ≤ U < 1):")
    print("  N =", N)
    print("  mean = {:.6f}".format(mean))
    print("  std dev = {:.6f}".format(std))
    print("  2nd moment m2 = {:.6f}".format(m2))
    print("  3rd moment m3 = {:.6f}".format(m3))
    print("  4th moment m4 = {:.6f}".format(m4))

    # Theoretical expected values for a perfect uniform [0,1) distribution:
    #   E[U] = 1/2
    #   Var(U) = 1/12  => std = sqrt(1/12)
    #   E[U^2] = 1/3
    #   E[U^3] = 1/4
    #   E[U^4] = 1/5
    print("  Theoretical E[U] = 0.5")
    print("  Theoretical Var(U) = 1/12 = {:.6f}".format(1/12))
    print("  Theoretical E[U^2] = 1/3 = {:.6f}".format(1/3))
    print("  Theoretical E[U^3] = 1/4 = {:.6f}".format(1/4))
    print("  Theoretical E[U^4] = 1/5 = {:.6f}".format(1/5))


if __name__ == "__main__":
    run_raw_ints()
    print()
    run_unit_interval()

