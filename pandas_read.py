# -*- coding: utf-8 -*-

"""
Excel�t�@�C��(.xls)��csv�`���ɕϊ����ēǂݍ��݁A�U�z�}�E�q�X�g�O�������쐬�A
�܂��͉�A���͂��s�����߂̃v���O����
�f�[�^�^��DataFrame�A�܂���Series�ɂȂ�
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csv�t�@�C����DataFrame�^�ɓǂݍ��݁Aindex��ύX
course_after_hischool = pd.read_csv('H22_univ.csv')
A = course_after_hischool
prefectures = A.pop('prefecture')
A.index = prefectures

#�V����Series���쐬�A�ǉ�
B = A['to_univ']
C = A['to_college']
D = B + C
A['learn'] = D

operations = 'hist'

#���ёւ��A�q�X�g�O�����̍쐬
if operations == 'hist':
    B = A.sort_index(by = 'learn', ascending = False)
    B['learn'].plot()
    plt.show()

#�U�z�}�̍쐬
if operations == 'plot':
    pd.tools.plotting.scatter_plot(A, 'learn', 'univ_per_mill', color='green')
    plt.show()

#��A���͂��s��
if operations == 'regress':
    regression = pd.ols(y=A['learn'], x=A['univ_per_mill'], intercept = True)
    print(regression)