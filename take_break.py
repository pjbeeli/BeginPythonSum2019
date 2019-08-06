"""
Set an alarm to take a break by playing a youtube video
"""


import webbrowser
import time


# controller = webbrowser.get()
# controller.open("http://www.youtube.com/watch?v=SMwZsFKIXa8&amp;feature=fvst")

#  https://www.youtube.com/watch?v=2LPn_wMf44Y

# import time
# help(time)

def main():
    """
    Test function
    :return:
    """
    video_address = "https://www.youtube.com/watch?v=2LPn_wMf44Y"
    # Delay "sleep"
    time.sleep(50*60)
    webbrowser.open(video_address)
    cnt = 1
    while cnt <8:
        time.sleep(60 * 60)
        webbrowser.open(video_address)
        cnt +=1
        print("It is time to take a break, is: ", time.ctime())


if __name__ == '__main__':
    main()
    exit(0)