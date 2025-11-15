import pandas as pd

# 1. 只保留 login 行
login = df[df['activity'] == 'login']

# 2. 每个用户首次登录日期
first_login = login.groupby('user_id', as_index=False)['activity_date'].min()
first_login.rename(columns={'activity_date': 'first_login'}, inplace=True)

# 3. 过滤最近 90 天内首次登录的用户
start_date = pd.to_datetime('2019-06-30') - pd.Timedelta(days=90)

filtered = first_login[
    (first_login['first_login'] >= start_date) &
    (first_login['first_login'] <= '2019-06-30')
]

# 4. 按首次登录日期计数
result = filtered.groupby('first_login', as_index=False)['user_id'].count()

# 5. 改名成题目要求格式
result.rename(columns={
    'first_login': 'login_date',
    'user_id': 'user_count'
}, inplace=True)

result
