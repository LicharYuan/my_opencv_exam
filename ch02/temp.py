import tensorflow as tf
a=tf.truncated_normal([5,30])
b,c=tf.split(a,[2,3])
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(a))
    print('-------------')
    print(sess.run(b))
    print('------------------')
    print(sess.run(c))
