from sklearn import tree
features = [[140,1],[130,1],[150,2],[170,2]]
labels = ['apple','apple','orange','orange']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150,2]]))