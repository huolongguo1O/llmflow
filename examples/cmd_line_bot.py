from . import *
llm = LLMFlow(prompt=prompts.basic_prompt.assistant)
while True:
    print("Assistant: "+llm.run(input("User: ")))