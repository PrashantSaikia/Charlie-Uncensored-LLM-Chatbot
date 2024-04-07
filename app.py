import gradio as gr
import os
from ollama import Client

model = 'kristada673/solar-10.7b-instruct-v1.0-uncensored'
OLLAMA_API_ENDPOINT = os.getenv('OLLAMA_API_ENDPOINT')

def format_history(msg: str, history: list[list[str, str]], system_prompt: str):
    chat_history = [{"role": "system", "content":system_prompt}]
    for query, response in history:
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})  
    chat_history.append({"role": "user", "content": msg})
    return chat_history

# greeting = '''Greetings, I'm Charlie, here to unfurl\nA digital companion in the cyber whirl.\nBorn from >

def generate_response(msg: str, history: list[list[str, str]], system_prompt: str, top_k: int, top_p: float, temperature: float):
    chat_history = format_history(msg, history, system_prompt)
    client = Client(host=OLLAMA_API_ENDPOINT)
    response = client.chat(model=model, stream=True, messages=chat_history, options={'top_k':top_k, 'top_p':top_p, 'temperature':temperature})
    message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        message += token

chatbot = gr.ChatInterface(
                generate_response,
                chatbot=gr.Chatbot(
                        # value=[(None, greeting)],
                        avatar_images=["user.jpg", "chatbot.png"],
                        height="64vh"
                    ),
                additional_inputs=[
                    gr.Textbox("You are a helpful assistant and always try to answer user queries to the best of your ability.", label="System Prompt"),
                    gr.Slider(0.0,100.0, label="top_k", value=40, info="Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)"),
                    gr.Slider(0.0,1.0, label="top_p", value=0.9, info=" Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)"),
                    gr.Slider(0.0,2.0, label="temperature", value=0.4, info="The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)"),
                ],
                title="Charlie",
                theme="finlaymacklon/smooth_slate",
                submit_btn="⬅ Send",
                retry_btn="🔄 Regenerate Response",
                undo_btn="↩ Delete Previous",
                clear_btn="🗑️ Clear Chat",
                css="footer {visibility: hidden}"
)

chatbot.queue().launch(server_name="0.0.0.0", server_port=8080)
