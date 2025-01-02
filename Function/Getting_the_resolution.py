from pytubefix import YouTube
#The_resolution function is used to get the resolution of a video if we want to download it as video
#The resolution is look like 360p, 144p...
def The_resolution(url) : 
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True)
    #For .filte(progressive=True) it refers that the video and audio are included in a single file.
    resolution = [stream.resolution for stream in streams if stream.resolution]
    #Here, stream.resolution is get all the available rsolution from the video
    resolution = sorted(set(resolution),key= lambda x: int(x[:-1]), reverse=True )
    # Here I re-arange the list by for each stream(360pstr type)
    
    print(f"The available resolution: ")
    for a in resolution: 
        print(a)
    

    

