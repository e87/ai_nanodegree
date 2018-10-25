import time
from os import listdir


sum = 0

print("Starting the loop")
start_time = time.time()
for i in range(10000):
    sum += i

end_time = time.time()
print(start_time)
print(end_time)

print("The code took %s to complete" % (end_time - start_time))


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image
    files. Reads in pet filenames and extracts the pet image labels from the
    filenames and returns these label as petlabel_dic. This is used to check
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    # print(in_files)
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).

    # Creates empty dictionary for the labels
    petlabels_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
        # print('inside the loop {}'.format(in_files[idx][0]))
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if in_files[idx][0] != ".":

            # Creates temporary label variable to hold pet label name extracted
            pet_label = ""

            # TODO: 3. BELOW REPLACE pass with CODE that will process each
            #          filename in the in_files list to extract the dog breed
            #          name from the filename. Recall that each filename can be
            #          accessed by in_files[idx]. Be certain to place the
            #          extracted dog breed name in the variable pet_label
            #          that's created as an empty string ABOVE

            pet_label = in_files[idx].split('.')[0]
            pet_label = ''.join([i for i in pet_label if not i.isdigit()]).replace("_", " ").strip()
            print(pet_label)

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates
            # duplicate files (filenames)
            if in_files[idx] not in petlabels_dic:
                petlabels_dic[in_files[idx]] = pet_label

            else:
                print("Warning: Duplicate files exist in directory",
                      in_files[idx])

    # print(petlabels_dic)
    # returns dictionary of labels
    return petlabels_dic


for key, value in get_pet_labels('D:\\GitHub\\intro_to_python\\pet_images').items():
    print("File: {} ------- Label: {}".format(key, value))


s = 'Saint_bernard_08010'
result = ''.join([i for i in s if not i.isdigit()]).replace("_", " ")
print(result)