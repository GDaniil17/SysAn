import csv
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        raise RuntimeError(f'Not enough params. Length of input data = {len(args)}')
    filename, y, x = args[:3]
    y = int(y)
    x = int(x)

    with open('test.csv', newline='') as csvfile:
        file_data = list(csv.reader(csvfile, delimiter=';', quotechar='|'))
        for row in file_data:
            print(row)
        print()
        if y >= len(file_data) or x >= len(file_data[y]):
            raise RuntimeError(f'Coordinates are out of bounds y = {y}, x = {x}. ',
                               'But the sizes of data are y = {len(file_data)}, x = {len(file_data[0])}')
        else:
            print(file_data[y][x])

# cmd: python task.py inputname 1 2

