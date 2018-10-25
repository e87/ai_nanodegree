from typing import List

my_list = [1, 2, 3]  # type: List[int]

if my_list:
    print('list is not empty')

else:
    print('empty')


list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

for item in list_of_months:
    print(str(list_of_months.index(item) + 1) + "-" + item)


list_of_months_abbreviation = []

for item in list_of_months:
    list_of_months_abbreviation.append(item[:3])

for item in list_of_months_abbreviation:
    print(str(list_of_months_abbreviation.index(item) + 1) + "-" + item)


my_list = "boston".split(" ")
print(my_list)
if 'Terrier' in my_list:
    print("terrier is in the list")
else:
    print('No Terrier')