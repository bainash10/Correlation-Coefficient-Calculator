import numpy as np

def correlation_analysis(x, y):
    # Calculate correlation coefficient
    correlation_coefficient = np.corrcoef(x, y)[0, 1]

    # Interpretation of correlation coefficient
    if correlation_coefficient > 0:
        correlation_strength = "strong" if correlation_coefficient >= 0.7 else "moderate"
        interpretation = "There is a {} positive correlation (r = {:.2f}).".format(correlation_strength, correlation_coefficient)
    elif correlation_coefficient < 0:
        correlation_strength = "strong" if correlation_coefficient <= -0.7 else "moderate"
        interpretation = "There is a {} negative correlation (r = {:.2f}).".format(correlation_strength, correlation_coefficient)
    else:
        interpretation = "There is no correlation (r = {:.2f}).".format(correlation_coefficient)

    return correlation_coefficient, interpretation

# Example usage
try:
    x = list(map(float, input("Enter the values of the first variable (space-separated values): ").split()))
    y = list(map(float, input("Enter the values of the second variable (space-separated values): ").split()))

    if len(x) != len(y):
        raise ValueError("The number of values for both variables must be the same.")

    correlation_coefficient, interpretation = correlation_analysis(x, y)
    print("Correlation Coefficient (r) =", correlation_coefficient)
    print(interpretation)
except ValueError as e:
    print("Invalid input: {}".format(e))
