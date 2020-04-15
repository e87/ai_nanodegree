
def skip_elements(elements):
    """
    This function takes a list of elements and return a new list with every other elements from the original list

    Parameters:
        list of elements
    Return:
        New list with every other element in the elements list
    """

    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if elements.index(element) % 2 == 0:
            # Add this element to the resulting list
            new_list.insert(i, element)
        # Increment i
        i += 1

    return new_list


def skip_elements_enumerate(elements):
    """

    """
    new_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_list.insert(index, element)

    return new_list


def sum_divisors(n):
    """
    Returns the sum of all divisors of n, with n being exclusive
    """
    sum = 0
    # Return the sum of all divisors of n, not including n
    divisor = 1
    while divisor < n:
        if n % divisor == 0:
            sum += divisor
        divisor += 1

    return sum


def to_celsius(x):
    """
    Takes temperature in celsius and returns it converted to fahrenheit
    Parameter:
        Temperature in Celsius
    Return
        Temperature in fahrenheit
    """
    return (x - 32) * 5 / 9


def replace_domain(email, old_domain, new_domain):
    """
    Function that replace the domain on an email address
    Parameters
        :param email: valid email address
        :param old_domain: email address old domain
        :param new_domain: email address new domain
    Return
        email address with the new domain
    """
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    return False


def difference_bases_number(number):
    print()
    print("{:*^38}".format("Base Table"))
    for num in range(1, number +1):
        # print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(num))
        print("int: {0:>3d};".format(num),  "hex: {0:>3x};".format(num), "oct: {0:>3o};".format(num), "bin: {0:>3b}".format(num))


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


def double_word(word):
    double_word = word * 2
    return double_word + str(len(double_word))


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


def convert_seconds(seconds):
    """
    Returns the hours, minutes and remaining seconds
    :param seconds: number of seconds to convert to hours, minutes and remaining seconds
    :return: Tuple with hours, minutes and remaining seconds
    """
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


def file_size(file_info):
    file_name, file_type, file_size = file_info
    return "{:.2f}".format(file_size / 1024)


def full_namne(people):
    """
    Takes a list of tuple with name and email and returns a string with the name and email inside angle brackets

    Return
        string of name and email
    """
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))

    return result


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for permission in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if permission >= value:
                result += letter
                permission -= value
            else:
                result += "-"
    return result


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        words[words.index(word)] = word[1:] + word[0:1] + "ay"

    # Turn the list back into a phrase

    say = " ".join(words)
    return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"