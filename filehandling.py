# # <---------------------------------------------------------reading file--->

# file = open("filehandling.txt","r") 
# print(file.read())
# file.close()

# file = open("filehandling.txt","rb") 
# print(file.read())
# file.close()

# # <---------------------------------------------------------writing file--->

# file = open("filehandling.txt","w+")
# file.write("Helloo , Love u bacheeee .....")
# file.close()


# file = open("filehandling.txt", "a")

# file.write("Byeee , Hate u bacheeee .....")
# file.close()

# # <------------------------------------------------------with statement file--->

# with open("filehandling.txt", "r") as file:
#     data = file.read()
# print(data)


# #  <-------------------------------------------------------exceptional statement file--->

# try:
#     file = open("filehandling.txt", "r+t")
#     data = file.read()
#     print(data)
# finally:
#     file.close()

# # <-------------------------------------------------------creating new file--->

# file = open("newfile.txt", "x")

# file.write("This is a new file created using the x mode.")
# file.close()

# file = open("newfile.txt", "r")
# t = file.read()
# print(t)

# # <-------------------------------------------------------json file handling--->

# file = open("filehandling.json", "r")

# file.write('{"name": "abhi", "age": 21, "city": " amp"}')
# file.close()

# data = file.read()
# print(data)


# # <-------------------------------------------------------Delete--->

# import os
# if os.path.exists("newfile.txt"):
#     os.remove("newfile.txt")
# else:
#     print("File deleted successfully")


# import os
# os.remove("newfile.txt")


# import os
# os.rename('filehandling.json','jsonfile.json')


# import os
# os.rmdir('newfile.txt') #filenotfound error