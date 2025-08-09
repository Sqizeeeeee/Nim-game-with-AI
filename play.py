from nim import train, play, save_ai, load_ai
import os

FILENAME = 'nim_ai.pkl'

if os.path.exists(FILENAME):
    print('loading AI')
    ai = load_ai(FILENAME)
else:
    print('loading AI')
    ai = train(100000)
    save_ai(ai, FILENAME)

    
play(ai)
