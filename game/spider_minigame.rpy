init:
    transform scurry1:
        zoom 0.2
        linear 2.5 xpos 100 ypos 100
        linear 2.5 xpos 1150 ypos 150
        linear 2.5 xpos 900 ypos 650
        linear 2.5 xpos 300 ypos 550
        linear 2.5 xpos 100 ypos 300
        repeat

    transform scurry2:
        zoom 0.2
        linear 2.7 xpos 1150 ypos 600
        linear 2.7 xpos 200 ypos 650
        linear 2.7 xpos 1000 ypos 300
        linear 2.7 xpos 450 ypos 150
        linear 2.7 xpos 700 ypos 500
        repeat

    transform scurry3:
        zoom 0.2
        linear 2.8 xpos 640 ypos 360
        linear 2.8 xpos 50 ypos 700
        linear 2.8 xpos 1200 ypos 700
        linear 2.8 xpos 1300 ypos 100
        linear 2.8 xpos 700 ypos 50
        repeat

    transform scurry4:
        zoom 0.2
        linear 2.6 xpos 50 ypos 650
        linear 2.6 xpos 1150 ypos 700
        linear 2.6 xpos 400 ypos 350
        linear 2.6 xpos 900 ypos 100
        linear 2.6 xpos 200 ypos 250
        repeat

    transform scurry5:
        zoom 0.2
        linear 2.4 xpos 850 ypos 650
        linear 2.4 xpos 300 ypos 100
        linear 2.4 xpos 1150 ypos 350
        linear 2.4 xpos 100 ypos 400
        linear 2.4 xpos 800 ypos 150
        repeat

screen spider_minigame():

    default spiders = [
        {"id": 0, "transform": scurry1, "special": False},
        {"id": 1, "transform": scurry2, "special": False},
        {"id": 2, "transform": scurry3, "special": True},
        {"id": 3, "transform": scurry4, "special": False},
        {"id": 4, "transform": scurry5, "special": False},
    ]

    for s in spiders:
        if s["id"] not in clicked_spiders:
            if s["special"]:
                imagebutton:
                    idle "spider invite.PNG"
                    focus_mask True
                    at s["transform"]
                    action [Hide("spider_minigame"), Jump("after_spider_game")]
            else:
                imagebutton:
                    idle "spider.PNG"
                    focus_mask True
                    at s["transform"]
                    action Function(clicked_spiders.append, s["id"])
