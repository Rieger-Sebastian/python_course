"""
--> sentence, <-- reverse sentence
order the words in a sentence in reverse
"""
reversed_sentence = ''

sentence = str(input('please type in a sentence\n'))

sentence_list = sentence.split(' ')

for word in reversed(sentence_list):
    reversed_sentence += word + ' '


print(reversed_sentence)