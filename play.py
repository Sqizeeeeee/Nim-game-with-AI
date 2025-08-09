from nim import train, play, save_ai, load_ai
import os

FILENAME = 'nim_ai.pkl'

if os.path.exists(FILENAME):
    print('Loading AI...')
    ai = load_ai(FILENAME)

else:
    print('Trainig AI')
    ai = train(10000000)
    save_ai(ai, FILENAME)

print('AI is ready to play!')
play(ai)
