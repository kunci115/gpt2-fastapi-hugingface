import os

input_file = 'got.txt'
output_directory = 'data_chunks'
chunk_size = 1024

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read the input file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Calculate the number of chunks required
num_chunks = len(text) // chunk_size
if len(text) % chunk_size != 0:
    num_chunks += 1

# Split the text into chunks and save as individual files
for i in range(num_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    chunk = text[start:end]
    
    # Save the chunk to a file
    chunk_filename = os.path.join(output_directory, f'chunk_{i}.txt')
    with open(chunk_filename, 'w', encoding='utf-8') as file:
        file.write(chunk)

print(f'Successfully split the file into {num_chunks} chunks.')
