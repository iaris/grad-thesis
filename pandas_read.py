# -*- coding: utf-8 -*-

%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Excelファイル(.xls)をcsv形式に変換して読み込み、散布図・グラフを作成、
または回帰分析を行うためのプログラム
データ型はDataFrame、またはSeriesになる
"""

<<<<<<< HEAD
# csv�t�@�C����DataFrame�^�ɓǂݍ��݁Aindex��ύX
course_after_hischool = pd.read_csv('H22_univ.csv')
A = course_after_hischool
=======
%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csvファイルをDataFrame型に読み込み、indexを変更
A = pd.read_csv('H22_univ.csv')
>>>>>>> 3a258e39c637be72f5ee9adfd6aaf5270513d645
prefectures = A.pop('prefecture')
A.index = prefectures

"""
#新しいSeriesを作成、追加
B = A['to_univ']
C = A['to_college']
D = B + C
A['learn'] = D
"""

<<<<<<< HEAD

operations = 'bar'

#���ёւ��A�_�O���t�̍쐬
if operations == 'bar':
    B = A.sort_index(by = 'learn', ascending = False)
    B['to_univ'].plot(kind = 'bar')
=======
operations = 'graph'

#並び替え、グラフの作成
if operations == 'graph':
    B = A.sort_index(by = 'to_univ', ascending = False)
    B['to_univ'].plot()
>>>>>>> 3a258e39c637be72f5ee9adfd6aaf5270513d645
    plt.show()

#散布図の作成
if operations == 'plot':
    pd.tools.plotting.scatter_plot(A, 'learn', 'upm', color='green')
    plt.show()

#回帰分析を行う
if operations == 'regress':
<<<<<<< HEAD
    vals = ['upm', 'bcdum', 'dsmf', 'rowo', 'phi']
    regression = pd.ols(y=A['learn'], x=A[vals], intercept = True)
    print(regression)
=======
    ind_var = ['univ_per_mil', 'rate']
    regression = pd.ols(y=A['learn'], x=A[ind_var], intercept = True)
    print(regression)
>>>>>>> 3a258e39c637be72f5ee9adfd6aaf5270513d645
