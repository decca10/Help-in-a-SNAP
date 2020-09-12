from sklearn.ensemble import RandomForestClassifier, VotingClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

import numpy as np


X_train = np.loadtxt('X_train.csv', delimiter=',')
y_train = np.loadtxt('y_train.csv', delimiter=',')
X_test = np.loadtxt('X_test.csv', delimiter=',')
y_test = np.loadtxt('y_test.csv', delimiter=',')

vote = vote = VotingClassifier([
    ('rf',RandomForestClassifier()),
    ('gb',GradientBoostingClassifier()),
    ('bag',BaggingClassifier())])

params={
    'rf__n_estimators':[10,100,1000],
    'rf__max_depth':[2,10,20,None],
    'rf__bootstrap':[True,False],
    'gb__subsample':[0.6,0.8,1.0],
    'gb__max_depth':[2,10,20,None],
    'bag__n_estimators':[10,100,1000]
}
gs = GridSearchCV(vote,param_grid=params)
gs.fit(X_train,y_train)
print(gs.best_score_)
gs.best_params_
