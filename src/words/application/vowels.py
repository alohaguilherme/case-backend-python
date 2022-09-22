class Vowels:
    @staticmethod
    def count(word: str = None) -> int:
        vowels = [letter for letter in word if letter.lower()
                  in ('a', 'e', 'i', 'o', 'u')]
        return len(vowels)
