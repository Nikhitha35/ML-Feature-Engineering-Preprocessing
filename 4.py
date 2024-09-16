import numpy as np
matrix = np.array([[7,8,9], 
                   [4,5,6], 
                   [1,2,3]])
covariance_matrix = np.cov(matrix, rowvar=False)
correlation_matrix = np.corrcoef(matrix, rowvar=False)
print(f"Covariance Matrix:\n{covariance_matrix}")
print(f"Correlation Matrix:\n{correlation_matrix}")
