
def show_beautiful_version(input_data: list):
    f_string = ""

    for item in input_data:
        if f_string:
            f_string += " < "
        if isinstance(item, list):
            f_string += "{"+", ".join(map(str, item))+"}"
        else:
            f_string += str(item)
    print(f_string)

def calculate(input_data):
    show_beautiful_version(input_data)
    group = {} # min_el, list of elements in a group
    order = []
    for item in input_data:
        if isinstance(item, list):
            order.append(item[0])
            group[item[0]] = item
        else:
            order.append(item)
            group[item] = [item]

    ans = {}
    max_el = (input_data[-1] if isinstance(input_data[-1], int) else input_data[-1][-1])
    print(f"max_el = {max_el}")
    seen = set()
    for i in order:
        for j in group[i]:
            ans[j] = [0]*max_el
            for k in range(1, max_el+1):
                ans[j][k-1] = int(k not in seen)
            #ans[j] = [0]*(i-1)+[1]*(max_el-i+1)
        seen.update(group[i])
    print(seen)
    print("Res: ")
    for i in range(1, max_el+1):
        print(i, "\t", *ans[i])
    return ans

def matrix_mult(A, B):
    if len(A) != len(B) or len(A[1]) != len(B[1]):
        raise ValueError("Sizes of A and B are different")
    return [[A[i][j] * B[i][j] for j in range(len(A[1]))] for i in range(1, max(A.keys())+1)]

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    calculate([3,[1,4],2,6,[5,7,8],[9,10]])
    A = [1,[2,3],4,[5,6,7],8,9,10]
    A = calculate(A)
    B = [[1,2],[3,4,5,],6,7,9,[8,10]]
    B = calculate(B)
    C = matrix_mult(A, B)
    print_matrix(C)
