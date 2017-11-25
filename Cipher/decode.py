import sys
import collections


def find_key(text):
    key = collections.Counter(text).most_common(1)[0][0]
    return ord(key) - ord(' ')


def shift_character(c, n):
    return chr(ord(c) + n)


def decode_text(text, key):
    return "".join([shift_character(c, -key) for c in text])


def decode_file(cipher_file, message_file):
    with open(cipher_file, 'r') as file:
        cipher_text = file.read()

    key = find_key(cipher_text)
    message = decode_text(cipher_text, key)

    with open(message_file, 'w') as file:
        file.write(message)


decode_file(sys.argv[1], sys.argv[2])