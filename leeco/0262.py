import pandas as pd

# # === 数据 ===
trips = pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9,10],
    'client_id':[1,2,3,4,1,2,3,2,3,4],
    'driver_id':[10,11,12,13,10,11,12,12,10,13],
    'city_id':[1,1,6,6,1,6,6,12,12,12],
    'status':['completed','cancelled_by_driver','completed','cancelled_by_client',
              'completed','completed','completed','completed','completed','cancelled_by_driver'],
    'request_at':['2013-10-01','2013-10-01','2013-10-01','2013-10-01',
                  '2013-10-02','2013-10-02','2013-10-02','2013-10-03','2013-10-03','2013-10-03']
})

users = pd.DataFrame({
    'users_id':[1,2,3,4,10,11,12,13],
    'banned':['No','Yes','No','No','No','No','No','No'],
    'role':['client','client','client','client','driver','driver','driver','driver']
})

# # === 步骤 ===
# clients = users[(users['banned'] == 'No') & (users['role'] == 'client')]
# drivers = users[(users['banned'] == 'No') & (users['role'] == 'driver')]

# merged = trips.merge(clients, left_on='client_id', right_on='users_id') \
#               .merge(drivers, left_on='driver_id', right_on='users_id', suffixes=('_client', '_driver'))

# merged = merged[(merged['request_at'] >= '2013-10-01') & (merged['request_at'] <= '2013-10-03')]

# result = merged.groupby('request_at').agg(
#     total=('id', 'count'),
#     cancelled=('status', lambda x: (x.isin(['cancelled_by_driver','cancelled_by_client'])).sum())
# )
# result['Cancellation Rate'] = (result['cancelled'] / result['total']).round(2)
# result = result.reset_index().rename(columns={'request_at':'Day'})
# result = result[['Day','Cancellation Rate']]

# print(result)
# 从users表中获取非禁止用户的列表（包括客户和司机，注意users表里有role字段区分）。
n=users[users['banned']=='No']['users_id']
n
# 过滤trips表，只保留client_id和driver_id都在非禁止用户列表中的行程，并且request_at在2013-10-01至2013-10-03之间。
a=trips[(trips.client_id.isin(n))&(trips.driver_id.isin(n))]

b=trips.query('client_id in @n ')
print(b)