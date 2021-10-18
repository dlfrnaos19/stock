import os
import json
import requests
with open(os.path.join(os.getcwd(),'info.json'),'r',encoding='utf-8') as f:
    info = json.load(f)
 
def post_message(text):
    token = info['slacktoken']
    channel = info['channel_name']
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

markdown_text = '''
This message is plain.
*This message is bold.*
`This message is code.`
_This message is italic._
~This message is strike.~
'''

attach_dict = [{
    'color'      :'#ff0000',
    'author_name':'INVESTAR',
    "author_link":'github.com/investar',
    'title'      :'오늘의 증시 KOSPI',
    'title_link' :'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
    'text'       :'2,326.13 △11.89 (+0.51%)',
    'image_url'  :'ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}]
