# PROBLEMS 11 to 15 — string functions
#
# Write each function so it RETURNS a value. Do not print inside them.
# Test with:  python3 week0/check.py


# PROBLEM 11: full_name(first, last)
# Returns both names capitalized with a space between.
#   full_name("maia", "rowe")     ->  "Maia Rowe"
#   full_name("ada", "lovelace")  ->  "Ada Lovelace"





# PROBLEM 12: last_word(sentence)
# Returns the last word of a sentence.
#   last_word("the quick brown fox")  ->  "fox"
#   last_word("hello world")          ->  "world"
#
# Hint: .split() gives you a list. A negative index counts from the end,
#       so list[-1] is the last item.





# PROBLEM 13: first_and_last(word)
# Returns the first and last character stuck together.
#   first_and_last("python")  ->  "pn"
#   first_and_last("maia")    ->  "ma"





# PROBLEM 14: username(email)
# Returns everything before the @ sign.
#   username("maia@example.com")  ->  "maia"
#   username("hello@gmail.com")   ->  "hello"
#
# Hint: .split() takes an argument telling it what to split on.





# PROBLEM 15: word_count(sentence)
# Returns how many words are in the sentence.
#   word_count("the quick brown fox")  ->  4
#   word_count("hello world")          ->  2
#
# Hint: len() tells you how many items are in a list.
