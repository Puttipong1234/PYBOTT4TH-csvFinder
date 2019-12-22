import os
import glob
from utils.csvFinder import csvFinder
from utils.dialogflow_uncle import detect_intent_texts
from utils.reply import reply_msg , SetMessage_Object

from msgflex.flex import *

from flask import Flask, request, abort

app = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_storage_path = os.path.join(base_dir,"CSVs")
csv_files = [f for f in os.listdir(csv_storage_path) if f.endswith('.csv')]

db = {}

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

channel_access_token = 'NuHb+ux87r03IsI2k9uC0t9s1X+ViaLXMx21PG58kHoWXfABptstIpxx50elygjAXAJS40qiCp+Bi5/uaRf3GzXzavRFCDIifowRNLkfaiPTj0D5zh/cgsStl6xPFOF/s4rGxS+sjhrBrbWeBUt/7QdB04t89/1O/w1cDnyilFU='
channel_secret = '065a7ee19337d9a7592557718cf62584'

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    text_from_user = event.message.text #ข้อความจากยูศเซอ
    reply_token = event.reply_token #รีพลายโทเคน
    userid = event.source.user_id #ยูซเซอไอดี

    result_from_dialogflow = detect_intent_texts(project_id="axial-device-255804",
                                        session_id=userid ,
                                        text=text_from_user , 
                                        language_code="th")
    
    action = result_from_dialogflow["action"]
    response = result_from_dialogflow["fulfillment_messages"] #as list
    
    print("action : " + action)
    print("response : " + str(response))

    if userid not in db.keys():
        db[userid] = {
            "keyword" : None,
            "Column" : None
        }

    if action == "FIND_ROW":
        # 1. ตอบกลับไป กรุณาใส่ตีเวิด
        all_text = []
        for each in response:
            text = TextSendMessage(text=each)
            all_text.append(text)
        
        line_bot_api.reply_message(reply_token,messages=all_text) #reply messageกลับไป

        return 'OK'
    
    elif action == "FIND_ROW_RESULT":

        db[userid]["value"] = text_from_user  #เก็บข้อมูล

        CSV = csvFinder(csvPath="./CSVs/รายการบ้านสองชั้น.csv")
        search_result = CSV.find_row(val=text_from_user,limit=10) ##search result => list[dict]

        all_bubbles = []
        for each in search_result:
            แถวที่พบ = each["true_row"]
            คำที่ค้นหา = text_from_user
            คะแนนความเที่ยงตรง = each["score"]
            คอลัมน์ที่ค้นพบคำนี้ = each["col_name"]

            รายการที่ค้นพบ = each["result"]  #dictionary

            bubble = flex_find_row(แถวที่พบ,คำที่ค้นหา,คะแนนความเที่ยงตรง,คอลัมน์ที่ค้นพบคำนี้,รายการที่ค้นพบ)
            all_bubbles.append(bubble)

        flex_to_reply = make_carousel(all_bubble = all_bubbles)

        flex_to_reply = SetMessage_Object(flex_to_reply)
        reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)

        return 'OK'
    
    elif action == "FIND_VALUE":
        # 1. ตอบกลับไป กรุณาใส่ตีเวิด
        all_text = []
        for each in response:
            text = TextSendMessage(text=each)
            all_text.append(text)
        
        line_bot_api.reply_message(reply_token,messages=all_text) #reply messageกลับไป

        return 'OK'
    
    elif action == "FIND_VALUE_GET_COLUMN":

        all_text = []
        for each in response:
            text = TextSendMessage(text=each)
            all_text.append(text)

        line_bot_api.reply_message(reply_token,messages=all_text) #reply messageกลับไป

        return 'OK'
    
    elif action == "FIND_VALUE_GET_COLUMN_RESULT":

        col_to_find = response[0] ## dialogflow บอกว่า user ต้องการค้นหา column ไหน

        CSV = csvFinder(csvPath="./CSVs/รายการบ้านสองชั้น.csv")
        search_result = CSV.find_value(val=text_from_user,col_to_find=col_to_find,limit=10) #ค้นหา

        results = [i["result"] for i in search_result]

        flex = flex_find_value(คำที่ค้นหา=text_from_user,results=results)
        print(flex)
        flex_to_reply = SetMessage_Object(flex)
        reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)

        return 'OK'

    # CSV = csvFinder(csvPath=os.path.join(csv_storage_path,csv_files[0]))
    # res = CSV.find_row(val=text_from_user,limit=3)

    


if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Credentials.json"
    os.environ["DIALOGFLOW_PROJECT_ID"] = "axial-device-255804"
    app.run(port=5000,debug=True)


