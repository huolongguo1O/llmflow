import zhipuai
import config
class LLM_GLM4():
    def __init__(self):
        self.model = zhipuai.ZhipuAI(api_key=config.GLM4_API_KEY)
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
    
    def add_prompt(self, prompt):
        self.history.append({"role": "system", "content": prompt})
    
    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})

    def generate_response(self):
        try:
            response = self.model.chat.completions.create(
                model="glm-4",  # 填写需要调用的模型名称
                messages=self.history,
            )
            # print(response)
            self.add_history({"role": response.choices[0].message.role, "content": response.choices[0].message.content})
            return 200, response.choices[0].message.content
        except Exception as e:
            return 500, "模型调用失败: "+ str(e)
