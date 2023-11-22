layeredimage thehamster:

    always:
        "hamster" # 默认图像
     # 根据物品列表中的物品更改外观
    if 'hamster2' in itemlist:
        'hamster2_on'

    # 不同的眼睛状态
    group eyes:
        attribute smile:
            "eyezhengyan"
        attribute eyemimi:
            "eyemimi"
        attribute cry:
            "eyeku"
        attribute scream:
            'eyeduiyan'
        attribute happy:
            "eyemimi"
        attribute weiqu:
            'eyezhengyan'
        attribute guaiqiao:
            "eyemimi"
        attribute shengqi:
            'eyezhengyan'
        attribute hengge:
            'eyemimi'
        attribute xiangxiakan:
            'eyekanxiamian'


    group other:
        attribute weiqyu:
            "eyebowweiqu"

    # 不同的嘴巴状态
    group mouth:
        attribute smile:
            "mouthguaiqiao"
        attribute happy:
            "mouthdaxiao"
        attribute cry:
            "mouthku"
        attribute scream:
            "mouthhuhan"
        attribute weiqu:
            'mouthku'
        attribute guaiqiao:
            'mouthguaiqiao'
        attribute shengqi:
            'mouthhuhan'
        attribute hengge:
            'mouthhengge'
        attribute xiangxiakan:
            'mouthhengge'

    # 根据物品列表中的物品更改配饰
    if 'yellowcap' in itemlist:
        'yellowcap_on'

    if 'fangjin' in itemlist:
        'fangjin_on'

    if 'fangjin_blue' in itemlist:
        'fangjin_blue_on'

    if 'sunglass' in itemlist:
        'sunglass_on'

    if 'weijin' in itemlist:
        'weijin_on'

    if 'pifeng' in itemlist:
        'pifeng_on'


    # 变成猪
    if pigpig:
        'pig'
    if pigpig2:
        'pig2'

    # 有痘痘
    if zhangdoudou:
        'doudou'

