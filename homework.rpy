init 2 python:
    def clear_inputter():
        global input_text

        input_text = 0

    def add_to_inputter(num):
        global input_text
        if input_text <= 99:
            input_text = input_text * 10 + num


    def show_countdown_hw(st, at):
        if st > 10:
            return Text("00",size=200), None
        else:
            d = Text("{:.1f}".format(10- st),size=200)
            return d, 0.1

screen inputted_num():
    zorder 1
    add 'inputted.png'
    style_prefix 'bag'
    frame:
        pos (130,320)
        maximum (0,0)
        text '{color=#4f6d7d}[hw_question]x[hw_question]={/color}' size 40
    frame:
        pos (290,300)
        maximum (0,0)
        text '{color=#4f6d7d}[input_text]{/color}' size 100

screen inputter():
    zorder 1
    modal True
    style_prefix 'bag'
    imagemap:
        auto "inputer_%s.png"

        hotspot (140, 400, 120, 95) action Function(add_to_inputter, 1)
        hotspot (300, 400, 120, 95) action Function(add_to_inputter, 2)
        hotspot (460, 400, 120, 95) action Function(add_to_inputter,3)
        hotspot (140, 520, 120, 95) action Function(add_to_inputter, 4)
        hotspot (300, 520, 120, 95) action Function(add_to_inputter, 5)
        hotspot (460, 520, 120, 95) action Function(add_to_inputter, 6)
        hotspot (140, 630, 120, 95) action Function(add_to_inputter, 7)
        hotspot (300, 630, 120, 95) action Function(add_to_inputter, 8)
        hotspot (460, 630, 120, 95) action Function(add_to_inputter, 9)
        hotspot (140, 740, 120, 95) action Function(clear_inputter)
        hotspot (300, 740, 120, 95) action Function(add_to_inputter, 0)
        hotspot (460, 740, 120, 95) action Jump('after_input')

    timer 10 action Jump('too_slow_homwork')


#####################
##战斗####

label homework_game:
###############
#战斗前准备#####
###############
    hide screen send_detective_screen
    hide screen index_chengjiu
    hide screen index_bag
    $ spoint = 0
    $ hw_time = 0


#######################
####做作业画面准备#########
#####################
    image pink = '#fad6e0'
    scene pink
    with dissolve
    play music 'audio/homework.mp3' fadeout 1.0 fadein 1.0
    show text "{size=200}{color=#d5c868}Start{/color}{/size}" at truecenter with vpunch
    pause 1
    hide text
    with dissolve
    show zuoyeben at truecenter
    with dissolve

    jump homework_start



#################################
#########做作业-战斗开始####################
##################################

label homework_start:
# 显示得分

    # 恢复表情
    show thehamster smile:
        xpos 100 ypos 40
    $ input_text = 0
    $ hw_time += 1
    if hw_time == 6:
        jump winlost_homework


# 出题

    '请作答！'

# 通过键盘输入做题
    hide zuoyeben
    with dissolve

    show screen inputted_num
    image countdown_hw = DynamicDisplayable(show_countdown_hw)
    show countdown_hw:
        xpos 0.3 ypos 1000
    $ hw_question = renpy.random.randint(11,29)
    $ hw_answer = hw_question ** 2
    call screen inputter



label after_input:
    hide image countdown_hw

    if hw_answer == input_text:
        show thehamster happy
        play sound heihei
        '回答正确！'

        $ spoint += 1

    else:
        '回答错误'
        show thehamster cry
        play sound ea
        '答案是[hw_answer]。'

    jump homework_start


label too_slow_homwork:
    hide image countdown_hw
    '太慢啦！这个没记住噢'
    '答案是[hw_answer]。'

    jump homework_start

    jump winlost_homework
# 判定胜利
label winlost_homework:
    hide screen inputted_num
    hide screen inputter
    if spoint < 3:
        scene lost
        with fade
        stop music fadeout 1.0
        play sound 'audio/lost.ogg'
        '小仓鼠数学好差噢...'


    else:
       scene win
       with fade
       stop music fadeout 1.0
       play sound 'audio/win.ogg'
       '小仓鼠数学得了高分！'


    '一共答对了[spoint]道题！'
    $ hw_heart_peace = spoint*3
    $ heart_peace += hw_heart_peace
    play sound heartpeace
    '获得了[hw_heart_peace]颗小心心碎片！'

    '学习好辛苦噢！今天就到这里吧！'
    play sound kunkun
    jump hello

