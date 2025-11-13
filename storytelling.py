from transformers import pipeline

# Load pre-trained text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Create initial prompt
prompt = "It was a dark and stormy night."

# Initialize story string
story = ""

for _ in range(5): 
    continuation = generator(prompt, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id)
   
    # Add the generated text to the story
    story += " " + continuation[0]['generated_text']
    
    # Use last sentence as the next prompt
    prompt = continuation[0]['generated_text'].split('.')[-2]

print("Generated Story:\n")
print(story)