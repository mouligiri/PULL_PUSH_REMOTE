
import re
string_surrounded_digit="9 is my birthday, year is 1998"
whitespace_word_string="   Mouli  " 
word_string="abc"
# Matches strings that start and end with a digit and have any characters in between
string_surrounded_by_digit_regexpression = re.search(r'^\d+.*\d+$', string_surrounded_digit)
# Matches strings that contain only whitespace or word characters
space_word_regexpression = re.search(r'^[\s\w]+$', whitespace_word_string)
# Matches strings that contain only non-whitespace characters
word_regexpression = re.search(r'^\S+$', word_string)


print("Start and End with digits string match: ", string_surrounded_by_digit_regexpression.group())
print("Whitespace or word string match: ",space_word_regexpression.group())
print("Word string match: ",word_regexpression.group() )
