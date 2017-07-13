#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:11:09 2016

@author: Mateus Vilione Braz Lima
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix
data_df = pd.read_csv('/home/ubuntu/workspace/glass.csv')
print('Amostra correspondente a 30% da base de dados original')
amostra=data_df.sample(np.floor(0.3*data_df.shape[0]))
print(amostra)

print('-----------------------------------------------------------------')

print('media da base')
print(data_df.mean())
print('media da amostra')
print(amostra.mean())

print('-----------------------------------------------------------------')

print('\nmedia da base para o atributo potassium')
print(data_df['K'].mean())

print('\ndesvio padrão da base para o atributo potassium')
print(data_df['K'].std())

print('\nmaior da base para o atributo potassium')
print(data_df['K'].max())

print('\nmenor da base para o atributo potassium')
print(data_df['K'].min())

print('-----------------------------------------------------------------')

print('\n quantidade de instâncias por tipo diferente de vidro')

print(data_df['Type'].value_counts())

print('-----------------------------------------------------------------')

plt.matshow(data_df.corr())



