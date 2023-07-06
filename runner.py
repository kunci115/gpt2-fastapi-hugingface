
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

async def generate(prefix, max_length=800, top_k=5, model_dir='fine_tuned_model'):
    # Load the fine-tuned model and tokenizer
    model = GPT2LMHeadModel.from_pretrained(model_dir)
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)

    # Encode the prefix
    input_ids = tokenizer.encode(prefix, add_special_tokens=True, return_tensors='pt')

    # Generate text based on the prefix
    model.eval()
    model.config.pad_token_id = tokenizer.eos_token_id
    model.config.eos_token_id = tokenizer.eos_token_id
    model.config.vocab_size = model.config.vocab_size + len(tokenizer.get_added_vocab())
    model.resize_token_embeddings(len(tokenizer))
    # model, input_ids = model.to(torch.device("cuda")), input_ids.to(torch.device("cuda"))

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            top_k=top_k,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    # Decode and return the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text
