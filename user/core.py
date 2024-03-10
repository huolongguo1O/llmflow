import time
import config
class LLMFlow():
    def __init__(self, prompt, llm, debug=False):
        self.prompt = prompt
        self.llm = llm
        self.run_depth = 0
        self.debug = debug
        for i in self.prompt:
            self.llm.add_prompt(prompt=i)

    def run(self, text):
        assert self.run_depth < config.max_depth
        if text is not None:
            self.llm.add_user_message(text)
        ret = self.llm.generate_response()
        if self.debug:
            print(ret)
        if ret[0] == 502:
            time.sleep(1)
            self.run_depth += 1
            return self.run(None)
        if ret[0] == 200:
            return ret[1]
        ValueError("LLMFlow failed to generate a response with status code:" + str(ret[0]) + "\nReason: " + str(ret[1]))