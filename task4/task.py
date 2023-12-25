import numpy as np

def task() -> list:
    sums, products = set(), set()
    for i in range(1, 7):
        for j in range(1, 7):
            sums.add(i + j)
            products.add(i * j)
    
    sums, products = sorted(sums), sorted(products)
    sum_lookup = {s: sums.index(s) for s in sums}
    product_lookup = {p: products.index(p) for p in products}
    counts = np.zeros((len(sums), len(products)))
    for i in range(1, 7):
        for j in range(1, 7):
            counts[sum_lookup[i + j], product_lookup[i * j]] += 1
    
    probabilities = counts / 36

    zero_probabilities = np.abs(probabilities) > 0.0001
    entropy_AB = -np.sum(probabilities * np.log2(np.where(zero_probabilities, probabilities, 1)))
    
    probabilities_A = np.sum(probabilities, axis=1)
    zero_probabilities_A = np.abs(probabilities_A) > 0.0001
    entropy_A = -np.sum(probabilities_A * np.log2(np.where(zero_probabilities_A, probabilities_A, 1)))
    
    probabilities_B = np.sum(probabilities, axis=0)
    zero_probabilities_B = np.abs(probabilities_B) > 0.0001
    entropy_B = -np.sum(probabilities_B * np.log2(np.where(zero_probabilities_B, probabilities_B, 1)))
    
    entropy_A_B = entropy_AB - entropy_A
    
    information_AB = entropy_B - entropy_A_B
    
    return [round(i, 2) for i in [entropy_AB, entropy_A, entropy_B, entropy_A_B, information_AB]]

if __name__ == "__main__":
    print("H(AB), H(A), H(B), Ha(B), I(a,b):",task())
