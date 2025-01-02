import pytubefix.streams
from .Getting_the_resolution import The_resolution
from pytubefix import YouTube
from Classes import Download_process
import time
import sys

def url_input(s_url):
# s_url is the input url.
# I defined the return variable that I need to return
  audio_video_choice = None
  Ask_for_the_required_resolution = None
  exiting = None

# I used the concept of try/exception to basically check if the given link is valid or not. 
  try: 
    #The audio_checker is just to check the available of the video before asking the user to insert Audio/Video
    #If the link is not valid the except condition is met
    audio_checker = YouTube(s_url)
    audio_checker.streams.get_audio_only()
    #The while is used for a condition when the user insert neither Audio nor Video,
    #  then the user will be asked if he wants to re-enter audio/video. If yes,
    #  the audio_video_choice will be executed again. If not, the program will be exited.
    while True :
      audio_video_choice = input("To download audio insert Audio:\nTo download video insert Video:\n").capitalize().strip()
     
      if audio_video_choice == "Video" :
       
      # This function is used to get the resolution of a Youtube video for example 144p or 720p.
       The_resolution(s_url)
      # Here the time.sleep is used to facilitate the selection process without haste.   
       time.sleep(1)
       print("\nFrom the above resolutions, insert the desired resolution to download, for example 360p ")
       Ask_for_the_required_resolution = input()
       break
      # If the procedures are correctly executed we can break the while process
     
      elif audio_video_choice == "Audio" :
        break

      else :
        print("Neither Video nor Audio is inserted")
        ask_the_user_to_continue = input("To re-enter Video/Audio inser 1, to exit the program insert any key:\n").strip()
        if ask_the_user_to_continue == "1":
          pass
        # Here where the procedures to ask the user to choose Audio/Video will happen again
        else :
          print("Exiting the program. Goodbye!") 
          exiting = 1
          break

  except :
      print("Insert a valid YouTue url!")
      exiting = 1
      audio_video_choice = None
  if exiting == 1:   
    sys.exit(0) 

  return audio_video_choice, Ask_for_the_required_resolution
# 1- In  case of valid url: 
# 1.a- If it was for a video (audio_video_choice) & (Ask_for_the_required_resolution) will return values.
# 1.b- If it was for an audio (audio_video_choice) will be return str Audio, but (Ask_for_the_required_resolution),
# will return None.
#2- In case of unvalid url it will return two arguments of None.

def ready_to_download(download_url,a_v,path,res = None):
  #a_v is the choices of Audio/Video that is getting from the main code
  #The main code implement the above (url_input) function to get the choices which will be used here
  if a_v == "Video":
    video = Download_process.Video(download_url,path,res)
    call_for_download_process = Download_process.Download_Process()
    call_for_download_process.download_audio_video(video)
    #for these code go to Classes.Download_process
  elif a_v == "Audio" :
    audio = Download_process.Audio(download_url,path)
    call_for_download_process = Download_process.Download_Process()
    call_for_download_process.download_audio_video(audio)


