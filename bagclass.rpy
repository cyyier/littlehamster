# 初始化字典，物品，Item类
init 1 python:
    item_index = dict([
        ('yellowcap', Item(id='yellowcap', name='小黄帽',
            description='一顶可爱的小黄帽',
            peace=5,bought=0,puton=0, )),
        ('sunglass', Item(id='sunglass', name='墨镜',
            description='一个很酷的墨镜',
            peace=10,bought=0,puton=0,)),
        ('fangjin', Item(id='fangjin', name='方巾',
            description='红色的小方巾',
            peace=10,bought=0,puton=0,)),
        ('fangjin_blue', Item(id='fangjin_blue', name='蓝方巾',
            description='蓝色的小方巾',
            peace=10,bought=0,puton=0,)),
        ('weijin', Item(id='weijin', name='围巾',
            description='一条温暖的围巾',
            peace=20,bought=0,puton=0,)),
        ('pifeng', Item(id='pifeng', name='披风',
            description='帅气的披风，有点儿贵',
            peace=30,bought=0,puton=0,)),
        ('duck', Item(id='duck', name='鸭子',
            description='一只很长的鸭子',
            peace=20,bought=0,puton=0,)),
        ('hamster2', Item(id='hamster2', name='2号',
            description='2号小仓鼠',
            peace=20,bought=0,puton=0,)),
        ('mofashu', Item(id='mofashu', name='魔法书',
            description='可以把仓鼠变猪头的魔法书',
            peace=15,bought=0,puton=0,)),
        ('ukulele', Item(id='ukulele', name='尤克里里',
            description='小仓鼠在学习尤克里里',
            peace=1,bought=0,puton=0,)),
        ])

# 初始化列表，商店中的物品
init 2 python:
    show_index = [item_index['yellowcap'], item_index['sunglass'],
                item_index['fangjin'], item_index['fangjin_blue'],item_index['weijin'],
                item_index['pifeng'], item_index['duck'],item_index['hamster2'],item_index['mofashu'],item_index['ukulele']
                ]


init python:
    # Bag 类，玩家的背包
    class Bag(object):
        def __init__(self):
            self._bag = dict()

    # Item 类，可购买的物品
    class Item(object):
        def __init__(self, id, name, description, peace, bought, puton):
            self._id = id
            self._name = name
            self._description = description
            self._peace = peace  # 价格
            self._bought = bought  # 是否已购买
            self._image_path = 'images/' + id + '.png'  # 物品图像路径
            self._image_on_path = 'images/' + id + '_on.png'  # 装备时的物品图像路径
            self._puton = puton  # 是否已装备

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @property
        def description(self):
            return self._description

        @property
        def peace(self):
            return self._peace

        @property
        def bought(self):
            return self._bought

        @property
        def image_path(self):
            return self._image_path

        @property
        def image_on_path(self):
            return self._image_on_path

        @property
        def puton(self):
            return self._puton

        # 获取物品的详细信息
        def get_item_info(self):
            return self._name + '：\n' + self._description + '\n' + '价格：' + str(self._price)

        # 购买物品
        def get_item(self):
            self._bought = 1

        # 装备物品
        def puton_item(self):
            self._puton = 1

        # 卸下物品
        def putoff_item(self):
            self._puton = 0

        # 判断物品是否已装备
        def puton_true(self):
            return self._puton == 1

