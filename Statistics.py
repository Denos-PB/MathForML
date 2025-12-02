import numpy as np
import pandas as pd
# Problem: You are tracking the daily page views (in thousands)
#  for the past five days: 78,92,85,95,80. 
# What is the average (mean) daily page view count?

pages = [78,92,85,95,80]
d_page = np.mean(pages)
print(d_page)

