import os
import openai


openai.api_key = "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"




gpt_prompt = "Generate a large and detailed story for a video game:\n\nA ninja in Japan whose parents died when he was a child. "


response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=gpt_prompt,
  temperature=0.4,
  max_tokens=1000,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

firstResponse = response['choices'][0]['text']

print(firstResponse)
# print("#############################")
second_prompt = gpt_prompt + firstResponse + "\nGive a more detailed story than the one you created above: "
# print(second_prompt)
# print("#############################")

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=second_prompt,
  temperature=0.4,
  max_tokens=2000,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print("Second")
print(response)
