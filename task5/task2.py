import json
import numpy as np

# Загрузка данных из файла JSON
def load_data(json_path):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Преобразование списка с учетом экспертизы
def flatten_expertise(input_data):
    indices = []
    flattened = []
    idx_counter = 0
    for group in input_data:
        if not isinstance(group, list):
            group = [group]
        for item in group:
            indices.append(idx_counter)
            flattened.append(item)
        idx_counter += 1
    return flattened, indices

# Создание бинарной матрицы на основе экспертного списка
def binary_matrix(expert_data):
    flattened, indices = flatten_expertise(expert_data)
    length = len(flattened)
    matrix = np.zeros((length, length), dtype=int)

    for i, element in enumerate(flattened):
        i_idx = indices[i]
        for j, other_element in enumerate(flattened):
            j_idx = indices[j]
            if i_idx <= j_idx:
                matrix[element - 1, other_element - 1] = 1

    return matrix.tolist()

# Определение общего ядра двух матриц
def joint_kernel(matrix_one, matrix_two):
    core_1 = np.array(matrix_one)
    core_2 = np.array(matrix_two)
    
    intersection = np.logical_or(core_1 & core_2, core_1.T & core_2.T).astype(int)
    non_common_pairs = [(i+1, j+1) for i in range(intersection.shape[0]) for j in range(i, intersection.shape[1]) if not intersection[i, j]]

    combined_pairs = []
    for pair in non_common_pairs:
        pair_set = set(pair)
        combined = False
        for combined_pair in combined_pairs:
            if pair_set & set(combined_pair):
                combined_pair.extend(pair_set - set(combined_pair))
                combined = True
                break
        if not combined:
            combined_pairs.append(list(pair_set))
    
    return combined_pairs

# Поиск элемента в ядре
def find_in_core(element, elements_core):
    for cluster in elements_core:
        if element in cluster:
            return True, cluster
    return False, []

# Сопоставление данных экспертов с учетом общего ядра
def experts_agreement(expert_one, expert_two, core):
    combined_results = []

    for group_one in map(lambda x: [x] if isinstance(x, int) else x, expert_one):
        for group_two in map(lambda x: [x] if isinstance(x, int) else x, expert_two):

            common_elements = set(group_one) & set(group_two)
            for element in group_one:
                found_in_core, core_cluster = find_in_core(element, core)
                if found_in_core:
                    if core_cluster not in combined_results:
                        combined_results.append(core_cluster)
                        break
            
            if common_elements and not found_in_core:
                if len(common_elements) > 1:
                    combined_results.append(list(common_elements))
                else:
                    combined_results.append(common_elements.pop())

    print(combined_results)
