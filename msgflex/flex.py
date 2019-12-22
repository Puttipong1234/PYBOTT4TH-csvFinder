def box_list(key,value):


    each_box = {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "| {}".format(key),
                    "size": "sm",
                    "color": "#888888",
                    "flex": 0
                },
                {
                    "type": "text",
                    "text": value,
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "wrap": True
                }
                ]
        }
    
    return each_box



def flex_find_row(แถวที่พบ,คำที่ค้นหา,คะแนนความเที่ยงตรง,คอลัมน์ที่ค้นพบคำนี้,รายการที่ค้นพบ):


    all_boxes = []
    for key,val in รายการที่ค้นพบ.items():
        box = box_list(key,val)
        all_boxes.append(box)
    
    seperator = {
                "type": "separator",
                "margin": "sm"
            }
    
    all_boxes.append(seperator)



    bubble ={
    "type": "bubble",
    "size": "giga",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "โครงการ :บ้านสองชั้น 20 ล้าน",
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
        },
        {
            "type": "text",
            "text": "| ตำแหน่งที่พบ : แถวที่ {}".format(แถวที่พบ),
            "weight": "bold",
            "size": "lg",
            "margin": "xs"
        },
        {
            "type": "text",
            "text": "คำที่ค้นหา : {}".format(คำที่ค้นหา),
            "size": "xs",
            "color": "#aaaaaa",
            "wrap": True,
            "align": "start",
            "margin": "md"
        },
        {
            "type": "text",
            "text": "คะแนนความเที่ยงตรง : {}".format(คะแนนความเที่ยงตรง),
            "size": "xs",
            "color": "#aaaaaa",
            "wrap": True,
            "align": "start",
            "margin": "none"
        },
        {
            "type": "text",
            "size": "xs",
            "color": "#aaaaaa",
            "wrap": True,
            "align": "start",
            "text": "คอลัมน์ที่ค้นพบคำนี้ : {}".format(คอลัมน์ที่ค้นพบคำนี้)
        },
        {
            "type": "separator",
            "margin": "xxl"
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "xl",
            "spacing": "sm",
            "contents": all_boxes
        },
        {
            "type": "separator",
            "margin": "xxl"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "margin": "md",
            "contents": [
            {
                "type": "text",
                "text": "ลิงค์ Google Sheet",
                "size": "xs",
                "color": "#aaaaaa",
                "flex": 0
            },
            {
                "type": "text",
                "text": "คลิก",
                "color": "#1DB446",
                "size": "xs",
                "align": "end",
                "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://docs.google.com/spreadsheets/d/1jJh2FrTGco-c_-W_a6ZRvr_Vhu3lu5lxS5TalCLozqg"
                }
            }
            ]
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "image",
                "url": "https://cdn-images.prod.thinkofliving.com/wp-content/uploads/1/2019/04/24112413/05-NEO-HOME_Italian-Style.jpg",
                "position": "relative",
                "size": "xs",
                "aspectMode": "cover"
            }
            ],
            "position": "absolute",
            "cornerRadius": "50px",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "offsetEnd": "10px",
            "offsetTop": "10px"
        }
        ]
    },
    "styles": {
        "footer": {
        "separator": True
        }
    }
    }

    return bubble



def make_carousel(all_bubble):

    carousel = {
  "type": "carousel",
  "contents": all_bubble
  }

    flex = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": carousel
  }

    return flex


def flex_find_value(คำที่ค้นหา,results):

    all_boxes = []
    for num,each in enumerate(results , start=1):
        box = {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "- รายการที่ {}".format(num),
                  "flex": 0,
                  "margin": "xs",
                  "weight": "bold",
                  "color": "#969696"
                },
                {
                  "type": "text",
                  "text": each,
                  "size": "xs",
                  "align": "end",
                  "color": "#AAAAAA"
                }
              ]
            }
        
        all_boxes.append(box)


    flex = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://cdn-images.prod.thinkofliving.com/wp-content/uploads/1/2019/04/24112413/05-NEO-HOME_Italian-Style.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "md",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "| Result จากการค้นหา",
          "size": "lg",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "พบรายการจากคำที่ท่านค้นหา x รายการ",
          "margin": "none",
          "size": "xs",
          "color": "#AAAAAA",
          "wrap": True
        },
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": all_boxes
        },
        {
          "type": "separator"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "spacer",
          "size": "xs"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "google sheet link",
            "uri": "https://docs.google.com/spreadsheets/d/1jJh2FrTGco-c_-W_a6ZRvr_Vhu3lu5lxS5TalCLozqg"
          },
          "color": "#009605",
          "style": "primary"
        }
      ]
    }
  }
}
    return flex