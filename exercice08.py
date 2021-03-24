from re import findall

def get_word_count(sentence):
       # Votre code ici
       return len(findall('\w+', sentence))

def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0
