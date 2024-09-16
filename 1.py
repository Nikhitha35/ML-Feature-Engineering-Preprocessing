import numpy as np
X = np.array([2,4,4,4,5,5,7,9])
mean_X = np.mean(X)
variance_X_sample = np.var(X, ddof=1)
variance_X_population = np.var(X)
print(f"Mean: {mean_X}")
print(f"Sample Variance: {variance_X_sample}")
print(f"Population Variance: {variance_X_population}")
