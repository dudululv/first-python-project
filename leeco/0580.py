import pandas as pd

def department_student_number(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 左连接：保证所有部门都出现
    df = department.merge(student, on='dept_id', how='left')

    # 按部门名统计学生数（student_id 为空的要算 0）
    result = df.groupby('dept_name')['student_id'].count().reset_index(name='student_number')

    # 排序：人数降序，再按部门名升序
    result = result.sort_values(['student_number', 'dept_name'], ascending=[False, True])

    return result
