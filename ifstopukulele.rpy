label if_stop_ukulele:
    '要让小仓鼠停止弹奏吗？'
    menu:
        '我要继续听！':
            jump if_stop_ukulele
        '先不要弹啦！':
            show ukulele_on:
                xpos 190 ypos 470
            hide yinfu
            play music neko fadeout 1.0 fadein 1.0
            show thehamster happy
            play sound heihei
            '我弹的好听吗？'

            menu:
                '小仓鼠弹得最好听啦！':
                    '谢谢你的夸奖！'
                    $ love += 3

                '真难听！我要捂住耳朵！':
                    show thehamster shengqi
                    play sound heng
                    '哼！再也不弹给你听了！'
                    show ukulele_on at throw_ukulele
                    play sound throw
                    $ itemlist.remove('ukulele')
                    $ getitemlist.remove('ukulele')
                    '小仓鼠扔掉了尤克里里。'
                    $ love -= 3
            hide ukulele_on
            jump if_game_end


label if_stop_ball:
    '要让小仓鼠停止拍皮球吗？'
    menu:
        '接着拍吧':
            jump if_stop_ball
        '拍了好多啦！休息一下吧':
            hide arm_right
            hide ball
            stop sound 
            jump if_game_end