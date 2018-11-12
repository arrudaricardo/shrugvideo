from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(40), index=True, unique=True)
    queue_video_id = db.Column(db.Integer)  # videos that user started to see but no finished 
    videos = db.relationship('Video', secondary='users_videos_link')  # videos that user has seen



class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    videoId = db.Column(db.String(11), index=True)
    message = db.Column(db.String(120))
    length = db.Column(db.Integer)
    title = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    users = db.relationship('User', secondary='users_videos_link')




class UserVideoLink(db.Model):  # video that user has seen
    __tablename__ = 'users_videos_link'
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), primary_key=True)






def init_db():
    db.create_all()  # create db
    # Create a test obj db
    new_ip = User(ip='000.000.000.000', queue_video_id=5)
    new_video = Video(videoId='JqvaQDDH3hQ', length=0, message="Cyclops Has No Friends", title='Cyclops Has No Friends')
    new_ip.videos.append(new_video)
    db.session.add(new_ip)

    new_ip1 = User(ip='000.000.000.001', queue_video_id=1)
    new_video1 = Video(videoId='cyK6cG5OIO0', length=0, message="I Cant Hear Myself Think", title='I Cant Hear Myself Think')
    new_ip1.videos.append(new_video1)
    db.session.add(new_ip1)

    new_ip2 = User(ip='000.000.000.002')
    new_video2 = Video(videoId='87vuh3YjtUs', length=0, message="Tequila Sundown", title='Tequila Sundown')
    new_ip2.videos.append(new_video2)
    db.session.add(new_ip2)

    new_ip3 = User(ip='000.000.000.003')
    new_video3 = Video(videoId='AcuCh7onaqw', length=0, message="Unstable Roommate", title='Unstable Roommate')
    new_ip3.videos.append(new_video3)
    db.session.add(new_ip3)

    new_ip4 = User(ip='000.000.000.004')
    new_video4 = Video(videoId='aVOxvj4beq8', length=0, message="Fuggedaboutit", title='Fuggedaboutit')
    new_ip4.videos.append(new_video4)
    db.session.add(new_ip4)

    new_ip5 = User(ip='000.000.000.005')
    new_video5 = Video(videoId='Vo1u3IIOmX4', length=0, message="Lets Go to the Aquarium!", title='Lets Go to the Aquarium!')
    new_ip5.videos.append(new_video5)
    db.session.add(new_ip5)

    new_ip6 = User(ip='000.000.000.006')
    new_video6 = Video(videoId='_nAzlxbyiwQ', length=0, message="The Reckoning of Cinco de Mayo", title='The Reckoning of Cinco de Mayo')
    new_ip6.videos.append(new_video6)
    db.session.add(new_ip6)

    new_ip7 = User(ip='000.000.000.007')
    new_video7 = Video(videoId='sPQz8hXUwT4', length=0, message="Old Draft", title='Old Draft')
    new_ip7.videos.append(new_video7)
    db.session.add(new_ip7)

    new_ip8 = User(ip='000.000.000.008')
    new_video8 = Video(videoId='5C6gDUcXCO0', length=0, message="Jeff Thompson Vs. the Wishgiver", title='Jeff Thompson Vs. the Wishgiver')
    new_ip8.videos.append(new_video8)
    db.session.add(new_ip8)

    new_ip9 = User(ip='000.000.000.009')
    new_video9 = Video(videoId='MhNrsUiL6bY', length=0, message="5SF BTS: Butter Boys", title='5SF BTS: Butter Boys')
    new_ip9.videos.append(new_video9)
    db.session.add(new_ip9)

    new_ip10 = User(ip='127.0.0.1', queue_video_id=1)
    new_video10 = Video(videoId='DhbmzGeG83w', length=0, message="Black Mirror S04E07", title='Black Mirror S04E07')
    new_ip10.videos.append(new_video10)
    db.session.add(new_ip10)



    db.session.commit()

def erase_db():
    a = input('Do you want to eresa and dele db (y/n)?')
    if a == 'y':

        db.reflect()
        db.drop_all()
