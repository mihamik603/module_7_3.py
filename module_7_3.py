import string


file_name = 'test_file.txt'

content = """It's a text for task.
Найти везде используйте его для самопроверки.
Успехов в решении задачи!
text text text"""


with open(file_name, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"Файл '{file_name}' был создан с содержимым.")


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
