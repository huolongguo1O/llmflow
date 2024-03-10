from zhipuai import Zhipuai
from .. import config
class LLM_GLM4():
    def __init__(self):
        self.model = Zhipuai(API_KEY=config.GLM4_API_KEY)
        self.history = []
        self.tools=[]
        self.generate_config={}

    def clear_history(self):
        self.history = []

    def add_history(self, input):
        self.history.append(input)
    
    def get_history(self):
        return self.history
    
    def set_history(self, history):
        self.history = history

    def add_tool(self, tool):
        self.tools.append(tool)
        
    def generate(self):
        response = self.model.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=self.history,
        )
