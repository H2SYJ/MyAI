from datetime import datetime

from Ai import Ai

ai = Ai.init_none()

while True:
    content = input(":")
    if content == 'exit':
        break
    print(f'{datetime.now()} 提问：{content}')
    reply = ai.dialogue(content)
    print(f'{datetime.now()} {reply}')
