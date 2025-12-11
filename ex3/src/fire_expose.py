import fire
from utils import greet, goodbye

if __name__ == '__main__':
    fire.Fire({
        'greet': greet,
        'goodbye': goodbye
    })
