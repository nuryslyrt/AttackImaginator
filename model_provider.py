from ollama import Client

class ModelProvider:
    def __init__(self, model, system_prompt, user_prompt, assistant_prompt):
        self.model = model
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.assistant_prompt = assistant_prompt
        
    def ollama(self):
        client = Client(host='http://localhost:11434')
        response = client.chat(model=self.model, options={"temperature":1.0}, messages=[
        {
            'role': 'system',
            'content': self.system_prompt
        },
        {
            'role': 'user',
            'content': self.user_prompt
        },
        {
            'role': 'assistant',
            'content': self.assistant_prompt
        },
        ])
        return(response['message']['content'])
