import numpy as np

def build_matrix(edges):
    matrix = {}
    
    def update_count(index, column):
        if index not in matrix:
            matrix[index] = [0, 0, 0, 0, 0]
        matrix[index][column] += 1
    
    for edge in edges:
        high, low = map(int, edge.split(','))
        high -= 1
        low -= 1
        
        update_count(high, 0)
        update_count(low, 1)

    for edge in edges:
        high, low = map(int, edge.split(','))
        high -= 1
        low -= 1
        
        matrix[high][2] += matrix[low][0]
        matrix[low][3] += matrix[high][1]
        matrix[high][4] += matrix[low][0] - 1

    return [matrix[i] for i in range(len(matrix))]

def calculate_entropy(matrix):
    n = len(matrix)
    entropy = 0
    for row in matrix:
        for num in row:
            p = num / (n - 1)
            if p > 0:
                entropy -= p * np.log2(p)
    return round(entropy, 1)

if __name__ == "__main__":
    csv_data = build_matrix(["1,2","2,3","2,6","3,4","3,5"])
    result = calculate_entropy(csv_data)
    print(result)
