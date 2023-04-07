import requests

slack = 'xoxb-2287798136820-4424796531104-9XkDtmHBTlj5tXQ8mBo3eKKi'

class Slack():
    def post_message(token, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": text}
        )
        #print(response)

    #post_message(slack,"#message", "넣고 싶은 메세지")