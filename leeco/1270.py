import pandas as pd

CEO = 1

# 第 1 层
level1 = employees.loc[(employees['manager_id'] == CEO) & 
                       (employees['employee_id'] != CEO), 'employee_id']

# 第 2 层
level2 = employees.loc[employees['manager_id'].isin(level1), 'employee_id']

# 第 3 层
level3 = employees.loc[employees['manager_id'].isin(level2), 'employee_id']

# 合并所有层级
result = pd.concat([level1, level2, level3]).drop_duplicates().sort_values()

print(result.to_frame('employee_id'))
