import numpy as np
vector1 = np.array([1,2,3,4])
vector2 = np.array([7,8,9,10])
covariance_matrix = np.cov(vector1, vector2)
covariance = covariance_matrix[0, 1]
print(f"Covariance Matrix:\n{covariance_matrix}")
print(f"Covariance between vec1 and vec2: {covariance}")
