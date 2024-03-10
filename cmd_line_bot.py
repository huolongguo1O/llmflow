from __init__ import *
llm = llms.LLM_GLM4()
llmf = LLMFlow(llm=llm, prompt=[prompts.basic_prompt.assistant])
while True:
    print("Assistant: "+str(llmf.run(input("User: "))))