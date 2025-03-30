def pascal(rowIndex):
    coefficients = [1]

    for Index in range(1, rowIndex + 1):
        nextCoefficient = coefficients[-1] * (rowIndex - Index + 1) // Index
        coefficients.append(nextCoefficient)
    return coefficients

print(pascal(4))