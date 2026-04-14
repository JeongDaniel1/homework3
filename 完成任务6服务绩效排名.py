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

# 任务6：服务绩效排名与热力图
print("\n" + "=" * 60)
print("任务6：服务绩效排名与热力图")
print("=" * 60)

# 1. 排名统计
print("1. 服务人次排名统计：")

# Top 10 司机
top_drivers = onboard_records['驾驶员编号'].value_counts().head(10)
print("\n   服务人次最多的 Top 10 司机：")
for i, (driver, count) in enumerate(top_drivers.items(), 1):
    print(f"   Top{i}: 司机 {int(driver)} - {count} 人次")

# Top 10 线路
top_routes = onboard_records['线路号'].value_counts().head(10)
print("\n   服务人次最多的 Top 10 线路：")
for i, (route, count) in enumerate(top_routes.items(), 1):
    print(f"   Top{i}: 线路 {route} - {count} 人次")

# Top 10 上车站点
top_stations = onboard_records['上车站点'].value_counts().head(10)
print("\n   服务人次最多的 Top 10 上车站点：")
for i, (station, count) in enumerate(top_stations.items(), 1):
    print(f"   Top{i}: 上车站点 {station} - {count} 人次")

# Top 10 车辆
top_buses = onboard_records['车辆编号'].value_counts().head(10)
print("\n   服务人次最多的 Top 10 车辆：")
for i, (bus, count) in enumerate(top_buses.items(), 1):
    print(f"   Top{i}: 车辆 {int(bus)} - {count} 人次")

# 2. 热力图可视化
print("\n2. 生成服务绩效热力图...")

# 准备数据矩阵
data_matrix = np.array([
    top_drivers.values,    # 司机
    top_routes.values,     # 线路
    top_stations.values,   # 上车站点
    top_buses.values       # 车辆
])

# 行标签和列标签
row_labels = ['司机', '线路', '上车站点', '车辆']
col_labels = [f'Top{i}' for i in range(1, 11)]

# 创建热力图
plt.figure(figsize=(12, 5))
sns.heatmap(data_matrix, annot=True, fmt='d', cmap='YlOrRd', 
            xticklabels=col_labels, yticklabels=row_labels)

# 设置图表属性
plt.title('服务绩效热力图', fontsize=16)
plt.xlabel('排名', fontsize=12)
plt.ylabel('维度', fontsize=12)
plt.xticks(rotation=0)

# 保存图像
plt.tight_layout()
plt.savefig('performance_heatmap.png', dpi=150, bbox_inches='tight')
print("   服务绩效热力图已保存为 performance_heatmap.png")

# 3. 结论说明
print("\n3. 结论说明：")
conclusion = """
从热力图，线路维度的服务人次明显高于其他维度，其中Top1线路的服务人次远超其他线路。
在司机维度中，Top1司机的服务人次也显著高于其他司机，说明存在TOP1司机吸引的特点。
上车站点和车辆维度的服务人次相对较为均衡，但TOP1、2的站点和车辆的服务人次明显较高。
"""
print(conclusion)

# 结果打包
print("结果打包")
# 创建zip文件
zip_filename = "第六作业结果.zip"
files_to_zip = [
    "hour_distribution.png",
    "route_stops.png", 
    "performance_heatmap.png"
]

# 添加线路驾驶员信息文件夹中的所有txt文件
for i in range(1101, 1121):
    file_path = f"线路驾驶员信息/{i}.txt"
    if os.path.exists(file_path):
        files_to_zip.append(file_path)

# 创建zip文件
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in files_to_zip:
        try:
            zipf.write(file)
        except FileNotFoundError:
            print(f"警告: 文件 {file} 未找到")

