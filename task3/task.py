import numpy as np

def calculate_entropy(csv_data: list) -> float:
    n, m = csv_data.shape
    total_entropy = 0

    for i in range(n):
        row_entropy = 0

        for j in range(m):
            if not csv_data[i, j]:
                continue

            probability = csv_data[i, j] / n
            row_entropy += probability * np.log2(probability)

        total_entropy -= row_entropy

    return total_entropy

def task(csv_string: str) -> float:
    csv_data = np.array([list(map(int, row.split(','))) for row in csv_string.strip().split('\n')])
    return calculate_entropy(csv_data)

if __name__ == "__main__":
    print(task("2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1"))
