# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:15:02 2024

@author: Khan M
"""
import pandas as pd
import matplotlib.pyplot as plt

speed = [0.1, 17.5, 40, 48, 52, 69, 88]

lifespan = [2, 8, 70, 1.5, 25, 12, 28]

index = ['snail', 'pig', 'elephant', 'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed, 'lifespan': lifespan}, index=index)

ax = df.plot.bar(rot=0)

