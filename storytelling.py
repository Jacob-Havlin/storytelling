from transformers import pipeline

# Load pre-trained text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Create initial prompt
prompt = input("What is your story prompt? ")

# Initialize story string
story = ""

while True:
    
    if prompt.lower() == "quit":
        break
   
    continuation = generator(prompt, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id)
   
    # Add the generated text to the story
    story += " " + continuation[0]['generated_text']
    print(story)
    
    # Use last sentence as the next prompt
    prompt_continue = input("Houw would you like to continue this? ")

print("Generated Story:\n")
print(story)