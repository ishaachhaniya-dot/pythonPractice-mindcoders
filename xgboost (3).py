# from xgboost import XGBClassifier
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import pandas as pd

# data= load_breast_cancer()
# X =pd.DataFrame(data.data, columns=data.feature_names)
# Y= data.target


# X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2 ,random_state=42)

# xgb= XGBClassifier(n_estimators=100,max_depth=4,learning_rate=0.1,random_state=42,eval_matric="logloss",verbosity=0)
# xgb.fit(X_train,Y_train)

# print(f'XGBoost Accuracy : {accuracy_score(Y_test,xgb.predict(X_test))*100:.2f}')




# import numpy as np
# def sigmoid(x): return 1/(1+np.exp(-x))
# def sigmoid_d(x): return x *(1-x)

# #XOR problem - a simple neural net test
# x=np.array([[0,0],[0,1],[1,0],[1,1]])
# y = np.array([[0],[1],[1],[0]])

# np.random.seed(42)
# W1=np.random.randn(2,4)* 0.5#input hidden weights
# W2=np.random.randn(4,1)*0.5 #hidden output weights

# lr=0.5
# losses=[]
# for epoch in range(10000):
#     #forward pass
#     h=sigmoid(x @ W1)
#     o=sigmoid(h @ W2)

#     #loss (mean squared error)
#     loss=np.mean((y-o)**2)
#     losses.append(loss)

#     #backward pass-comute gradient
#     d_o=(o-y)*sigmoid_d(o)
#     d_h=(d_o@ W2.T)*sigmoid_d(h)

#     #update wieghts
#     W2-=lr *h.T@ d_o
#     W1-=lr*x.T @ d_h

# import matplotlib.pyplot as plt
# plt.plot(losses);plt.title('loss decreasing durng training')
# plt.xlabel('epoch');plt.ylabel('loss');plt.show()

# print('final predictiond(should decreasing during training)')
# print(np.round(0,2))

# import tensorflow as tf
# from tensorflow import keras
# import numpy as np 
# import matplotlib.pyplot as plt

# #load MNIST: 70,000 handwritten digit images(28*28 pixels,grayscale)
# (X_train ,y_train),(X_test,y_test)=keras.datasets.mnist.load_data()
# print(f'Training: {X_train.shape}|test:{X_test.shape}')

# #visualise samples
# plt.figure(figsize=(12,2))
# for i in range(12):
#     plt.subplot(1,12,i+1)
#     plt.imshow(X_train[i],cmap='gray');plt.axis('off')
#     plt.title(str(y_train[i]),fontsize=8)
# plt.subtitle('sample MNIST digits');plt.show()

# #normalise: 0-255 -> 0-1(faster training,better convergence)
# X_train=X_train/255.0
# X_test=X_test/255.0

# #flatten 28828 -> 784(1D vector)
# X_train= X_train.reshape(-1,784)
# X_test=X_test.reshape(-1,784)                                                                                                                          

# #build neural network
# model=keras.Sequential([
#     keras.layers.Dense(512,activation='relu',input_shape=(784,)),
#     keras.layers.Droupout(0.2),
#     keras.layers.Dense(256,activation='relu'),
#     keras.layers.Dropout(0.2),
#     keras.layers.Dense(10,activation='softmax')
# ])

# model.summary()

# model.compile(
#     optimizer='adam',
#     loss='sparse_categorial_crossentropy',
#     metrics-['accuracy']
# )
# #Train the model
# history=model.fit(
#     X_train,y_train,
#     epochs=10,
#     batch_size=128,
#     validation_split=0.1,
#     callbacks=[keras.callbacks.EarlyStopping(patience=3,restore_best_)]
# )

# #Evaluate
# test_loss,test_acc=model.evaluate(X_test,y_test,verbose=0)
# print(f'Test Accuracy:{test_acc*100:.2f}%')

# #plot training history
# fig,axes=plt.subplots(1,2,figsize=(12,4))
# axes[0].plot(history.history['accuracy'],  label='Train')
# axes[0].plot(history.history['val_accuracy'],  label='validation')
# axes[0].set_title('Accuracy');axes[0].legend()
# axes[1].plot(history.history['loss'],   label='train')
# axes[1].plot(history.history['val_loss'],label='validation')
# axes[1].set_title('loss');axes[1].legend()
# plt.tight_layout();plt.show()

# #see predictions on test images
# predictions=model.predict(X_test[:15])
# pred_classes= np.argmax(predictions,axis=1)

# plt.figure(figsize=(15,3))
# for i in range(15):
#     plt.subplot(1,15,i+1)
#     plt.imshow(X_test[i].reshape(28,28),cmap='gray')
#     correct=pred_classes[i]==y_test[i]
#     plt.title(str(pred_classses[i]),color='green if correct else 'red',fontsize=8)
#     plt.axis('off')
# plt.subtitle('green=correct  Red=wrong');plt.show()
