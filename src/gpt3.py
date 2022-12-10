import os
import openai


openai.api_key = "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"




gpt_prompt = "Generate a large and detailed story for a video game:\n\nA ninja in Japan whose parents died when he was a child."


response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=gpt_prompt,
  temperature=0.4,
  max_tokens=1000,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]['text'])

# second_prompt = "Can you make the story more detailed?"

# response = openai.Completion.create(
#   engine="text-davinci-003",
#   prompt=second_prompt,
#   temperature=0.4,
#   max_tokens=2000,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )

# print("Second\n")
# print(response['choices'][0]['text'])

# prediction_table.add_data(gpt_prompt,response['choices'][0]['text'])
