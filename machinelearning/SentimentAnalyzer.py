
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Training data: product reveiws
reviews=[
    ('this product is absolutely amazing! highly recommend!', 1),
    ('great quality anf fast delivery. very happy!',1),
    ('Excellent value for money.works perfectly!',1),
    ('loved it! Will definitely buy.',1),
    ('total scam,Do not buy this product.',0),
    ('poor quality and very late delivery.',0),
    ('horible experience.never buying again.',0),
    ('very disappinted.not as described at all.',0),
    ('terrible quality.broke after two days.',0)
]
texts,labels=zip(*reviews)
vectorizer=TfidfVectorizer(ngram_range=(1,2),max_features=500)
X = vectorizer.fit_transform(texts)
y=list(labels)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

clf=LogisticRegression()
clf.fit(X_train,y_train)
print(f'accuracy: {accuracy_score(y_test,clf.predict(X_test))*100:.0f}%')

#test on new reviews
new=['this is a wonderful product! Totally worth it!',
     'very bad experience.quality is awful.',
     'average product. nothing special. ']

X_new=vectorizer.transform(new)
for review,pred,prob in zip(new,clf.predict(X_new),clf.predict_proba(X_new)):
    sentiment='postive' if pred==1 else 'Negative'
    confidence=max(prob)*100
    print(f'[{sentiment} {confidence:.0f}%] {review[:45]}...')
