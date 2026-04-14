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
# 任务5：线路驾驶员信息批量导出
print("\n" + "=" * 60)
print("任务5：线路驾驶员信息批量导出")
print("=" * 60)

# 1. 筛选线路号在1101至1120之间的所有记录
print("1. 筛选线路号在1101至1120之间的记录...")
filtered_df = df[(df['线路号'] >= 1101) & (df['线路号'] <= 1120)]
unique_routes = sorted(filtered_df['线路号'].unique())
print(f"   筛选出 {len(unique_routes)} 条线路: {unique_routes}")

# 2. 创建名为"线路驾驶员信息"的文件夹
print("\n2. 创建文件夹...")
folder_name = "线路驾驶员信息"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"   已创建文件夹: {folder_name}")
else:
    print(f"   文件夹已存在: {folder_name}")

# 3. 对每条线路，输出车辆编号→驾驶员编号对应关系
print("\n3. 生成线路驾驶员信息文件...")
generated_files = []

for route in unique_routes:
    # 筛选该线路的记录
    route_df = filtered_df[filtered_df['线路号'] == route]
    
    # 获取唯一的（车辆编号，驾驶员编号）组合
    vehicle_driver_pairs = route_df[['车辆编号', '驾驶员编号']].drop_duplicates()
    
    # 写入文件
    filename = f"{folder_name}/{route}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"线路号: {route}\n")
        f.write("车辆编号 驾驶员编号\n")
        for _, row in vehicle_driver_pairs.iterrows():
            f.write(f"{int(row['车辆编号'])} {int(row['驾驶员编号'])}\n")
    
    generated_files.append(filename)

# 4. 打印文件生成路径
print("\n4. 文件生成路径：")
for file in generated_files:
    print(f"   {file}")

print(f"\n   已成功生成 {len(generated_files)} 个文件")

