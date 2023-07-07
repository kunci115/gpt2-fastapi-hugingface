import os
import re
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def pre_process_data(text):
    "Do the preprocess for data's"
    # with open(input_file, 'r', encoding='utf-8') as file:
    #     text = file.read()
    # Perform any necessary pre-processing steps on the text
    text = text.replace("\n", " ")
    text = re.sub(r'[^\w\s]', '', text)
    # Return the pre-processed text
    return text

def fine_tune_model(training_text, model_name='gpt2', output_dir='fine_tuned_model'):
    """Fine tuning from pretained gpt2 model"""
    # Load pre-trained GPT-2 model
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    # Tokenize and encode the training text
    input_ids = tokenizer.encode(training_text, add_special_tokens=True, return_tensors='pt')
    # Fine-tune the model
    model.train()
    model.config.pad_token_id = tokenizer.eos_token_id
    model.config.eos_token_id = tokenizer.eos_token_id
    model.config.vocab_size = model.config.vocab_size + len(tokenizer.get_added_vocab())
    model.resize_token_embeddings(len(tokenizer))
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
    for _ in range(1):
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Save the fine-tuned model
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

OUTPUT_DIRECTORY = 'data_chunks'

# Get the list of chunked files
chunk_files = [filename for filename in os.listdir(OUTPUT_DIRECTORY) if filename.endswith('.txt')]

# Pre-process the training data
# training_text = pre_process_data('data_chunks/chunk_5.txt')
# Process each chunked file
COUNTER = 0
for chunk_file in chunk_files:
    # print(chunk_file)
    chunk_file_path = os.path.join(OUTPUT_DIRECTORY, chunk_file)
    COUNTER += 1
    # # Read the chunked file
    with open(chunk_file_path, 'r', encoding='utf-8') as file:
        chunk_text = file.read()
    # Preprocess the chunked text
        preprocessed_text = pre_process_data(chunk_text)
    # Fine-tune the model
        fine_tune_model(preprocessed_text)
        print(COUNTER)
