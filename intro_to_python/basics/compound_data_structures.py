
# Data structure that contains other data structures

elements = {'hydrogen':{'number': 1,
                        'weight': 1.00794,
                        'symbol': 'H'},
            'helium':{'number': 2,
                      'weight': 4.002602,
                      'symbol': 'He'}}

print(elements['hydrogen'])
print(elements.get('helium'))

# to print information from the nested dictionary, do the following
print(elements['hydrogen']['symbol'])
print(elements.get('hydrogen')['symbol'])

