# string = "1234567"
string = "abcdefg"

print(string.isdigit())

# if string.isdigit():
#     print("String contains all numbers")
# else:
#     print("String doesn't contains all numbers")

phrase = "Ala ma kota"
number_of_words = len(phrase.split())
print(number_of_words)

letter = "a"
phrase = phrase.lower()
number_of_letter_in_phrase = phrase.count(letter)
print(number_of_letter_in_phrase)