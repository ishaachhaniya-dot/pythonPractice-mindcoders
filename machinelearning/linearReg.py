# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score

# #study hours vs exam marks
# # study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5] 
# # marks = [25,38,52,65,71,78,85,89,93,96,43,68,82,91]

# # x = np.array(study).reshape(-1,1)
# # y = np.array(marks)

# # x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# # model = LinearRegression()
# # model.fit(x_train, y_train)

# # print(f'Slope: {model.coef_[0]:.2f}(marks increase per study hour)')
# # print(f'Intercept: {model.intercept_:.2f}(marks at 0 study hours)')

# # Y_pred = model.predict(x_test)
# # print(f'R^2 score: {r2_score(y_test,Y_pred):.4f} (1.0 = perfect)')
# # print(f'RMSE: {mean_squared_error(y_test,Y_pred)**0.5: .2f}')

# # new_pred = model.predict([[7]])[0]
# # print(f'Student studying 7 hrs predicted marks:{new_pred:.1f}')

# #plot
# # plt.figure(figsize=(9,5))
# # plt.scatter(x,y,color = 'steelblue', s=100,alpha=0.8, label ='Actual')
# # plt.plot(x,model.predict(x),color='red',linewidth=2, label='predicted line')
# # plt.xlabel('study hours/day'); plt.ylabel('exam marks')
# # plt.title('linear regression - study hour vs marks')
# # plt.legend(); plt.grid(True,alpha=0.3); plt.show()

# import pandas as pd
# import numpy as np
# '''from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from sklearn.preprocessing import StandardScaler
# import seaborn as sns; import matplotlib.pyplot as plt

# #Generate student pass/fail dataset
# np.random.seed(42); n = 300
# study = np.random.uniform(1,10,n)
# attend = np.random.uniform(40,100,n)
# tasks = np.random.randint(0,11,n)
# score = study*5 + attend*0.3 + tasks*2 + np.random.normal(0,8,n)
# passed = (score > 65).astype(int)

# df = pd.DataFrame({'study':study, 'attend':attend, 'tasks':tasks, 'passed':passed})
# x = df[['study','attend','tasks']]
# y = df['passed']

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state = 42)

# scaler = StandardScaler()
# xtr = scaler.fit_transform(x_train)
# xte = scaler.transform(x_test)

# model = LogisticRegression()
# model.fit(xtr, y_train)

# y_pred = model.predict(xte)
# print(f'Accuracy: {accuracy_score(y_test,y_pred)*100:.1f}%')
# print(classification_report(y_test,y_pred,target_names=['Fail', 'Pass']))

# #confusion matrix
# cm = confusion_matrix(y_test,y_pred)
# sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',
#             xticklabels=['Fail','Pass'],yticklabels=['Fail','Pass'])'''
# plt.title('confusion matrix'); plt.show()

# #predict new student
# new = scaler.transform(([7, 85, 9]))
# pred = model.predict(new)[0]
# prob = model.predict_proba(new)[0]
# print(f'Prediction: {"Pass" if pred==1 else "Fail"} | Probability: {prob[1]*100:.1f}%')

# from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt

# iris = load_iris()
# x,y = iris.data, iris.target 
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# #Decision Tree
# dt = DecisionTreeClassifier(max_depth=3,random_state=42)
# dt.fit(x_train,y_train)
# print(f'Decision Tree Accuracy: {accuracy_score(y_test,dt.predict(x_test))*100:.1f}%')
# print(export_text(dt,feature_names = list(iris.feature_names)))

# #visualize tree
# plt.figure(figsize=(14,6))
# plot_tree(dt,feature_names=iris, feature_names,class_names=iris.target_names,
#             filled=True, rounded=True, fontsize=9)
# plt.title('Decision Tree, Iris Classification'); plt.show()

# #random forest, multiple trees  vote
# rf = RandomForestClassifier(n_estimators =100, random_state = 42)
# rf.fit(x_train,y_train)
# print(f'Random Forest Accuracy: {accuracy_score(y_test,rf.predict(x_test))*100: .1f}')

# #Feature importance, which inputs matter most

# import pandas as pd
# imp = pd.Series(rf.features_importances_,index = iris.feature.names).sort_values(ascending=False)
# imp.plot(kind = 'bar', color='steelblue')
# plt.title('Feature importance';plt.tight_layout(); plt.show())import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score

# #study hours vs exam marks
# study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5] 
# marks = [25,38,52,65,71,78,85,89,93,96,43,68,82,91]

# x = np.array(study).reshape(-1,1)
# y = np.array(marks)

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# model = LinearRegression()
# model.fit(x_train, y_train)

# print(f'Slope: {model.coef_[0]:.2f}(marks increase per study hour)')
# print(f'Intercept: {model.intercept_:.2f}(marks at 0 study hours)')

# Y_pred = model.predict(x_test)
# print(f'R^2 score: {r2_score(y_test,Y_pred):.4f} (1.0 = perfect)')
# print(f'RMSE: {mean_squared_error(y_test,Y_pred)**0.5: .2f}')

# new_pred = model.predict([[7]])[0]
# print(f'Student studying 7 hrs predicted marks:{new_pred:.1f}')

# #plot
# plt.figure(figsize=(9,5))
# plt.scatter(x,y,color = 'steelblue', s=100,alpha=0.8, label ='Actual')
# plt.plot(x,model.predict(x),color='red',linewidth=2, label='predicted line')
# plt.xlabel('study hours/day'); plt.ylabel('exam marks')
# plt.title('linear regression - study hour vs marks')
# plt.legend(); plt.grid(True,alpha=0.3); plt.show()


