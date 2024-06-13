from instagrapi import Client
import json

# cl = Client(json.load(open('./insta-login-setting.json')))
cl = Client()
cl.login('huynhdieuhoadc59361@fthcapital.com', '35hj5cAvXfuQ08b')

json.dump(
    cl.get_settings(),
    open('./insta-login-setting.json', 'w')
)
cl.photo_upload(
    "./test.jpg",
    "Cô gái xinh đẹp nhất quả đât"
)
