def double_word(word):
    doubleword = word * 2
    return doubleword + str(len(doubleword))


print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


# String Indexing
name = "James"
print(name[1])
print(len(name))


def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


# String Slice. Upper bound value is not included in the range.
color = "Orange"
sub_string = color[1:4]
print(sub_string)

# To create a new string use string slicing or assign the new string to the old one
# Index Method. We get a value error if you pass a value that is not found on the string
print("Index function")
pets = "Cats & Dogsc"
print(pets.index("&"))
pets.index("C")

# this will throw an error
# pets.index("x")

# Use the Keyword in to check if a word or character is in a string
print("Cats" in pets)
print("Dragons" in pets)


print("")


# Function that replace the domain on an email address
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


print(replace_domain("jsanc@hez@hdhwine.com", "hdhwine.com", "gmail.com"))