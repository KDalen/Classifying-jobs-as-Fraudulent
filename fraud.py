import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno

data = pd.read_csv('fake_job_postings.csv')
print(data.head())
msno.matrix(data)
