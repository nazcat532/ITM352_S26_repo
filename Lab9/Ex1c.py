# Open the file names.txt and read its contents and print the number of names

file_object = open("names.txt")
contents = file_object.read()
contents_list = contents.splitlines()
print(contents)
file_object.close()