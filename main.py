from Ai import Ai

ai = Ai()
print(ai.dialogue("你好"))

while True:
    print(ai.dialogue(input(":")))
