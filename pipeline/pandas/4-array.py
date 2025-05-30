#!/usr/bin/env python3
'''
    Take the last 10 rows of the columns High
    and Close and convert them into a numpy.ndarray
'''
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('../Data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

A = df.iloc[-10:, [3, 4]].values

<<<<<<< HEAD
print(A)
=======
print(A)
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
