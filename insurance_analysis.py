import numpy as np


def calculate_regression_coefficients(data):
    # Select vehicle characteristics
    X = data[['Power', 'Value_vehicle', 'Weight']].to_numpy()

    # Select actual insurance premiums
    y = data['Premium'].to_numpy()

    # Add a column of ones for the intercept
    X = np.column_stack((np.ones(len(X)), X))

    # Calculate regression coefficients using least squares
    coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

    return coefficients