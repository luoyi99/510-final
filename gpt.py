import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

# Define the prompt to be sent to the OpenAI API
system_prompt = ("Imagine you are a content classification expert, able to categorize any content and summarize it. "
          "Based on the text content, generate three tags for me. Don't include any other content, just give me the "
          "tags themselves, seperated by comma.")


def get_tags(web_content):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Specify the model to use
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": web_content}
    ],
    max_tokens=950,  # The maximum number of tokens to generate
    temperature=0.5,  # Controls randomness. Closer to 0 makes the output more deterministic
    top_p=1.0,  # Nucleus sampling: top p% of the likelihood distribution are considered for sampling
    frequency_penalty=0.0,  # Discourages repetition of tokens based on their frequency in the text so far
    presence_penalty=0.0  # Discourages repetition of entire tokens regardless of their frequency
)
    response = response.choices[0].message.content
    tags = [t.strip() for t in response.split(',')]

    return tags
