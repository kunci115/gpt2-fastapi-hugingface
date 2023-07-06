import os

INPUT_FILE = 'got.txt'
OUTPUT_DIRECTORY = 'data_chunks'
CHUNK_SIZE = 1024

if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

# Read the input file
with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    text = file.read()

# Calculate the number of chunks required
num_chunks = len(text) // CHUNK_SIZE
if len(text) % CHUNK_SIZE != 0:
    num_chunks += 1

# Split the text into chunks and save as individual files
for i in range(num_chunks):
    start = i * CHUNK_SIZE
    end = (i + 1) * CHUNK_SIZE
    chunk = text[start:end]
    # Save the chunk to a file
    chunk_filename = os.path.join(OUTPUT_DIRECTORY, f'chunk_{i}.txt')
    with open(chunk_filename, 'w', encoding='utf-8') as file:
        file.write(chunk)

print(f'Successfully split the file into {num_chunks} chunks.')
