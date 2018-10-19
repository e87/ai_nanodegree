import other_script
import useful_functions as uf

# To import a script, use the import keyword.
# Import statement are written at the top of a python file.
# You don't need to type out the file extension.

num_list = [1,2,3,4,5]
mean = uf.mean(num_list)  # you need to type the entire name of the module if you don't add an alias.

print(mean)

