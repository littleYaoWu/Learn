#https://www.jianshu.com/p/589ed0a8137d
# 2018/08/01


from keras.models import Sequential
from keras.layers import Dense
import numpy

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

#load dataset
dataset = numpy.loadtxt('indians-diabetes.csv', delimiter = ",")
X = dataset[:, 0:8]
Y = dataset[:, 8]

# model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit model
model.fit(X, Y, nb_epoch=150, batch_size=10)

# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


predictions = model.predict(X)
rounded = [round(x) for x in predictions]
print(rounded)
#TypeError: type numpy.ndarray doesn't define __round__ method?????????
