# -*- coding: utf-8 -*-
"""
Created on Thu May 18 13:17:59 2023

@author: admlocal
"""

import web_glassdoor_scraper as gs
import pandas as pd

path="C:/Users/admlocal/Desktop/chromedriver.exe"

gs.get_jobs("data_science", 30, False, path, 15)