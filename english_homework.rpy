init python:
    import random

screen english_question_screen():
    zorder 1
    add 'english_question.png'
    text '{color=#585858}[word_question_index]{/color}':
        size 100
        xcenter 0.5
        ycenter 0.5

#####################
##战斗####

label english_homework_game:
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
    '今天要学哪一部分单词呢？'
    menu:
        'a':
            $ list_choiced_index = index_list_a
        'bc':
            $ list_choiced_index = index_list_bc
        '我都可以，你选吧':
            $ list_choiced_index = renpy.random.choice([index_list_a,index_list_bc])



    jump english_homework_start



#################################
#########做作业-战斗开始####################
##################################

label english_homework_start:
# 显示得分

    # 恢复表情
    show thehamster smile:
        xpos 100 ypos 40
    $ input_text = 0
    $ hw_time += 1
    if hw_time == 6:
        jump english_winlost_homework


# 出题
python:


    if list_choiced_index == index_list_a:
        wordlist_choiced = wordlist_a
    elif list_choiced_index == index_list_bc:
        wordlist_choiced = wordlist_bc


    word_question_index = random.choice(list_choiced_index)
    correct_answer = wordlist_choiced[word_question_index]
    wrong_answers = wordlist_choiced.values()
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers_slice = random.sample(wrong_answers,3)
    answer_options = [correct_answer] + wrong_answers_slice
    random.shuffle(answer_options)

show screen english_question_screen

menu:
    '[answer_options[0]]':
        $ ehw_answer = answer_options[0]
    '[answer_options[1]]':
        $ ehw_answer = answer_options[1]
    '[answer_options[2]]':
        $ ehw_answer = answer_options[2]
    '[answer_options[3]]':
        $ ehw_answer = answer_options[3]

if ehw_answer == correct_answer:

    show thehamster happy
    play sound heihei
    '回答正确！'
    $ spoint += 1
else:
    show thehamster cry
    play sound ea
    '错啦！\n{size=30}[correct_answer]{/size}'




jump english_homework_start




# 判定胜利
label english_winlost_homework:
    hide screen english_question_screen
    if spoint < 3:
        scene lost
        with fade
        stop music fadeout 1.0
        play sound 'audio/lost.ogg'
        '小仓鼠英语好差噢...'


    else:
       scene win
       with fade
       stop music fadeout 1.0
       play sound 'audio/win.ogg'
       '小仓鼠英语得了高分！'


    '一共答对了[spoint]道题！'
    $ hw_heart_peace = spoint*3
    $ heart_peace += hw_heart_peace
    play sound heartpeace
    '获得了[hw_heart_peace]颗小心心碎片！'

    '学习好辛苦噢！今天就到这里吧！'
    play sound kunkun
    jump hello

