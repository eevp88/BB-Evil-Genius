import tweepyfrom subprocess import callfrom datetime import datetimefrom time import sleepimport subprocessimport Adafruit_BBIO.GPIO as GPIOGPIO.setup("P9_14", GPIO.IN)while True:    i = datetime.now()    now = i.strftime('%Y%m%d-%H%M%S')    GPIO.wait_for_edge("P9_14", GPIO.RISING)    kill = 'killall mjpg_streamer'    cmd = 'wget -O /root/frontdoor.jpg http://192.168.7.2:8090/?action=snapshot'    webcam = '/root/mjpg-streamer/mjpg_streamer -i "/root/mjpg-    streamer/input_uvc.so" -o "/root/mjpg-streamer/output_http.so -p 8090    -w ./www" &'call([webcam], shell=True)    sleep(5)    call ([cmd], shell=True)    consumer_key = 'xxxxxxxxxxxxx'    consumer_secret = 'xxxxxxxxxxxxxxx'    access_token = xxxxxxxxxxxxxxxxx'    access_token_secret = 'xxxxxxxxxxxxxxxxxx'    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    auth.set_access_token(access_token, access_token_secret) authentication    api = tweepy.API(auth)    photo_path = '/root/123.jpg'    status = 'BeagleBone Black door bell: ' + i.strftime('%Y/%m/%d %H:%M:%S    #beaglebone')    api.update_with_media(photo_path, status=status)    call ([kill], shell=True)