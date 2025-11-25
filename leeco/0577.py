import pandas as pd

# 构造示例数据
employee = pd.DataFrame({
    "empId": [3, 1, 2, 4],
    "name": ["Brad", "John", "Dan", "Thomas"],
    "supervisor": [None, 3, 3, 3],
    "salary": [4000, 1000, 2000, 4000]
})

bonus = pd.DataFrame({
    "empId": [2, 4],
    "bonus": [500, 2000]
})

# 左连接
df = employee.merge(bonus, on="empId", how="left")

# 筛选 bonus < 1000 或 bonus 为 NaN
result = df[(df["bonus"].isna()) | (df["bonus"] < 1000)][["name", "bonus"]]

print(result)
