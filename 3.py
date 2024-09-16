import numpy as np
vector1 = np.array([1,3,5,9,11])
vector2 = np.array([2,4,6,8,10])
correlation_matrix = np.corrcoef(vector1, vector2)
correlation = correlation_matrix[0, 1]
print(f"Correlation Matrix:\n{correlation_matrix}")
print(f"Correlation between vec1 and vec2: {correlation}")
