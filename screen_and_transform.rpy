transform throw_something:
    xalign 0.5 yalign 0.5
    alignaround (.5, .5)
     # 耗时2秒钟。
    linear 1.0 align (0.5, 0.8) zoom 5.0  rotate 720

transform throwed:
    xalign 0.5 yalign 0.8

transform centerbig:
    xalign 0.5 yalign 0.5
    linear 1.0 align(0.5,0.8) zoom 5.0

transform play_ukulele:
    xpos 190 ypos 470
    linear 1.0 rotate 8
    linear 1.0 rotate -8
    repeat

transform throw_ukulele:
    xpos 190 ypos 470
    linear 1.0 align(0,40) rotate 720 zoom 3.0
    linear 0.3 alpha 0




transform play_ukulele_yinfu:
    xpos 492 ypos 539 zoom 0.3
    linear 0 zoom 0.3 xoffset -20 yoffset 20 alpha 1
    linear 2.0 zoom 1.1 xoffset 50 yoffset -50 alpha 0
    pause 1.0
    repeat


transform move_arm_right:
    xpos 300 ypos 660
    linear 0.8 rotate 10 yoffset 5
    linear 0.8 rotate -10 yoffset -5
    repeat

transform move_ball:
    xpos 327 ypos 810
    linear 0.8 yoffset -50
    linear 0.8 yoffset 50
    repeat

transform battleleft:
    xalign 0.0 yalign 0.8
    zoom 0.7
    xzoom -1.0

transform battleright:
    xalign 1.3 yalign 0.8
    zoom 0.6

transform yizi_left:
    xalign 0.0 yalign 1.0 zoom 1.6

transform yizi_right:
    xalign 1.0 yalign 1.0 zoom 1.6

transform toolright:
    xpos 420 ypos 500 xzoom -1.0

transform toolleft:
    xpos 90 ypos 500

transform huangguancenter:
    xpos 180 ypos 560

transform huangguan_left:
    xpos 95 ypos 480

transform huangguan_right:
    xpos 410 ypos 480 xzoom -1.0


# 游戏主流程screen
screen send_detective_screen:

    draggroup:

        # 道具
        drag:
            drag_name "手"
            child "hand.png"
            droppable False
            dragged detective_dragged
            xpos 71 ypos 472
        drag:
            drag_name "枪"
            child "gun.png"
            droppable False
            dragged detective_dragged
            xpos 71 ypos 590
        drag:
            drag_name "书"
            child "book.png"
            droppable False
            dragged detective_dragged
            xpos 71 ypos 708
        drag:
            drag_name "番茄"
            child "tomato.png"
            droppable False
            dragged detective_dragged
            xpos 637 ypos 472
        drag:
            drag_name "冰激凌"
            child "ice.png"
            droppable False
            dragged detective_dragged
            xpos 637 ypos 590
        drag:
            drag_name "阔乐"
            child "cola.png"
            droppable False
            dragged detective_dragged
            xpos 637 ypos 708
        drag:
            drag_name '游戏机'
            child 'youxiji.png'
            droppable False
            dragged detective_dragged
            xpos 637 ypos 850

        drag:
            drag_name '作业本'
            child 'homework.png'
            droppable False
            dragged detective_dragged
            clicked play_sound_when_clicked
            xpos 71 ypos 850

        drag:
            drag_name '皮球'
            child 'ball.png'
            droppable False
            dragged detective_dragged
            xpos 540 ypos 947

        if 'ukulele' in itemlist:
            drag:
                drag_name '尤克里里'
                child 'ukulele.png'
                droppable False
                dragged detective_dragged
                xpos 198 ypos 947


        # 小仓鼠的哪
        drag:
            drag_name "耳朵"
            child "hamster_ear.png"
            droppable True
            draggable False
            xpos 175 ypos 398
        drag:
            drag_name "眼睛"
            draggable False
            child "hamster_eye.png"
            xpos 173 ypos 481

        drag:
            drag_name "嘴巴"
            draggable False
            child "hamster_mouth.png"
            xpos  173 ypos 550
        drag:
            drag_name "肚子"
            draggable False
            child "hamster_body.png"
            xpos 175 ypos 653

# 下方love显示
screen single_stat1():
    frame:
        xpos 0.0
        ypos 0.99
        bar:
            value AnimatedValue(love, 20.0, 1.0)
            xmaximum 720
            ysize 30
screen heart():
    use single_stat1()

# 上方心心碎片数量
screen show_heart_peace():
    frame:
        pos (10,10)
        maximum (0,0)
        add 'heartpic.png'
    frame:
        pos (70,10)
        maximum (0,0)
        text "{color=#222}[heart_peace]{/color}" size 40

# 成就界面
screen chengjiu():
    zorder 1
    modal True
    add 'dacangshu.png'
    style_prefix 'chengjiu'

    vbox:
        xpos 1
        if config.has_music:
            vbar value Preference("music volume")

    vbox:
        xalign 0.15 yalign 0.05
        text ('''
        你和小仓鼠一起度过了{color=#cc0066}[game_time_format]{/color}的时光:\n
        你把小仓鼠逗开心了{color=#cc0066}[happyhamster]{/color}次。\n
        你让小仓鼠伤心了{color=#cc0066}[sadhamster]{/color}次。\n
        有{color=#cc0066}[normalhamster]{/color}次小仓鼠平静的度过了。\n
        你用枪指着小仓鼠{color=#cc0066}[gun]{/color}次，\n
        其中{color=#cc0066}[gunned]{/color}次被小仓鼠反击了。\n
        你用各种东西砸了小仓鼠{color=#cc0066}[throw]{/color}次，\n
        其中有{color=#cc0066}[catch_tomato]{/color}次小仓鼠接住了番茄扔了回来。\n
        你还用魔法书把小仓鼠变成了猪{color=#cc0066}[changepig]{/color}次。\n
        你看着小仓鼠认真学习了{color=#cc0066}[xuexi]{/color}次。\n
        你也喂小仓鼠吃了{color=#cc0066}[eat_tomato]{/color}个番茄，{color=#cc0066}[eat_ice]{/color}根冰激凌，\n
        喝了{color=#cc0066}[eat_cola]{/color}杯可乐。\n
        你们还一起分享了{color=#cc0066}[ice_together]{/color}根冰激凌，{color=#cc0066}[cola_together]{/color}杯可乐。\n
        要好好照看你的小仓鼠呀! \n
                              by大仓鼠''')

    frame:
        pos(0.85,1000)
        maximum (0,0)
        textbutton "返回" action [Hide('chengjiu')]

style chengjiu_text:
    size 30

style chengjiu_button_text:
    size 30
    idle_color "#fa6aae"
    hover_color "#f0b8d2"
    outlines [ (2, "#fff") ]
    kerning 2

# 成就index
screen index_chengjiu():
    zorder 1
    frame:
        pos(10, 160)
        maximum (0,0)
        textbutton '历程' action [Show('chengjiu')]

