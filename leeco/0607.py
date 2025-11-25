import pandas as pd

# 示例数据
sales_person = pd.DataFrame({
    'sales_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
    'salary': [100000, 12000, 65000, 25000, 5000],
    'commission_rate': [6, 5, 12, 25, 10],
    'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
})

company = pd.DataFrame({
    'com_id': [1, 2, 3, 4],
    'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
    'city': ['Boston', 'New York', 'Boston', 'Austin']
})

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
    'com_id': [3, 4, 1, 1],
    'sales_id': [4, 5, 1, 4],
    'amount': [10000, 5000, 50000, 25000]
})

# 链式操作：找出没有向 RED 公司销售的销售员
result = (
    sales_person[~sales_person['sales_id'].isin(
        orders.merge(
            company[company['name'].str.strip().str.upper() == 'RED'],
            on='com_id',
            how='inner'
        )['sales_id']
    )][['name']]
)
print(result)
