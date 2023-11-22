# 游戏名称：小小仓鼠

小小仓鼠是一个使用 Python 和 Ren'Py 框架开发的交互式游戏。在这个游戏中，玩家可以与小仓鼠进行互动，记忆英语单词和练习算数。

## 项目介绍

本游戏的设计灵感来源于经典的虚拟宠物游戏，结合了互动式学习元素。游戏目标是通过完成各种任务获得“小心心碎片”，使用这些碎片可以解锁新的道具。玩家主要通过拖拽和点击进行操作，与小仓鼠进行各种互动。

## 技术栈

- **Python**：用于实现游戏逻辑和功能。
- **Ren'Py**：用于构建游戏界面和处理用户交互。

## 安装和运行指南

1. 克隆仓库到本地。
2. 安装 Ren'Py（如果尚未安装）。
3. 使用 Ren'Py 打开游戏目录并运行。

## 代码说明

- ### 游戏主逻辑

  ```
  label main_menu:
      return
  label start:
      scene black
      with fade
  label hello:
      play music neko
      # 初始化变量
      $ love = 10
      $ play_time = 0
      ...
  ```

  ### 事件处理

  ```
  if tool == '猫':
      if enemytool == '仓鼠':
          $ ehp -= 1
          ...
      else:
          $ shp -= 1
          ...
  elif tool == '仓鼠':
      if enemytool == '猫':
          $ shp -= 1
          ...
      else:
          $ ehp -= 1
          ...
  ...
  ```

  ### 类的定义和使用

  ```
  class Item(object):
      def __init__(self, id, name, description, peace, bought, puton):
          self._id = id
          self._name = name
          ...
      @property
      def id(self):
          return self._id
      ...
  ```

## 学习体会与挑战

在此项目中，我实践了函数、类、逻辑判断等编程知识点，同时也加深了对 GUI的了解。

## 联系方式

- 邮箱：cyouso@hotmail.com

  

# ゲーム名： - 小さなハムスター

「小さなハムスタ」はPythonとRen'Pyフレームワークを使って開発したゲームです。このゲームでは、プレイヤーは可愛いハムスターと触れ合いながら、英語の単語を学んだり、算数の問題を解くことができます。

## プロジェクトの概要

このゲームには、楽しみながら学べる要素を盛り込みました。ゲームの目的は、「小さなハートの破片」を集め、それらを使って新しいアイテム使用を解除することです。ドラッグ＆ドロップやクリック操作で、ハムスターとの様々なインタラクションを楽しめます。

## 使用技術

- **Python**：ゲームのロジックや機能を実装するために使用。
- **Ren'Py**：ゲームのインターフェースを構築し、ユーザーとのインタラクションを処理するために使用。

## インストールと実行方法

1. リポジトリをローカルにクローンします。
2. Ren'Pyをインストールします（まだインストールしていない場合）。
3. Ren'Pyでゲームフォルダを開き、ゲームを実行します。

## コードについて

- ### ゲームのメインロジック

  ```
  label main_menu:
      return
  label start:
      scene black
      with fade
  label hello:
      play music neko
      # 初始化变量
      $ love = 10
      $ play_time = 0
      ...
  ```

  ### イベントハンドリング

  ```
  if tool == '猫':
      if enemytool == '仓鼠':
          $ ehp -= 1
          ...
      else:
          $ shp -= 1
          ...
  elif tool == '仓鼠':
      if enemytool == '猫':
          $ shp -= 1
          ...
      else:
          $ ehp -= 1
          ...
  ...
  ```

  ### **クラスの定義と利用**

  ```
  class Item(object):
      def __init__(self, id, name, description, peace, bought, puton):
          self._id = id
          self._name = name
          ...
      @property
      def id(self):
          return self._id
      ...
  ```



## 学んだことと挑戦

このプロジェクトを通して、関数、クラス、論理判断などのプログラミングの基本を実践しました。また、GUIの概念についても理解できました。

## 連絡先

- メール：[cyouso@hotmail.com](mailto:cyouso@hotmail.com)