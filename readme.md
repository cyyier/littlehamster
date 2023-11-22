# ゲーム名： - 小さなハムスター

「小さなハムスタ」はPythonとRen'Pyフレームワークを使って開発したゲームです。このゲームでは、プレイヤーは可愛いハムスターと触れ合いながら、英語の単語を学んだり、算数の問題を解くことができます。

## プロジェクト概要

このゲームには、楽しみながら学べる要素を盛り込みました。ゲームの目的は、「小さなハートの破片」を集め、それらを使って新しいアイテム使用を解除することです。ドラッグ＆ドロップやクリック操作で、ハムスターとの様々なインタラクションを楽しめます。

## 使用技術

- **Python**：ゲームのロジックや機能を実装するために使用。
- **Ren'Py**：ゲームのインターフェースを構築し、ユーザーとのインタラクションを処理するために使用。

## コードサンプル

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
