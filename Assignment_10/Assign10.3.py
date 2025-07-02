import numpy as np
arr = np.array([
    [1, 2, np.nan],
    [4, np.nan, 6],
    [7, 8, 9]])
mean = np.nanmean(arr, axis=0)
nan_idx = np.where(np.isnan(arr))

# Step 3: Replace NaNs with column mean
arr[nan_idx] = mean[nan_idx[1]]

print("Replaced NaNs with column means:")
print(arr)