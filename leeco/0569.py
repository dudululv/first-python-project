import pandas as pd

# 示例数据（和你题目一致）
data = {
    "id": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
    "company": ["A","A","A","A","A","A","B","B","B","B","B","B","C","C","C","C","C"],
    "salary":  [2341,341,15,15314,451,513,15,13,1154,1345,1221,234,2345,2645,2645,2652,65]
}
df = pd.DataFrame(data)

# 排序后在公司内打 rank（从1开始）
df = df.sort_values(['company', 'salary', 'id']).reset_index(drop=True)
df['rank'] = df.groupby('company').cumcount() + 1

# 计算每个公司的人数（cnt），并计算整数中位位置 m1,m2
df['cnt'] = df.groupby('company')['id'].transform('count')
df['m1'] = (df['cnt'] + 1) // 2
df['m2'] = (df['cnt'] + 2) // 2

# 选出 rank 等于 m1 或 m2 的行
median_rows = df[(df['rank'] == df['m1']) | (df['rank'] == df['m2'])]

# 输出需要的列
result = median_rows[['id', 'company', 'salary']].reset_index(drop=True)
print(result)
