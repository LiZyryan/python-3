import string
def create_hashtag(input_string):
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    words = input_string.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    return hashtag[:140]
user_input = input("Введіть рядок: ")
print(create_hashtag(user_input))
