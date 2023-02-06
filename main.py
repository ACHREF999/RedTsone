from pytube import *

chosen_stream = None
forbidden_symb = ['#','%','&','{','}','\\','$','!',"'",
                      '"',':','@','>','<','*','?','/',' ','+','`','|','=']

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
