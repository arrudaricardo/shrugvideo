import pafy
import json
import os
import random


def yt_check(videoId):
    """ return a tuple of float len of youtube videoid and title"""
    if len(videoId) != 11:
    	return ('404', None)
    try:
    	video = pafy.new(videoId)
    except OSError:
    	return ('404', None)

    duration = video.duration.split(':')
    # parse duration str to float
    h = int(duration[0]) * 60
    m = int(duration[1])
    s = int(duration[2]) // 60
    return ((h + m + s), (video.title))

def get_videoid():
    with open(os.path.join(os.getcwd(),'app', 'data', 'data.json'), 'r') as f:
        data = json.load(f)
        video_list = data['ID']
        
        return data['ID'][-1]


