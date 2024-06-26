from datetime import datetime

from Ai import Ai

ai = Ai()
print(f'{datetime.now()} {ai.dialogue("你好")}')

while True:
    content = input(":")
    if content == 'exit':
        break
    print(f'{datetime.now()} 提问：{content}')
    reply = ai.dialogue(content)
    print(f'{datetime.now()} {reply}')
