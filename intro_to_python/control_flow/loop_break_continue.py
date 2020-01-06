
# A loop will terminate immediately it if encounter a break keyword
# The break keyword work on both while and for loops
# Sometimes we want to skip an iteration of the loop. We achieve this with the continue keyword
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

for num in check_prime:
    # Search for factors, iterating from 2 to the number ifself
    for i in range(2, num):

        # number is not prime if module is 0
        if(num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break  # this is to prevent more checks being performed on the same number

        # check until we search for all possible numbers.
        if i == num -1:
            print("{} IS a prime number".format(num))

