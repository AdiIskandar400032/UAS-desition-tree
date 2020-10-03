from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['laki-laki', 'laki-laki', 'perempuan', 'laki-laki', 'laki-laki', 'laki-laki', 'perempuan', 'perempuan',
     'perempuan', 'laki-laki', 'laki-laki']



clf = clf.fit(X, Y)

prediction = clf.predict([[160, 60, 22]])

print(prediction)