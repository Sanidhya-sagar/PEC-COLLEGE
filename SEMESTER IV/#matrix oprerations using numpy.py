#matrix oprerations using numpy

import numpy as np

def create_matrix(rows, cols):
    return np.random.randint(1, 10, size=(rows, cols))


def perform_operations(matrix1, matrix2):
    
    dot_product = np.dot(matrix1, matrix2.T) 

    scalar_product = np.multiply(matrix1, 5)  

    cross_product = np.cross(matrix1, matrix2)

    return dot_product, scalar_product, cross_product


def find_min_max(matrix):
    minimum = np.min(matrix)
    maximum = np.max(matrix)
    return minimum, maximum

def sum_diagonal_duddy(matrix):
    diagonal_sum = np.trace(matrix)
    return diagonal_sum

# Main function
def main():
    # Create matrices
    matrix1 = create_matrix(3, 3)
    matrix2 = create_matrix(3, 3)

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    # Perform operations
    dot_product, scalar_product, cross_product = perform_operations(matrix1, matrix2)

    print("\nDot Product:")
    print(dot_product)

    print("\nScalar Product:")
    print(scalar_product)

    print("\nCross Product:")
    print(cross_product)

    # Find min and max
    min_value, max_value = find_min_max(matrix1)
    print(f"\nMinimum Value: {min_value}")
    print(f"Maximum Value: {max_value}")

    # Find sum of diagonal elements
    diagonal_sum = sum_diagonal_duddy(matrix1)
    print(f"\nSum of Diagonal Elements: {diagonal_sum}")

main()