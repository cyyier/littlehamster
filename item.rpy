# 初始化道具列表
default itemlist = []
default getitemlist = []

# 定义背包屏幕
screen bag_screen():
    zorder 1  # 设置层次顺序
    modal True  # 设为模态窗口
    add 'bagbg.png'  # 背包背景图
    style_prefix 'bag'  # 使用'bag'作为样式前缀

    # 定义一个固定容器来布局元素
    fixed:
        # 垂直盒子
        vbox:
            xalign 0.3
            yalign 0.3

        # 5列2行的网格
        grid 5 2:
            pos (.1, .73)
            xspacing 30
            yspacing 30

            # 遍历显示道具
            for item in show_index:
                vbox:
                    spacing -10  # 设置间距
                    # 显示道具图像
                    add Composite(
                        (80, 80),
                        (0, 0), item.image_path)

                    # 检查道具是否已获取
                    if item.id not in getitemlist:
                        text str(item.peace)  # 显示道具信息
                        # 兑换按钮
                        textbutton '兑换':
                            sensitive heart_peace >= item.peace  # 按钮激活状态
                            # 兑换操作
                            action [Confirm('确定要兑换吗？',
                                    (SetVariable('heart_peace', heart_peace - item.peace),
                                    AddToSet(getitemlist, item.id)),Null)]
                    else:
                        text str('')
                        if item.id not in itemlist:
                            # 使用道具按钮
                            textbutton "使用":
                                action [Function(item.puton_item),
                                        AddToSet(itemlist, item.id)]
                        else:
                            # 闲置道具按钮
                            textbutton "闲置":
                                action [Function(item.putoff_item),
                                        RemoveFromSet(itemlist, item.id)]

        # 关闭按钮
        frame:
            pos(600,900)
            maximum (0,0)
            textbutton "关闭" action [Hide('bag_screen')]

# 文本样式定义
style bag_text:
    size 20

# 按钮文本样式定义
style bag_button_text:
    size 40
    idle_color "#fa6aae"
    hover_color "#f0b8d2"
    outlines [ (2, "#fff") ]
    kerning 2

# 道具索引屏幕
screen index_bag():
    zorder 1  # 层次顺序
    frame:
        pos(10, 80)
        maximum (0,0)
        textbutton '道具' action [Show('bag_screen')]  # 显示背包屏幕的按钮