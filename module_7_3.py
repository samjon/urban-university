
import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for char in string.punctuation:
                        line = line.replace(char, '')
                        # Удаляем лишние пробелы
                    line = ' '.join(line.split())
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        positions = {}
        for name, words in all_words.items():
            if word.lower() in words:
                positions[name] = words.index(word.lower()) + 1
        return positions

    def count(self, word):
        all_words = self.get_all_words()
        counts = {}
        for name, words in all_words.items():
            counts[name] = words.count(word.lower())
        return counts

# Пример использования
finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))







