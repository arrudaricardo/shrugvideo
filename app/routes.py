from app import app
from flask import render_template, request, jsonify
import pafy
import os
import json
from datetime import datetime
from app import db
from app.models import User, Video, UserVideoLink
from datetime import datetime
from random import randint
import re


def get_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr).split(',')[0]


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/postVideoId', methods=['POST'])
def postVideoId():

    video_id = request.form['videoid']
    msg = request.form['msg-txt']
    ip = str(get_ip())

    try:
        video = pafy.new(video_id)
    except (OSError, ValueError) as e:
        return jsonify(result='404', error=e)



    post = Video(videoId=video.videoid, length=video.length // 60, message=msg, title=video.title, timestamp=datetime.utcnow()) # add a Post db obj

    # check for user in db
    user = User.query.filter_by(ip=ip).first()

    if user == None or user.ip != ip: #if user do not exist
        new_user = User(ip=ip)

        db.session.add(new_user)
        new_user.videos.append(post)

    else: #user already exist in db
        user.videos.append(post)

    db.session.commit()


    return jsonify(result='saved successfully')


@app.route('/getVideoId', methods=['POST'])
def getVideoId():  # send last video posted
    ip = str(get_ip())
    user = User.query.filter_by(ip=ip).first()


    if user == None or user.ip != ip: # if user(ip) dont existed in db
        print('new user creation')

        # last video posted with len < 5.
        video = Video.query.filter(Video.length <= 5).order_by(Video.timestamp.desc()).first()

        new_user = User(ip=ip) # create a new user

        new_user.queue_video_id = video.id
        db.session.add(new_user)
        db.session.commit()
        return jsonify(result=video.videoId, msg=video.message)

    else:  # if user(ip) exist in db

        if user.queue_video_id != None:  # if user has video in queue return same video
            video = Video.query.filter(Video.id == user.queue_video_id).first()
            return jsonify(result=video.videoId, msg=video.message)

        else: #existed user with no video in queue

            # get last video <5 min that the user hasn't seen
            video = db.session.query(Video).filter(~Video.users.any(Video.id.in_([x.id for x in user.videos]))).filter(Video.length < 5).order_by(Video.timestamp.desc()).first()

            if video == None:  #user has no video <5min to see

                #get the shortest video >5 min that the user hasnt seen.
                video = db.session.query(Video).filter(~Video.users.any(Video.id.in_([x.id for x in user.videos]))).order_by(Video.length).first()
                if video == None: #user has no video to see
                    return jsonify(result='404') #
                else:
                    user.queue_video_id = video.id
                    db.session.commit()
                    return jsonify(result=video.videoId, msg=video.message)

            else: #user has videos <5min to see.
                user.queue_video_id = video.id
                db.session.commit()
                return jsonify(result=video.videoId, msg=video.message)




@app.route('/finishVideo', methods=['POST'])
def finishVideo():  # when user finish the video, remove from User.queue_video_id
    ip = str(get_ip())
    user = User.query.filter_by(ip=ip).first()

    video_id = request.form['videoId']
    video = Video.query.filter(Video.videoId == video_id).first()

    user.queue_video_id = None # clean video in queue

    #save into db as seen
    user.videos.append(video)
    db.session.commit()
    return jsonify(response='Remove queue for ip {}'.format(user.ip))
