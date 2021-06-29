import matplotlib.pyplot as plt #Explanatory modeling Box and Histogram

import pandas
from pandas.plotting import scatter_matrix #Scatter plot

from sklearn import model_selection
from sklearn.model_selection import train_test_split #splits the data

from sklearn.naive_bayes import GaussianNB 

from sklearn.metrics import accuracy_score
#NB for uncertainity reasoning

url="C:/Users/ambogholi/Documents/Test/wine.csv"
names = ['Wine', 'Alcohol', 'Malic.Acid', 'Ash', 'Acl'
         'Mg','Phenols','Flavanoid','Nonflavar','Proanth',
         'Color.int','Hue','OD','Proline']
dataset = pandas.read_csv(url,names=names)

print(dataset.shape)
print(dataset.head(5))
print(dataset)
print(dataset.describe())
print(dataset.groupby('Wine').size())

#visualization
dataset.plot(kind='box', subplots=True, layout=(2,7), sharex=False, sharey=False)
plt.show()

dataset.hist()
plt.show()


scatter_matrix(dataset)
plt.show()

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split\
    (X, Y, test_size=validation_size, random_state=seed)

print(" X_train",X_train)
print("X_test",X_test)
print("Y_train",Y_train)
print("Y_test",Y_test)


url="C:/Users/ambogholi/Documents/Test/wine_test.csv"
names = ['Wine','Alcohol', 'Malic.Acid', 'Ash', 'Acl'
         'Mg','Phenols','Flavanoid','Nonflavar','Proanth',
         'Color.int','Hue','OD','Proline']
dataset_test = pandas.read_csv(url,names=names)

array = dataset_test.values
X_new_test= array[:,0:4]


print("X_new_test",X_new_test)

model = GaussianNB()
model = model.fit(X_train ,Y_train)
y_predicted = model.predict(X_new_test)
print("predicted",y_predicted)

print(accuracy_score(Y_test,y_predicted))