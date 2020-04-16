def email_list(domains):
    emails = []
    for email, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, email))
    return (emails)


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))



def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"]}))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)


def add_prices(basket):
    """
        Returns the total price of all of the groceries in the dictionary.
        :param basket: dictionary
        :return: float number to two decimal point
    """
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for key, value in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += value
    # Limit the return value to 2 decimal places
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44


address = "1001 1st Ave"
number, street = address.split(" ", 1)
print(number)
print(street)
for word in address.split():
    print(word)

# see list comprehension for an different version
def highlight_word(sentence, word):
    new_sentence = []
    for w in sentence.split():
        if w == word:
            new_sentence.append(w.upper())
        else:
            new_sentence.append(w)
    return " ".join(new_sentence)



print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))



Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

total_guests = Taylors_guests.update(Rorys_guests)
print(Taylors_guests)