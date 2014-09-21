# -*- coding: utf-8 -*-

"""
Excelファイル(.xls)をcsv形式に変換して読み込み、散布図・ヒストグラムを作成、
または回帰分析を行うためのプログラム
データ型はDataFrame、またはSeriesになる
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csvファイルをDataFrame型に読み込み、indexを変更
course_after_hischool = pd.read_csv('H22_univ.csv')
A = course_after_hischool
prefectures = A.pop('prefecture')
A.index = prefectures

#新しいSeriesを作成、追加
B = A['to_univ']
C = A['to_college']
D = B + C
A['learn'] = D

operations = 'hist'

#並び替え、ヒストグラムの作成
if operations == 'hist':
    B = A.sort_index(by = 'learn', ascending = False)
    B['learn'].plot()
    plt.show()

#散布図の作成
if operations == 'plot':
    pd.tools.plotting.scatter_plot(A, 'learn', 'univ_per_mill', color='green')
    plt.show()

#回帰分析を行う
if operations == 'regress':
    regression = pd.ols(y=A['learn'], x=A['univ_per_mill'], intercept = True)
    print(regression)