import pandas as pd

# Users 表
users = pd.DataFrame({
    'user_id': [1, 2, 3, 4],
    'user_name': ['Moustafa', 'Jonathan', 'Winston', 'Luis'],
    'credit': [100, 200, 10000, 800]
})

# Transactions 表
transactions = pd.DataFrame({
    'trans_id': [1, 2, 3],
    'paid_by': [1, 3, 2],
    'paid_to': [3, 2, 1],
    'amount': [400, 500, 200],
    'transacted_on': ['2020-08-01', '2020-08-02', '2020-08-03']
})

# 计算每个用户支出总额
spent = transactions.groupby('paid_by')['amount'].sum().reset_index()
spent.rename(columns={'amount': 'spent'}, inplace=True)

# 计算每个用户收入总额
received = transactions.groupby('paid_to')['amount'].sum().reset_index()
received.rename(columns={'amount': 'received'}, inplace=True)

# 合并 users、spent、received
df = users.merge(spent, left_on='user_id', right_on='paid_by', how='left') \
          .merge(received, left_on='user_id', right_on='paid_to', how='left')

# 支出或收入为空时设为 0
df['spent'] = df['spent'].fillna(0)
df['received'] = df['received'].fillna(0)

# 计算交易后的余额
df['credit'] = df['credit'] - df['spent'] + df['received']

# 判断是否透支
df['credit_limit_breached'] = df['credit'].apply(lambda x: 'Yes' if x < 0 else 'No')

# 选取最终列
result = df[['user_id', 'user_name', 'credit', 'credit_limit_breached']]

print(result)
