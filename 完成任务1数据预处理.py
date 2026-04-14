import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
import zipfile
warnings.filterwarnings('ignore')

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']
plt.rcParams['axes.unicode_minus'] = False
print("《人工智能编程语言》第六次作业 - 公交IC卡刷卡数据分析")
# 任务1：数据预处理
print("任务1：数据预处理")
# 1.1 读取数据
print("1. 读取数据...")
df = pd.read_csv('ICData.csv', sep=',')
print(f"数据集基本信息：")
print(f"  行数: {df.shape[0]}, 列数: {df.shape[1]}")
print(f"  各列数据类型：")
print(df.dtypes)
print(f"\n前5行数据：")
print(df.head())

# 1.2 时间解析
print("\n2. 时间解析...")
# 将交易时间列转换为datetime类型
df['交易时间'] = pd.to_datetime(df['交易时间'], format='%Y/%m/%d %H:%M:%S')
# 提取小时字段
df['hour'] = df['交易时间'].dt.hour
print("  已添加hour列（小时字段）")

# 1.3 构造衍生字段
print("\n3. 构造衍生字段...")
# 计算搭乘站点数 = |下车站点 - 上车站点|
df['ride_stops'] = abs(df['下车站点'] - df['上车站点'])
# 删除ride_stops为0的异常记录
initial_rows = df.shape[0]
df = df[df['ride_stops'] != 0]
deleted_rows = initial_rows - df.shape[0]
print(f"  删除了 {deleted_rows} 行 ride_stops 为 0 的异常记录")

# 1.4 缺失值检查
print("\n4. 缺失值检查...")
missing_values = df.isnull().sum()
print("  各列缺失值数量：")
print(missing_values)

# 处理缺失值
if missing_values['驾驶员编号'] > 0:
    print(f"  发现 {missing_values['驾驶员编号']} 个驾驶员编号缺失值，采用删除处理")
    df = df.dropna(subset=['驾驶员编号'])

print(f"\n预处理后数据集信息：")
print(f"  行数: {df.shape[0]}, 列数: {df.shape[1]}")
print(f"  列名: {list(df.columns)}")

