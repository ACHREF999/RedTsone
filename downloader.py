from pytube import *


chosen_stream = None

forbidden_symb = ['#','%','&','{','}','\\','$','!',"'",
                      '"',':','@','>','<','*','?','/',' ','+','`','|','=']





# TODO get text on `Download` Click [X]
# TODO paste text on `paste` Click [X]
# TODO check if valid url [X]
# note that the url validation is not even good i need to rework it
# but now it does half the trick

# TODO create new thread where you download the Stream[s] [X]

# So now i want to implement the list view and also make a wrapper arround the download function
# what it means is that init_download will start the thread of adding an item to the list of downloads and track the progress of the download
# init download :
#   create new Thread
#   add new item to the list
#   start the download


# so after i click download and validate the url i pass it to this function which handles
# downloading streams at my prefered resolution
# i would love to have a function that chooses the streams with the correct resolution
# and in here i just trigger the ` download ` API

def download_playlist(url,path):
    # so here in the playlist we are making a new folder for the playlist
    # and we are downloading each video in that folder
    #

    p = Playlist(url)

    if path and path[-1] == '/':

        path += p.title+'/'


    else :

        path += '/'+p.title+'/'


    for video in p.video_urls:

        download_video(video,path)


def get_stream(yt):
    stream = None

    # i dont need to put the '720p' here but we can get the stream directly in here

    if yt.streams.get_highest_resolution().resolution in ['144p', '240p', '360p', '480p','720p']:

        stream = yt.streams.get_highest_resolution()


    else:

        stream = yt.streams.filter(res='720p')



    return stream

def clean_title(title):

    new = title+' '

    new = new[:-1]

    # Not consumming the string to avoid unexpected behaviour


    for symb in forbidden_symb:

        new = title.replace(symb, "_")

    return new


def download_video(url,path):
    yt = YouTube(url)


    # print(f'streams of the video are : {yt.streams}')
    #filter through res

    stream = get_stream(yt)

    title = yt.title

    #clean the name

    title = clean_title(title)

    print(f'downloading {title} with a resolution of {stream.resolution}')

    stream.download(path, title)

    print('finished Downloading')


def download(url,path):


    if 'list' in url.lower():
        download_playlist(url,path)


    else :
        download_video(url,path)







if __name__ == '__main__':
    url = ""
    url = input('Please enter the url  : ')

    try:
        # Playlist object is a container for many youtube objects
        playlist = Playlist(url)


        # if the url is not playlist url then it will throw

        # an error when trying to use its functionality
        # so basically we cant check if the corresponding type is

        # rightly casted until we try to run the 'funcs' of a certain object


        # chosen_stream = None


        for index,video in enumerate(playlist.videos):
            temp = video.streams.get_highest_resolution()
            # print(temp)
            # print(temp.__dict__)
            if temp.resolution in ["1080p","2160p", "4320p", "1440p"]:
                print(temp.resolution)
                chosen_stream = video.streams.filter(res="720p").first()

                print('skipped to lesser')
                # continue
            else:
                chosen_stream = temp
                print('it was the highest res acceptable')
            # pass
            vtitle = video.title[:]
            for symbol in forbidden_symb:
                print(symbol,end=' ')
                vtitle = vtitle.replace(symbol,'_')
            print('\n '+vtitle)
            chosen_stream.download('myDownloads\\',filename=f" - [{vtitle}].mp4",filename_prefix=f'{playlist.title} - {index+1}-{playlist.length+1}')
    except:
        yt = YouTube(url)
        temp = yt.streams.get_highest_resolution()
        if temp.resolution in ["1080p", "2160p", "4320p", "1440p"]:
            chosen_stream = yt.streams.filter(res='720p').first()
            print('Skipped higher Resolutions')
        else :
            chosen_stream = temp

        vtitle = yt.title[:]
        for symbol in forbidden_symb:
            print(symbol, end=' ')
            vtitle = vtitle.replace(symbol, '_')
        print('\n ' + vtitle)

        chosen_stream.download('myDownloads\\',filename=f"Unrecognized [{vtitle}].mp4")

    finally:
        print('''
        
        
        
        ----------Finished-----------------
        
        
        
        
        ''')





# print(playlist)
# def get_highest_res_stream(temp):
#     pass
