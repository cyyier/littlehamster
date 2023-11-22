# ゲーム名： - 小さなハムスター
## 概要

このゲームでは、プレイヤーは可愛いハムスターと触れ合いながら、英語の単語を学んだり、算数の問題を解くことができます。「小さなハートの破片」を集め、それらを使って新しいアイテム使用を解除します。

## 技術スタック

- **Python**：ゲームのロジックや機能を実装するために使用。
- **Ren'Py**：ゲームのインターフェースを構築し、ユーザーとのインタラクションを処理するために使用。

## コードサンプル

- ### メインロジック

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
