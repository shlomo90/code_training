import sys

dic_words = {}
total_words = ''
words = ['Do', 'you', 'verb', 'your', 'adjective', 'noun', 'adverb']
# aa = sys.stdin.readline()
dic_words['noun'] = raw_input('Enter a noun: ')
dic_words['verb'] = raw_input('Enter a verb: ')
dic_words['adjective'] = raw_input('Enter an adjective: ')
dic_words['adverb'] = raw_input('Enter an adverb: ')

for word in words:
    dic_data = dic_words.get(word)
    if (dic_data is None):
        total_words += word
    else:
        total_words += dic_data

    total_words += ' '

print(total_words)
