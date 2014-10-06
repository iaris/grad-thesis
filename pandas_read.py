# -*- coding: utf-8 -*-

"""
Excelファイル(.xls)をcsv形式に変換して読み込み、散布図・グラフを作成、
または回帰分析を行うためのプログラム
データ型はDataFrame、またはSeriesになる
"""

%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csvファイルをDataFrame型に読み込み、indexを変更
A = pd.read_csv('H22_univ.csv')
prefectures = A.pop('prefecture')
A.index = prefectures

"""
#新しいSeriesを作成、追加
B = A['to_univ']
C = A['to_college']
D = B + C
A['learn'] = D
"""

operations = 'graph'

#並び替え、グラフの作成
if operations == 'graph':
    B = A.sort_index(by = 'to_univ', ascending = False)
    B['to_univ'].plot()
    plt.show()

#散布図の作成
if operations == 'plot':
    pd.tools.plotting.scatter_plot(A, 'learn', 'univ_per_mill', color='green')
    plt.show()

#回帰分析を行う
if operations == 'regress':
    ind_var = ['univ_per_mil', 'rate']
    regression = pd.ols(y=A['learn'], x=A[ind_var], intercept = True)
    print(regression)
