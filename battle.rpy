init python:
    # 拖拽物品后的处理
    def battle_dragged(drags1, drop1):
        if not drop1:
            return

        store.tool = drags1[0].drag_name
        return True

    # 战斗时的倒计时显示
    def show_countdown(st, at):
        if st > 1.3:
            return Text("0.0",size=100), None
        else:
            d = Text("{:.01f}".format(1.30 - st),size=100)
            return d, 0.01


##########################
##########显示血条#########
##########################

screen hp_stat():
# 小仓鼠血条
    frame:
        ypos 100
        xalign 0.0

        vbox:
            spacing 5
            hbox:
                text "小仓鼠" min_width 220
            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5
                bar:
                    value AnimatedValue(shp, 5, 1.0)
                    xmaximum 180
                    ysize 26
                if shp > 0:
                    text " [shp]/5":
                        yalign 0.5
                else:
                    text " 0/5":
                        yalign 0.5
# 喵污血条
    frame:
        ypos 100
        xalign 1.0

        vbox:
            spacing 5
            hbox:
                text "喵污" min_width 220
            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5
                bar:
                    value AnimatedValue(ehp, 5, 1.0)
                    xmaximum 180
                    ysize 26
                if ehp > 0:
                    text " [ehp]/5":
                        yalign 0.5
                else:
                    text " 0/5":
                        yalign 0.5


#######################
####拖拽################
#############################
screen battle_screen:
    draggroup:
        # 道具们
        drag:
            drag_name "猫"
            child "battlecat.png"
            droppable False
            dragged battle_dragged
            xpos 100 ypos 300
        drag:
            drag_name "可乐"
            child "battlecola.png"
            droppable False
            dragged battle_dragged
            xpos 250 ypos 300
        drag:
            drag_name "仓鼠"
            child "battlehamster.png"
            droppable False
            dragged battle_dragged
            xpos 400 ypos 300
        # 盘子
        drag:
            drag_name "盘子"
            child "panzi.png"
            draggable False
            xpos 80 ypos 680


    # 如果是手速战斗模式，跳转
    if battle_style == 'shousu':
        timer 1.3 action Jump('too_slow')

# 太慢的情况下跳转到的标签
label too_slow:
    '你没有应战，喵污直接向你发起攻击。'
    $ shp -= 1
    hide battlecola
    hide battlehamster
    hide battlecat
    hide battlecola1
    hide battlehamster1
    hide battlecat1
    hide huangguan
    if shp <= 0:
        jump winlost
    else:
        jump battle_start


#####################
##战斗####
#####################

label battle:
###############
#战斗前准备#####
###############
    $ shp = 5
    $ ehp = 5
    hide screen send_detective_screen
    hide screen index_chengjiu
    hide screen index_bag

#######################
####战斗画面准备#########
#####################
    image pink = '#fad6e0'
    scene pink
    show yizi at yizi_left
    show yizi2 at yizi_right
    show thehamster smile at battleleft
    show miaowu normal at battleright
    show panzi:
        xpos 80 ypos 680
    show panzi as panzi2:
        xpos 0.6 ypos 680
    with dissolve
    play music 'audio/battle.ogg' fadeout 1.0 fadein 1.0
    show text "{size=200}{color=#d5c868}FIGHT{/color}{/size}" at truecenter with vpunch
    pause 1
    hide text
    with dissolve
    if battle_style == 'caiquan':
        '小仓鼠和喵污猜拳！'
    elif battle_style == 'shousu':
        '小仓鼠和喵污拼手速！'

    jump battle_start


#################################
#########猜拳-战斗开始####################
##################################

label battle_start:
# 显示皇冠和hp
    show screen hp_stat
    show huangguan at huangguancenter

    # 恢复表情
    show thehamster smile
    show miaowu normal

# 手速时敌人选择并绘制
    if battle_style == 'shousu':
        $ enemytool = renpy.random.choice(['猫','仓鼠','可乐'])
        if enemytool == '猫':
            show battlecat as battlecat1 at toolright
            with dissolve
        elif enemytool == '仓鼠':
            show battlehamster as battlehamster1 at toolright
            with dissolve
        else:
            show battlecola as battlecola1 at toolright
            with dissolve
                #倒计时
        image countdown = DynamicDisplayable(show_countdown)
        show countdown:
            xpos 310 ypos 650

# 拖拽画面
    call screen battle_screen


# 显示己方选择
    if tool == '猫':
        show battlecat at toolleft
    elif tool == '仓鼠':
        show battlehamster at toolleft
    else:
        show battlecola at toolleft

# 猜拳时敌人的选择
    if battle_style == 'caiquan':
        $ enemytool = renpy.random.choice(['猫','仓鼠','可乐'])
        if enemytool == '猫':
            show battlecat as battlecat1 at toolright
            with dissolve
        elif enemytool == '仓鼠':
            show battlehamster as battlehamster1 at toolright
            with dissolve
        else:
            show battlecola as battlecola1 at toolright
            with dissolve

# 两边选的一样时
    if tool == enemytool:
        '你们都用了[tool]进行攻击，谁也没打过谁...'
        show huangguan at huangguancenter
        with vpunch
        hide battlecola
        hide battlehamster
        hide battlecat
        hide battlecola1
        hide battlehamster1
        hide battlecat1
        hide huangguan
        jump battle_start
# 两边选的不同时
    else:
        if tool == '猫':
            if enemytool == '仓鼠':
                $ ehp -= 1
                show huangguan at huangguan_left
                play sound heihei
                show thehamster happy
                show miaowu cry
                '你用猫吃掉了喵污的仓鼠，啊呜！！'
            else:
                $ shp -= 1
                play sound miao
                show huangguan at huangguan_right
                show thehamster cry
                '你的猫喝多了喵污的可乐，牙疼的满地打滚！！。'
        elif tool == '仓鼠':
            if enemytool == '猫':
                $ shp -= 1
                show huangguan at huangguan_right
                play sound cry
                show thehamster scream
                '你的仓鼠被喵污的猫一口吃掉，太惨了！！。'
            else:
                $ ehp -= 1
                show huangguan at huangguan_left
                play sound heihei
                show thehamster happy
                show miaowu cry
                '你的仓鼠快乐的喝掉了喵污的可乐，好喝！！。'
        else:
            if enemytool == '猫':
                $ ehp -= 1
                show huangguan at huangguan_left
                play sound heihei
                show thehamster happy
                show miaowu cry
                '你的可乐把喵污的猫的牙全变成大虫牙了！！。'
            else:
                $ shp -= 1
                show huangguan at huangguan_right
                play sound cry
                show thehamster weiqu
                '你的可乐被喵污的仓鼠一口就喝掉，它还打了个嗝！！。'
    jump winlost

# 判定胜利
label winlost:
    if shp > 0 and ehp > 0:
        hide battlecola
        hide battlehamster
        hide battlecat
        hide battlecola1
        hide battlehamster1
        hide battlecat1
        hide huangguan
        jump battle_start
    else:
        hide text
        with dissolve
        hide screen hp_stat
        if shp <= 0:
            scene lost
            with fade
            stop music fadeout 1.0
            play sound 'audio/lost.ogg'
            '小仓鼠被打败了...'
            play sound heartpeace
            '只获得了4颗小心心碎片。'
            $ heart_peace += 4
        else:
           scene win
           with fade
           stop music fadeout 1.0
           play sound 'audio/win.ogg'
           '小仓鼠取得了胜利！'
           play sound heartpeace
           '获得了15颗小心心碎片！'
           $ heart_peace += 15


    '玩累啦玩累啦！今天就到这吧！'
    play sound heihei
    jump hello












