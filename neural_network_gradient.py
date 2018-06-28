# Required Python Packages
# Download the MNIS dataset
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
 
# import tensorflow to the environment
import tensorflow as tf
 
# initializing parameters for the model
batch = 100
learning_rate = 0.001
training_epochs = 100
 
# creating placeholders
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])
 
# creating variables
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
 
# initializing the model
y = tf.nn.softmax(tf.matmul(x,W) + b)
 
# Defining Cost Function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
 
# Determining the accuracy of parameters
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
 
# Implementing Gradient Descent Algorithm
train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
 
# Initializing the session
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
 
# Creating batches of data for epochs
	for epoch in range(training_epochs):
		batch_count = int(mnist.train.num_examples / batch)
		for i in range(batch_count):
    			batch_x, batch_y = mnist.train.next_batch(batch)
 
# Executing the model
	print(sess.run([train_op], feed_dict={x: batch_x, y_: batch_y}))
 
# Print Accuracy of the model
	print("Epoch: ", epoch)
	print("Accuracy: ", accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
	print("Model Execution Complete")
