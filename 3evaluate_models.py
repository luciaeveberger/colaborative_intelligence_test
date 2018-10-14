# spot check for ES1
from numpy import mean
from numpy import std
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

prefix = "IndoorMovement/"
# load dataset
dataset = read_csv(prefix + 'es1.csv', header=None)
# split into inputs and outputs
values = dataset.values
X, y = values[:, :-1], values[:, -1]
# try a range of k values
all_scores, names = list(), list()
for k in range(1,22):
    scaler = StandardScaler()
    model = KNeighborsClassifier(n_neighbors=k)
    pipeline = Pipeline(steps=[('s',scaler), ('m',model)])
    names.append(str(k))
    scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=5, n_jobs=-1)
    all_scores.append(scores)
# summarize
m, s = mean(scores)*100, std(scores)*100
print('k=%d %.3f%% +/-%.3f' % (k, m, s))
# plot
pyplot.boxplot(all_scores, labels=names)
pyplot.show()