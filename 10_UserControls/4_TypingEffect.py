import flet as ft
from TypeWriterEffectControl import TypeWriterControl

def main(page: ft.Page):
    page.title = "TypeWriter Effect"
    page.window_width=400
    page.window_height=500
    page.bgcolor='#333333'
    page.theme_mode='dark'
    page.window_center()
    page.scroll='always'
    page.update()

    some_text_to_type = """
    ChatGPT (Chat Generative Pre-trained Transformer) is a chatbot launched by OpenAI in November 2022.
    
    It is built on top of OpenAI's GPT-3 family of large language models, and is fine-tuned (an approach to transfer learning) with both supervised and reinforcement learning techniques.

    ChatGPT was launched as a prototype on November 30, 2022, and quickly garnered attention for its detailed responses and articulate answers across many domains of knowledge. Its uneven factual accuracy was identified as a significant drawback. Following the release of ChatGPT, OpenAI was valued at $29 billion."""

    page.add(TypeWriterControl(some_text_to_type))

ft.app(target=main, assets_dir='assets')