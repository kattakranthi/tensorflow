import tensorflow as tf

# Define two tensors
a = tf.constant(2)
b = tf.constant(3)

# Add tensors
c = tf.add(a, b)

# Run the computation
print("Result of addition:", c.numpy())

# Check TensorFlow version
print("TensorFlow version:", tf.__version__)

# Check GPU availability
if tf.config.list_physical_devices('GPU'):
    print("GPU is available:", tf.config.list_physical_devices('GPU'))
else:
    print("GPU is not available.")

matrix = tf.constant([[1, 2], [3, 4]])  # Matrix tensor

# Operations on tensors
result = tf.add(matrix, matrix)
print("Tensor operations result:\n", result)
