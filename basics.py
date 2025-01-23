import tensorflow as tf

# Define two tensors
a = tf.constant(2)
b = tf.constant(3)

# Add tensors
c = tf.add(a, b)

# Run the computation
print("Result of addition:", c.numpy())

