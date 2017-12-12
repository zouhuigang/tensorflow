import tensorflow as tf
a = tf.constant('hello world')
sess=tf.Session()
print(sess.run(a))
