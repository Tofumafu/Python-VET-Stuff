# So firstly, we need to get the user input 
sentence = input("Enter a word or sentence to translate to Pig Latin: ").lower()

# This would split the sentences into words
words = sentence.split()

# Store all words from input 
pig_latin_sentence = []

"""
These are the vowels, by using list
We can determined how each word should
Be translated based on its first letter
"""
vowels = ['a', 'e', 'i', 'o', 'u']

# Translate each word to Pig Latin
for word in words:
    if word[0] in vowels:
        # If the word starts with a vowel, add "yay" to the end!
        pig_latin_word = word + "yay"
    else:
        # If the word starts with a consonant, move the first letter to the end and add "ay"!
        pig_latin_word = word[1:] + word[0] + "ay"
    
    # Add the translated word to the sentence list
    pig_latin_sentence.append(pig_latin_word)

# Join the translated words into a sentence, into a single line
translated_sentence = " ".join(pig_latin_sentence)

# Display the translated word/sentence 
print("Pig Latin:", translated_sentence)