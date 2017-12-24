import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)

c = a*b

sess = tf.Session()
File_Writer = tf.summary.FileWriter('/home/arjun/Desktop/desktop111/DeepLearningCodes/TF2/graph', sess.graph)


print(sess.run(c))
sess.close() 