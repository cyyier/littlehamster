# 游戏的脚本可置于此文件中。
default heart_peace = 0

default pigpig = False
default pigpig2 = False

default happyhamster = 0
default sadhamster = 0
default normalhamster =0
default gun = 0
default gunned = 0
default eat_tomato = 0
default throw_tomato = 0
default catch_tomato = 0
default throw = 0
default changepig = 0
default eat_cola = 0
default eat_ice = 0
default ice_together = 0
default cola_together = 0
default xuexi = 0





screen sleephamsterbutton:
    vbox xalign 0.5 yalign 0.5:
        imagebutton insensitive "hamstersleepbutton.png" idle 'hamstersleepbutton.png' action [Play('sound',sleepvoice), Jump('sleep')]

label main_menu:
    return
# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    scene black
    with fade

label hello:
    play music neko
    # 重置爱心值和次数
    $ love = 10
    $ play_time = 0
    $ eateat = 0
    $ not_healthy = 0
    $ zhangdoudou = False

    # 获取当前时间
    $ time_now = time.localtime()
    $ hour_now = time_now[3]

    if 0 < hour_now < 4:
        scene shenye
        with fade
        '这么晚你该睡觉啦！'

    elif 4<= hour_now < 10:
        scene qingchen
        with fade
        '早上好呀！'

    elif 10<= hour_now < 14:
        scene day
        with fade
        '中午好！'

    elif 14 <= hour_now <17 :
        scene day
        with fade
        '下午好！'

    else:
        if 17<= hour_now < 20:
            scene bangwan
            with fade
        else:
            scene shenye
            with fade
        '晚上好！'

label ifsleep:
    if 6 <= hour_now < 22:
        $ nowsleep = renpy.random.randint(1,3)
    else:
        $ nowsleep = renpy.random.randint(0,2)
    if nowsleep == 0 or nowsleep == 1:
        show hamstersleep at truecenter
        $ disturb = 0
        jump sleep
    else:
        jump notsleep

# 睡觉label
label sleep:
    $ disturb += 1

    # 被吵醒
    if disturb > 5:
        hide hamstersleep
        hide screen sleephamsterbutton
        with dissolve
        '小仓鼠被你吵醒了！'
        show thehamster shengqi at truecenter
        with dissolve
        play sound ganmaa
        jump drapdrap

    # 睡觉状态
    $ sleepvoice = renpy.random.choice(['audio/eng1.ogg','audio/eng2.ogg','audio/eng3.ogg'])
    show screen sleephamsterbutton

    # 睡觉动画
    image hamstersleep animated:
        "hamstersleep.png"
        pause 2.0
        "hamstersleep2.png"
        pause 2.0
        repeat

    # 展示睡觉
    show hamstersleep animated


    # 询问是否叫醒
    '小仓鼠正在睡觉，要叫醒它吗？'
    menu:
        '叫醒它':
            hide hamstersleep
            hide screen sleephamsterbutton
            show thehamster cry at truecenter
            with dissolve
            play sound kunkun
            '小仓鼠被叫醒了。'
            jump drapdrap   # 跳转至游戏主内容
        '让它继续睡':
            '小仓鼠呼呼大睡。'
            jump sleep

# 未睡觉label
label notsleep:

# 有小鸭子时展示仓鼠
    if 'duck' in itemlist:
        show duck_on:
            xpos 0.00 ypos 0.54
        show thehamster smile at truecenter
        with moveinright

        play sound heihei
        '我来啦！！'

        hide duck_on
        with moveoutleft

# 没有小鸭子时展示仓鼠
    else:
        show huaban:
            xpos 0.2 ypos 0.65 zoom 2
        show thehamster smile at truecenter
        with moveinright

        '我来啦！！'

        hide huaban
        with moveoutleft
# 跳转至游戏主内容
    jump drapdrap


