import sys
import math
from collections import Counter

def shannon_entropy_from_counts(counts: Counter, total: int) -> float:
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log(p, 2)
    return entropydef compute_entropy_file(fname: str, chunk_size: int = 1024*1024):
    counts = Counter()
    total = 0
    with open(fname, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            counts.update(chunk)
            total += len(chunk)
    return shannon_entropy_from_counts(counts, total)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    fname = sys.argv[1]
    h = compute_entropy_file(fname)
    print(f"Entropy (bits per byte): {h:.6f}")

if __name__ == "__main__":
    main()
 
