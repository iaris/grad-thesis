# -*- coding: utf-8 -*-

%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Excel�t�@�C��(.xls)��csv�`���ɕϊ����ēǂݍ��݁A�U�z�}�E�q�X�g�O�������쐬�A
�܂��͉�A���͂��s�����߂̃v���O����
�f�[�^�^��DataFrame�A�܂���Series�ɂȂ�
"""

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

operations = 'plot'

#���ёւ��A�_�O���t�̍쐬
if operations == 'bar':
    B = A.sort_index(by = 'learn', ascending = False)
    B['learn'].plot(kind = 'bar')
    plt.show()

#�U�z�}�̍쐬
if operations == 'plot':
    pd.tools.plotting.scatter_plot(A, 'learn', 'phi', color='green')
    plt.show()

#��A���͂��s��
if operations == 'regress':
    vals = ['upm', 'bcdum', 'dsmf', 'rowo', 'phi']
    regression = pd.ols(y=A['learn'], x=A[vals], intercept = True)
    print(regression)