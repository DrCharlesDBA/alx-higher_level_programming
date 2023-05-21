#!/usr/bin/python3
for lowercase_alphabet in [chr(i) for i in range(97, 123)]:
    if 'q' not in lowercase_alphabet and 'e' not in lowercase_alphabet:
            print("{}".format(lowercase_alphabet), end="")
