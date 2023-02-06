from pytube import *

# Playlist object is a container for many youtube objects
playlist = Playlist(input('Please enter the url  : '))


# if the url is not playlist url then it will throw

# an error when trying to use its functionality
# so basically we cant check if the corresponding type is

# rightly casted until we try to run the 'funcs' of a certain object

forbidden_symb = ['#','%','&','{','}','\\','$','!',"'",
                  '"',':','@','>','<','*','?','/',' ','+','`','|','=']

chosen_stream = None


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
    chosen_stream.download('myDownloads\\',filename=f" - [{vtitle}].mp4",filename_prefix=f'{playlist.title} - {index}-{playlist.length}')







# print(playlist)
# def get_highest_res_stream(temp):
#     pass
