import pandas as pd

# 示例数据
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Tom', 'Jerry', 'John']
})

orders = pd.DataFrame({
    'order_id': [1,2,3,4,5,6,7,8,9,10],
    'order_date': ['2020-07-31','2020-07-30','2020-08-29','2020-07-29','2020-06-10',
                   '2020-08-01','2020-08-01','2020-08-03','2020-08-07','2020-07-15'],
    'customer_id': [1,2,3,4,1,2,3,1,2,1],
    'product_id': [1,2,3,1,2,1,3,2,3,2]
})

products = pd.DataFrame({
    'product_id': [1,2,3,4],
    'product_name': ['keyboard','mouse','screen','hard disk'],
    'price': [120,80,600,450]
})

# 1. 统计每个顾客每个商品的下单次数
order_counts = orders.groupby(['customer_id','product_id']).size().reset_index(name='count')

# 2. 找出每个顾客的最大下单次数
max_counts = order_counts.groupby('customer_id')['count'].transform('max')
most_frequent = order_counts[order_counts['count'] == max_counts]

# 3. 与Products表连接，获取商品名称
result = most_frequent.merge(products[['product_id','product_name']], on='product_id', how='left')

# 4. 选择所需列
result = result[['customer_id','product_id','product_name']]

print(result)
