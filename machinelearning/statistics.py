'''STATISTICS FOR AI/ML'''

import numpy_practice as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

'''employee salaries(in thousand)'''
# salaries=[22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

'''central tendency-where is the 'centre' of data'''
# mean =np.mean(salaries) #average
# median=np.median(salaries) #middle value when sorted
# mode=stats.mode(salaries,keepdims=True).mode[0] #most frequent

# print(f'mean (average):Rs.{mean:.1f}k')
# print(f'median  (middle value):Rs.{median}k')
# print(f'mode  (most common): Rs.{mode}k')

'''spread--how varied is data'''
# std=np.std(salaries)
# var=np.var(salaries)
# rng=max(salaries)-min(salaries)
# q1=np.percentile(salaries,25)
# q3=np.percentile(salaries,75)
# iqr= q3-q1
# print(f'std daviation : {std:.2f}K  (most important spread measure)')
# print(f'IQR :  {iqr}K   (Q1={q1}, Q3={q3})')

'''outler detection using IQR(interquartile range)'''
# lower=q1-1.5*iqr
# upper=q3+1.5*iqr
# outliers=[x for x in salaries if x< lower or x> upper]
# print(f'outliers:{outliers}')

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats

'''employee salaries(in thousand)'''
# salaries=[22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

'''central tendency-where is the 'centre' of data'''
# mean =np.mean(salaries) #average
# median=np.median(salaries) #middle value when sorted
# mode=stats.mode(salaries,keepdims=True).mode[0] #most frequent

# print(f'mean (average):Rs.{mean:.1f}k')
# print(f'median  (middle value):Rs.{median}k')
# print(f'mode  (most common): Rs.{mode}k')

'''spread--how varied is data'''
# std=np.std(salaries)
# var=np.var(salaries)
# rng=max(salaries)-min(salaries)
# q1=np.percentile(salaries,25)
# q3=np.percentile(salaries,75)
# iqr= q3-q1
# print(f'std daviation : {std:.2f}K  (most important spread measure)')
# print(f'IQR :  {iqr}K   (Q1={q1}, Q3={q3})')

'''outler detection using IQR(interquartile range)'''
# lower=q1-1.5*iqr
# upper=q3+1.5*iqr
# outliers=[x for x in salaries if x< lower or x> upper]
# print(f'outliers:{outliers}')

'''correlation'''
# import numpy as np
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# #data
# np.random.seed(42)
# study=np.random.uniform(2,10,60)
# marks=study*8+np.random.normal(0,10,60)
# marks=np.clip(marks,30,100)
# absent=10-study+np.random.normal(0,1,60)

# df=pd.DataFrame({'study_hours':study,'marks':marks,'absenses':absent})
# corr_matrix=df.corr()
# print(corr_matrix.round(3))

# plt.figure(figsize=(6,4))
# sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',vmin=-1,vmax=1,fmt='.2f')
# plt.title('correlation matrix')
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm #normal distribution claculator

mean_h, std_h = 165, 7

#probability of being talller than 175 cm
prob = 1- norm.cdf(175, mean_h, std_h)#camulative distribution function
print(f'P(height > 175cm)= {prob: .4f} = {prob*100:.1f}%')

# #The 68-95-99
# print(f'68% of people: {mean_h-std_h :.0f}cm to {mean_h+std_h: .0f}cm')
# print(f'95% of people: {mean_h-2*std_h: 0f}cm to {+2*std_h: .0f}cm')
# print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h: .0f}')

# from sklearn.model_selection import train_test_split, cross_val_score

# np.random.seed(42)
# x = np.random.randn(500, 5)
# y = np.random.randint(0, 2, 500)

# x_train,x_test,y_train,y_test = train_test_split(
#   x,y, test_size = 0.2, random_state=42, stratify=y
#   )

# print(f'Training samples: {len(x_train)} | Test samples: {len(x_test)}')

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=50 , random_state=42)
# cv_scores = cross_val_score(model, x, y, cv = 5, scoring = 'accuracy')
# print(f'cv score each fold:{cv_scores,round(3)}')
# print(f'mean: {cv_scores.mean(): .4f} = {cv_scores.std():.4f}')



'''A/B testing analysis (chi square and p-value) '''
# import numpy as np
# from scipy import stats 
# import matplotlib.pyplot as plt

# #Data
# n_A,conv_A=1000,52
# n_B,conv_B=1000,68
# rate_A=conv_A/n_A
# rate_B=conv_B/n_B

# print(f'version A conversion rate:{rate_A*100:.1f}%')
# print(f'version B conversion rate:{rate_B*100:.1f}%')
# print(f'improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# #chi-square test for statistical significcant
# table=[[conv_A,n_A-conv_A],[conv_B,n_B-conv_B]]
# chi2,p_value,dof,expected=stats.chi2_contingency(table)

# print(f'chisquare: {chi2:.4f}')
# print(f'p-value:{p_value:.4f}')
# print('Result:','Significant - B is better!' if p_value<0.05 else 'not significant-could be random')



'''chi nd p value '''
# import numpy as np
# from scipy import stats 
# import matplotlib.pyplot as plt

# #Data
# n_A,conv_A=1000,52
# n_B,conv_B=1000,68
# rate_A=conv_A/n_A
# rate_B=conv_B/n_B

# print(f'version A conversion rate:{rate_A*100:.1f}%')
# print(f'version B conversion rate:{rate_B*100:.1f}%')
# print(f'improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# #chi-square test for statistical significcant
# table=[[conv_A,n_A-conv_A],[conv_B,n_B-conv_B]]
# chi2,p_value,dof,expected=stats.chi2_contingency(table)

# print(f'chisquare: {chi2:.4f}')
# print(f'p-value:{p_value:.4f}')
# print('Result:','Significant - B is better!' if p_value<0.05 else 'not significant-could be random')

