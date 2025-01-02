# This function is used to validate if the input directory is correct or exist.
#If it is exist, the function return the input path, if not it return the project path.
import os
def validate_directory(path): 
    if os.path.isdir(path):
        return str(path)
    else: 
       print("Invalid directory. Using project directory.") 
       return str(os.getcwd())