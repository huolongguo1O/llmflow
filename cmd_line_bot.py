from __init__ import *
llm = llms.LLM_GLM4()
llmf = LLMFlow(llm=llm, prompt=[prompts.core.build(prompts.basic_prompt.assistant, assistant_name="LLMFlow")],debug=True)
while True:
    print("Assistant: "+str(llmf.run(input("User: "))))