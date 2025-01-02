from pytubefix import YouTube
from pytubefix.cli import on_progress
from abc import ABC, abstractmethod


class Downloadable(ABC):
    def __init__(self,url,download_path,video_resolution = None):
        self.url = url #This is the link for the YouTube video
        self.download_path = download_path #This is the path that is obtained by applying Check_for_path function
        self.video_resolution = video_resolution #This is the resolution obtained by ask the user for the Resolution

        
    @abstractmethod
    def downloadav(self):
        pass
# An astract is used to handle inputs to Audio,Video classes
############################

# OCP is applied here to make the code more efficient for future expand
class Download_Process:  
    def download_audio_video(self,av_choice):
        av_choice.downloadav()
       
class Video(Downloadable) :
#The Video  inherit from downloadable to process the input 
    def downloadav(self):
        a_video = YouTube(self.url,on_progress_callback=on_progress)
        #The YouTube function prepare and get the video from youtube to apply the download process on it 
        #on_progress_callback=on_progress shows the progress of the download
        ready_to_download_vi = a_video.streams.get_by_resolution(self.video_resolution)
        #A stream is essentially a media file or a segment of a media file that can be processed, played, or downloaded. 
        # It can contain either video, audio, or both.
        ready_to_download_vi.download(output_path=self.download_path)     
        #output_path= is used to determine where we want the downloaded video to be saved in a specific directory

class Audio(Downloadable) :
    
    def downloadav(self):
        an_audieo = YouTube(self.url,on_progress_callback=on_progress)
        ready_to_download_au = an_audieo.streams.get_audio_only()
   
        ready_to_download_au.download(output_path=self.download_path)
 





 