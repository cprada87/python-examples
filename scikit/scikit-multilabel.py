from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = preprocessing.MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)