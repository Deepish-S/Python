import openai

# Define OpenAI API key
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
inpt = input("Enter your promt : ")
prompt = inpt

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

with open("response.txt", "w") as file:
    file.write(response)