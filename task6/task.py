import numpy as np
import json

def compute_metric(json_a, json_b, json_c):
    # Convert JSON strings to Python lists
    data_a = json.loads(json_a)
    data_b = json.loads(json_b)
    data_c = json.loads(json_c)
    
    # Determine the data length
    data_length = len(data_a)
    score_totals = [0] * data_length
    mean_score = 0
    variance_sum = 0
    normalized_variance_limit = 9 * (data_length ** 3 - data_length) / (12 * (data_length - 1))

    # Calculate the total scores and mean score
    for index in range(data_length):
        score_totals[index] = int(data_a[index][1]) + int(data_b[index][1]) + int(data_c[index][1])
        mean_score += score_totals[index]
    mean_score /= data_length

    # Calculate the sum of squared deviations from the mean
    for score in score_totals:
        variance_sum += (score - mean_score) ** 2
    variance_sum /= 2

    # Return the normalized sum of variances
    return variance_sum / normalized_variance_limit

# Main execution point
if __name__ == "__main__":
    print(compute_metric(
        '["O1","O2","O3"]',
        '["O1","O3","O2"]',
        '["O1","O3","O2"]'
    ))
