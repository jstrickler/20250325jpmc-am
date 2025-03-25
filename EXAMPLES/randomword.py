import random

class RandomWord():
    def __init__(self):
        with open('../DATA/words.txt') as words_in:
            self._word_list = [w.rstrip() for w in words_in]

    def __call__(self):
        """
        Return one random word when the instance is called

        :return: A random word as a string.
        """
        return random.choice(self._word_list)

if __name__ == '__main__':
    w = RandomWord()
    for _ in range(10):
        print(w())
