import pandas as pd

# 示例数据
data = {
    'user_id': [1,1,1,2,2,2,3,3,3,4,4],
    'session_id': [1,1,1,4,4,4,2,2,2,3,3],
    'activity_date': ['2019-07-20','2019-07-20','2019-07-20',
                      '2019-07-20','2019-07-21','2019-07-21',
                      '2019-07-21','2019-07-21','2019-07-21',
                      '2019-06-25','2019-06-25'],
    'activity_type': ['open_session','scroll_down','end_session',
                      'open_session','send_message','end_session',
                      'open_session','send_message','end_session',
                      'open_session','end_session']
}

df = pd.DataFrame(data)

# 转换为日期类型
df['activity_date'] = pd.to_datetime(df['activity_date'])

# 定义截止日期
end_date = pd.to_datetime('2019-07-27')
start_date = end_date - pd.Timedelta(days=29)  # 最近30天，包括今天

# 筛选近30天数据
df_30 = df[(df['activity_date'] >= start_date) & (df['activity_date'] <= end_date)]

# 按天统计活跃用户
result = df_30.groupby('activity_date')['user_id'].nunique().reset_index()
result.columns = ['day', 'active_users']

print(result)
