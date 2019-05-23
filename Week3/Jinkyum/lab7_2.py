# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

def min_max_scaler(data):
    n=data-np.min(data,0)
    d=np.max(data,0)-np.min(data,0)
    return n/(d+1e-7)

xy = np.array([[828.659973, 833.450012, 908100, 828.349976, 831.659973],
               [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
               [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
               [816, 820.958984, 1008100, 815.48999, 819.23999],
               [819.359985, 823, 1188100, 818.469971, 818.97998],
               [819, 823, 1198100, 816, 820.450012],
               [811.700012, 815.25, 1098100, 809.780029, 813.669983],
               [809.51001, 816.659973, 1398100, 804.539978, 809.559998]])

    
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

xy2=min_max_scaler(xy)
x_data2 = xy2[:, 0:-1]
y_data2 = xy2[:, [-1]]

X=tf.placeholder(tf.float32,[None,4])
Y=tf.placeholder(tf.float32,[None,1])

W=tf.Variable(tf.random_normal([4,1]),name="weight")
b=tf.Variable(tf.random_normal([1]),name="bias")

h=tf.matmul(X,W)+b
cost=tf.reduce_mean(tf.square(h-Y))

optimizer=tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(101):
    cost_val, hy_val,_=sess.run([cost, h,train],feed_dict={X:x_data,Y:y_data})
    print(step, "Cost:", cost_val, "\nPrediction:\n",hy_val)

sess.run(tf.global_variables_initializer())
for step in range(101):
    cost_val, hy_val,_=sess.run([cost, h,train],feed_dict={X:x_data2,Y:y_data2})
    print(step, "Cost:", cost_val, "\nPrediction:\n",hy_val)