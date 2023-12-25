def task(edges_csv: str):
    edges = edges_csv.split('\n')
    matrix = {}

    def update_count(index, column):
        if index not in matrix:
            matrix[index] = [0, 0, 0, 0, 0]
        matrix[index][column] += 1

    for edge in edges:
        sup, inf = map(int, edge.split(','))
        sup -= 1
        inf -= 1

        update_count(sup, 0)
        update_count(inf, 1)

    for edge in edges:
        sup, inf = map(int, edge.split(','))
        sup -= 1
        inf -= 1

        matrix[sup][2] += matrix[inf][0]
        matrix[inf][3] += matrix[sup][1]
        matrix[inf][4] += matrix[sup][0] - 1

    result = []
    for row in matrix.values():
        result.append(','.join(map(str, row)))

    return '\n'.join(result)


if __name__ == "__main__":
    print(task("1,2\n2,3\n2,6\n3,4\n3,5"))
