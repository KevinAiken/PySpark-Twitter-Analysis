from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import config

consumer_key = config.consumer_key

consumer_key_secret = config.consumer_key_secret

access_token = config.access_token

access_token_secret = config.access_token_secret

class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:

            msg = json.loads( data )
            print msg
            print  "single message:" + msg['text'].encode('utf-8')
            self.client_socket.send( msg['text'].encode('utf-8') )
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['trump'])

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "0.0.0.0"
port = 5555
s.bind((host, port))
s.listen(5)
c, addr = s.accept()
sendData(c)


