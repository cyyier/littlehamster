# 拖拽用代码 引入时间
init python:
    import time
    import datetime

    # 拖拽处理函数
    def detective_dragged(drags, drop):
        if not drop:
            return
        store.tool1 = drags[0].drag_name
        store.part = drop.drag_name
        return True

    # 点击时播放声音的函数
    def play_sound_when_clicked():
        renpy.music.play('audio/eng1.ogg','sound')
        renpy.jump('drapdrap')
        return True


label drapdrap:

    # 获取游戏小时数
    $ game_time = renpy.get_game_runtime()
    $ game_time_date = datetime.timedelta(seconds=game_time)
    $ game_time_split = str(game_time_date).split(':',-1)
    $ game_time_format = '%s小时%s分' % (game_time_split[0] ,game_time_split[1])

    # 展示界面部件
    show screen index_chengjiu
    show screen index_bag
    show screen show_heart_peace
    show screen heart
    call screen send_detective_screen


    # 不高兴声音集合
    $ randvoice = renpy.random.choice(['cry', 'ganmaa', 'no', 'niwanla',
                                        'miao','eng1','eng2','eng3'])
    $ voicepath = 'audio/' + randvoice +'.ogg'

    # 选择后
    # 枪
    if tool1 == '枪':
        $ gun += 1
        play sound voicepath
        show thehamster cry
        '你怎么可以用枪指着我？！'
        $ love -= 3

        if part == '肚子':
            $ gunned += 1
            show gun:
                xpos 276 ypos 688
            show thehamster shengqi
            '小仓鼠抢走了你的手枪并朝你射击。'
            show bullet:
                xpos 400 ypos 750
            play sound bulletintoglass
            pause 1.0
            play sound bulletintoglass
            show bullet as bullet2:
                xpos 300 ypos 800 zoom 1.5
            pause 1.0
            play sound bulletintoglass
            show bullet as bullet3:
                xpos 340 ypos 680
            pause 1.0
            '这下知道我的厉害了吧！'
            play sound heng
            hide bullet
            hide bullet2
            hide bullet3
            hide gun

    # 番茄
    elif tool1 == '番茄':
        if part == '嘴巴':
            $ not_healthy -= 1
            $ eateat += 1
            $ eat_tomato += 1
            play sound 'audio/eat.ogg'
            show thehamster happy
            '番茄真好吃！'
            $ love += 2
        elif part == '肚子':
            $ catch_tomato += 1
            show thehamster weiqu
            show tomato at throw_something
            play sound voicepath
            show thehamster guaiqiao
            pause 1.0
            hide tomato
            show rotten_tomato at throwed
            play sound 'audio/throw.ogg'
            pause 1.0
            '小仓鼠接住了番茄并朝你扔回来。'
            hide rotten_tomato
            with dissolve
            $ love -= 1
        else:
            $ throw += 1
            play sound voicepath
            show thehamster scream
            '啊啊啊！怎么朝我的[part]扔番茄？'
            $ love -= 1

    # 手
    elif tool1 == '手':
        if part == '眼睛':
            play sound voicepath
            show thehamster scream
            '眼睛要被戳瞎啦啊啊啊啊！'
            $ love -= 3
        elif part == '肚子':
            play sound voicepath
            show thehamster scream
            '不要不要不要不要痒痒痒痒痒痒！！'
            $ love -= 1
        elif part == '嘴巴':
            play sound jiuyaojiao
            show thehamster weiqu
            '堵我嘴巴我也要叫唤！我就叫我就叫！'
            $ love -= 1
        elif part == '耳朵':
            play sound voicepath
            show thehamster scream
            '干嘛动我耳朵！'
            $ love -= 1

    # 书
    elif tool1 == '书':
        if part == '眼睛':
            $ xuexi += 1
            play sound ea
            show thehamster weiqu
            '为什么要学习呀，哭唧唧'
            show thehamster guaiqiao
            '不过还是要学习呀！'
            $ love += 1
        else:
            $ changepig += 1
            if 'mofashu' in itemlist:
                $ randpig = renpy.random.randint(1,2)
                if randpig == 1:
                    $ pigpig = True
                else:
                    $ pigpig2 = True
                play sound pig
                '我怎么变成...哼哼哼？？？'
                '^(*￣(oo)￣)^哼哼'
                $ pigpig = False
                $ pigpig2 = False
                $ love -= 3
                show thehamster cry
            else:
                $ throw += 1
                play sound voicepath
                show thehamster scream
                '啊啊啊！怎么朝我的[part]扔书？'
                $ love -= 1

    # 冰激凌
    elif tool1 == '冰激凌':
        if part == '嘴巴':
            $ not_healthy += 2
            $ eat_ice += 1
            $ eateat += 1
            play sound eat
            show thehamster happy
            '冰激凌，吃冰激凌啦！'
            show thehamster guaiqiao
            '会不会长胖噢。'
            $ love += 3
        elif part == '肚子':
            $ not_healthy += 1
            $ ice_together += 1
            show thehamster guaiqiao
            show ice:
                xpos 276 ypos 688
            '是冰激凌哎！我们一起七！'
            show ice at centerbig
            play sound wei
            $ love += 1
            '给你七！'
            hide ice
        else:
            $ throw += 1
            play sound voicepath
            show thehamster scream
            '怎么朝我的[part]扔冰激凌！好凉噢！'
            $ love -= 2

    # 可乐 为避免重复用阔乐代替
    elif tool1 == '阔乐':
        if part == '嘴巴':
            $ not_healthy += 2
            $ eat_cola += 1
            $ eateat += 1
            play sound heihei
            show thehamster happy
            '阔落！阔落！好喝！！'
            show thehamster guaiqiao
            '会不会长虫牙噢。'
            $ love += 2
        elif part == '肚子':
            $ not_healthy += 1
            $ cola_together += 1
            show thehamster guaiqiao
            show cola:
                xpos 276 ypos 688
            '是阔落哎！我们一起喝！'
            show cola at centerbig
            play sound wei
            $ love += 1
            '给你喝！'
            hide cola
        else:
            $ throw += 1
            play sound voicepath
            show thehamster scream
            '怎么朝我的[part]扔可乐！都撒啦！'
            $ love -= 1

    # 游戏机
    elif tool1 == '游戏机':
        show youxiji:
            xpos 276 ypos 688
        if part == '肚子':
            play sound wei
            '要来和我比拼手速吗？'
            menu:
                '当然啦！':
                    $ battle_style = 'shousu'
                    jump battle
                '先不玩啦！':
                    play sound ea
                    show thehamster weiqu
                    '那下次要和我玩噢。'
                    hide youxiji
                    with dissolve

        else:
            play sound heihei
            '来一起猜拳吧！'
            menu:
                '看看我们谁比较厉害！':
                    $ battle_style = 'caiquan'
                    jump battle
                '等一下再陪你玩噢。':
                    play sound heng
                    show thehamster shengqi
                    '哼，大人都是坏蛋。'
                    hide youxiji
                    with dissolve

    # 作业本
    elif tool1 == '作业本':
        play sound ea
        show thehamster weiqu
        show homework:
            xpos 276 ypos 688
        if part == '肚子':
            '到了写数学作业的时间了吗？'
            menu:
                '对的！快来写作业！':
                    jump homework_game

                '你要再玩一会儿吗？':
                    show thehamster happy
                    play sound wei
                    '哇！还可以玩还可以玩！'
                    $ love += 1
                    hide homework
        else:
            '到了写英语作业的时间了吗？'
            menu:
                '天天玩可不行！':
                    jump english_homework_game
                '不想写就再休息一会吧！':
                    show thehamster happy
                    play sound heihei
                    '你真好！'
                    $ love += 1
                    hide homework

    # 尤克里里
    elif tool1 == '尤克里里':
        play music ukulele fadeout 1.0 fadein 1.0
        show thehamster hengge
        show ukulele_on at play_ukulele
        show yinfu at play_ukulele_yinfu
        hide screen send_detective_screen
        '小仓鼠开始弹尤克里里。'
        jump if_stop_ukulele


    # 皮球
    elif tool1 == '皮球':
        show arm_right at move_arm_right
        show ball at move_ball
        show thehamster xiangxiakan
        $ renpy.music.play('audio/ball.ogg', channel='sound', loop=True)
        '小仓鼠开始拍皮球。'
        jump if_stop_ball


# 判断是否结束当前游戏流程
label if_game_end:

    if eateat == 5 or eateat==10 :
        show thehamster weiqu
        play sound cry
        '吃这么多，我要被撑死啦！'
        $ love -= 1

    if zhangdoudou == True and not_healthy < 6:
        $ zhangdoudou = False
        show thehamster happy
        play sound heihei
        '我的痘痘治好啦！'
        $ love += 2

    if zhangdoudou == False and not_healthy >=6:
        show thehamster cry
        $ zhangdoudou = True
        play sound cry
        '我怎么长痘痘啦！！！'
        $ love -= 4

    pause 3.0
    $ heart_peace += 1
    $ play_time += 1

    if play_time >= 10 or love <= -5 or love >= 25:

        if love >= 15:
            play sound heihei
            show thehamster happy
            '你真好，最喜欢你啦！'
            '给你10颗心心小碎片！'
            play sound heartpeace
            $ heart_peace += 10
            '再和我一起玩呀！'
            $ happyhamster += 1
            jump hello

        elif love <= 5:
            play sound cry
            show thehamster weiqu
            '你是不是讨厌我呀，老是欺负我!'
            '不过看在你陪我玩的份上，还是给你3颗心心小碎片。'
            play sound heartpeace
            $ heart_peace += 3
            '再给你一次和我玩耍的机会吧。'
            $ sadhamster += 1
            jump hello

        else:
            play sound wei
            show thehamster smile
            '虽然没有特别好，不过谢谢你陪我玩。'
            '给你6颗小心心碎片。'
            play sound heartpeace
            $ heart_peace += 6
            '再一起玩一会儿吧。'
            $ normalhamster += 1
            jump hello
    # 如果未玩10次或者love未超标
    else:
        jump drapdrap


