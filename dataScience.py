from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import draw
import caculate
import caculate_public_or_private
 
files = glob('./未升學未就業情形(按群別分）/*.csv')
# print(files)

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
# print(df)
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

# 篩選我們要的資料
# 目標: 先看出未升學未就業人數最多 -> 根據就業概況分析學校可以提供什麼幫助增加升學率
# 學年度 O
# 國立私立 O
# 學程別
# 群科別 就業概況 比例

# # 未升學未就業情形
# # columns1 有"補習或準備升學人數"
columns1 = ["正在接受職業訓練人數", "正在軍中服役人數", "需要工作而未找到人數", "補習或準備升學人數", "健康不良在家休養人數", "準備出國人數", "其他人數"]
# draw.draw_all(df, columns1)

 
# # 未升學未就業情形_去掉補習或準備升學人數
# # columns2 沒有"補習或準備升學人數"
columns2 = ["正在接受職業訓練人數", "正在軍中服役人數", "需要工作而未找到人數", "健康不良在家休養人數", "準備出國人數", "其他人數"]
# draw.draw_all_not_have_further_studies(df, columns2)

# # 國立公立 未升學未就業情形_去掉補習或準備升學人數
# draw.draw_public_private(df, columns1)

# 學程別 未升學未就業情形_去掉補習或準備升學人數
school_type = ["普通科", "專業群科", "綜合高中", "實用技能學程", "進修部"]
# draw.draw_school_type(df, school_type, columns1)

# 各學程各個學年度未升學未就業總人數
data = {
    '學年度': [106, 107, 108, 109, 110, 106, 107, 108, 109, 110, 106, 107, 108, 109, 110, 106, 107, 108, 109, 110, 106, 107, 108, 109, 110],
    '學程別': ['普通科', '普通科', '普通科', '普通科', '普通科', '專業群科', '專業群科', '專業群科', '專業群科', '專業群科', '綜合高中', '綜合高中', '綜合高中', '綜合高中', '綜合高中', '實用技能學程', '實用技能學程', '實用技能學程', '實用技能學程', '實用技能學程', '進修部', '進修部', '進修部', '進修部', '進修部'],
    '總人數': [3843, 5048, 3234, 1646, 1783, 5474, 5115, 3948, 3629, 2797, 560, 540, 328, 175, 158, 977, 1125, 813, 800, 587, 1584, 1369, 1077, 1102, 797]
}

# 
people = pd.DataFrame(data)

school_type = ["進修部"]  #["普通科", "專業群科", "綜合高中", "實用技能學程", "進修部"]
columns3 = ["需要工作而未找到人數"]
draw.draw_school_type_percent2(df, school_type, people, columns1)

