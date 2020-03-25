# 1.debug的能力
# 2.加注释
# 3.高级应用：内置的一些Python算法包 collections,itertools，第三方的lib包：numpy
# 4.递归
# T(n) = T(n-1) + 1
# 5.图论（BFS，DFS）
# A->F
#    0 1 2 3 4
# 0  0 1 1 1 0
# 1  1 0 0 0 0
# 2  0 1 0 0 0
# 3  0 1 0 0 1
# 4  0 0 0 1 0
grid = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0]
]
from collections import defaultdict

components_points = defaultdict(list)


def find_components(row_index, column_index, grid, number_of_components):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    grid[row_index][column_index] = number_of_components

    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    if number_of_components > 5:
        return False

    components_points[number_of_components].append((row_index, column_index))

    result =  find_components(next_row_index, next_column_index, grid, number_of_components)
    if result == False :
        return False
    return True

def method_recursion():
    if grid:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        number_of_components = 2
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                if grid[row_index][column_index] == 1:
                    find_components(row_index, column_index, grid, number_of_components)
                    number_of_components += 1

        print(f"number of components is : {number_of_components}")

        print(grid)
        for component_index, points in components_points.items():
            print(component_index, points)


def method_iterative():
    if grid:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        visited = []
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        number_of_components = 0

        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                if grid[row_index][column_index] == 1 and (row_index,column_index) not in visited:
                    path = [(row_index, column_index)]
                    while path:
                        # 弹出正在处理点
                        current_point = path.pop()
                        visited.append(current_point)
                        current_row_index, current_column_index = current_point
                        for (row_direction, column_direction) in directions:
                            next_row_index, next_column_index = \
                                current_row_index + row_direction, current_column_index + column_direction
                            if 0 <= next_row_index < number_of_rows and \
                                    0 <= next_column_index < number_of_columns and \
                                    grid[next_row_index][next_column_index] == 1 \
                                    and (next_row_index, next_column_index) not in visited:
                                path.append((next_row_index, next_column_index))

                    number_of_components += 1

        print(f"number of components is : {number_of_components}")

        print(grid)
        for component_index, points in components_points.items():
            print(component_index, points)


method_iterative()

