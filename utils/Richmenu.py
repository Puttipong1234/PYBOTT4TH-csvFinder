richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": ">แถบช่วยเหลือ<",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 10,
        "width": 1647,
        "height": 814
      },
      "action": {
        "type": "message",
        "text": "สนใจคอสเรียน"
      }
    },
    {
      "bounds": {
        "x": 0,
        "y": 866,
        "width": 833,
        "height": 794
      },
      "action": {
        "type": "message",
        "text": "สนใจหนังสือ"
      }
    },
    {
      "bounds": {
        "x": 853,
        "y": 846,
        "width": 794,
        "height": 814
      },
      "action": {
        "type": "message",
        "text": "สนใจโปรแกรม"
      }
    },
    {
      "bounds": {
        "x": 1686,
        "y": 856,
        "width": 775,
        "height": 795
      },
      "action": {
        "type": "uri",
        "uri": "http://line.me/R/ti/p/@sketchuphome"
      }
    },
    {
      "bounds": {
        "x": 1686,
        "y": 10,
        "width": 795,
        "height": 814
      },
      "action": {
        "type": "message",
        "text": "ชำระเงิน"
      }
    }
  ]
}


channel_access_token = 'dAEAi3ozHbHyB5HSdaiiUPpJZAW5StlulXEE3Wuj56CqCeL7XXoZvRhmJ3sQCERmsMrQiLigwt1/YRG+CVOipwqMl//Zy1O7hl1m640lpFtlRKz01rQBpw22OubLFQakDs2Xy25jO6SfDi86ss6i7AdB04t89/1O/w1cDnyilFU='

import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())



CreateRichMenu(ImageFilePath='skphome_richmenu.png',Rich_json=richdata,channel_access_token=channel_access_token)


