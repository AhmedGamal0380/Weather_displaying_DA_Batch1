
import sys
from Function.Check_for_path import validate_directory
from Function import URL_process
from Classes import Download_process

# First, I greet the user then ask the user to insert the url of a video from YouTube:
print("Welcome in this YouTube Video Downloader application")  
url= input("Paste your url you want to download it here: ")
choices , resolution_choice  = URL_process.url_input(url)
#The URL_process.url_input returns two arg which are:
#1- choices: which are str of "Audio", or "Video", or None if there is no specific input insert to choices.
#2- resolution_choice: this is a retyrn that is get by applying Function.Getting_the_resolution.The_resolution
# - in the URL_process.url_input function.

# If the (choices) has any of str "Audio" or "Video" the main job of this code will be applaied.
if choices == "Audio" or choices == "Video" :
    Ask_for_path_download = input("Specify Output Directory for Downloads(path/to/directory):").strip()
    afpd = validate_directory(Ask_for_path_download)
    #Here after I ask the user to determine the path to download, 
    # a path checker function (validate_directory)is used.
    print(f"\nThe path you entered is: {afpd} ")
    #Once every thing is right we can successful download the YouTube video/audio.
    download_begin = URL_process.ready_to_download(url,choices,afpd,resolution_choice)
else :
    #If the choices has None value we can exit the program.
    sys.exit(0)

######
# You can use this url to test the code : https://www.youtube.com/watch?v=B7yTChc7JR0