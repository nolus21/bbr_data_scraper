# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:08:19 2020

@author: nowak
"""

input_file = 'D:\DK_DATA_MASTER\DK\Foedevarestyrelsen\chr_fvst_HERDS\combined_csv.csv'

import pandas as pd
import numpy as np


pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 800)
pd.set_option('display.max_rows', 25)

df = pd.read_csv(input_file, sep=',', encoding='ISO-8859-1', index_col=False)


# =============================================================================
# print(df)
# print(df['CHR-nummer'])
# print(df.Kommune)
# =============================================================================
print(df.Besætningstype)
print(df.Besætningstype)



df['Besætningstype'] = (df['Besætningstype'].replace(',','/', regex=True)
                        .astype(str))


df['Størrelse i alt antal'] = (df['Størrelse i alt antal'].astype(str).replace('.0','', regex=True)
                        .astype(str))

df['Størrelse kode A antal'] = (df['Størrelse kode A antal'].astype(str).replace('.0','', regex=True)
                        .astype(str))

df['Størrelse kode B antal'] = (df['Størrelse kode B antal'].astype(str).replace('.0','', regex=True)
                        .astype(str))

df['Størrelse kode C antal'] = (df['Størrelse kode C antal'].astype(str).replace('.0','', regex=True)
                        .astype(str))

print(df['Størrelse i alt antal'])
print(df['Størrelse kode A antal'])
print(df['Størrelse kode B antal'])
print(df['Størrelse kode C antal'])


df.to_csv( "D:\DK_DATA_MASTER\DK\Foedevarestyrelsen\chr_fvst_HERDS\CLEANED_FIN_1_combined_csv.csv", sep=';', index=True, index_label='CHR-nummer', encoding='ISO-8859-1')