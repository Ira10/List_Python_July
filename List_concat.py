import pandas as pd

L = [1, 2, 3]
M = [2, 5, 6]
N = ['p', 'pa', 'pu']

# Convert lists to pandas Series
L_series = pd.Series(L)
M_series = pd.Series(M)
N_series = pd.Series(N)

# Concatenate the Series
combined_df = pd.concat([L_series, M_series, N_series], ignore_index=True)
print(combined_df)

# 0     1
# 1     2
# 2     3
# 3     2
# 4     5
# 5     6
# 6     p
# 7    pa
# 8    pu
# dtype: object
