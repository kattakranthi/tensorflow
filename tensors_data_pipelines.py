# Creating a DataSet
import tensorflow as tf

# Create a dataset with a range of numbers
dataset = tf.data.Dataset.range(10)

# Print the elements of the dataset
for item in dataset:
    print(item.numpy())

# Apply transformations
dataset = dataset.map(lambda x: x * 2)  # Multiply each element by 2
dataset = dataset.filter(lambda x: x > 10)  # Keep elements greater than 10

# Print the transformed dataset
for item in dataset:
    print(item.numpy())

# Batch the data into groups of 3
dataset = dataset.batch(3)

# Print each batch
for batch in dataset:
    print(batch.numpy())

# Shuffle the dataset
dataset = dataset.shuffle(buffer_size=5)

# Print the shuffled dataset
for item in dataset:
    print(item.numpy())

# Create a text file
with open("data.txt", "w") as f:
    f.write("line 1\nline 2\nline 3\nline 4\n")

# Read the text file
dataset = tf.data.TextLineDataset("data.txt")

# Print the contents
for line in dataset:
    print(line.numpy().decode('utf-8'))
