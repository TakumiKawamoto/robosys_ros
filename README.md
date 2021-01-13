# robosys2020_ros
ロボットシステム学　課題2　ROS

## 内容

2020年10月から日本テレビ系「土曜ドラマ」で放送されたテレビドラマ「35歳の少女」のエンディングを再現

[日本テレビ公式](https://www.ntv.co.jp/shojo35/)ページを見ていただければイメージが掴めるかと思います

作中では、主題歌King Gnu -「三文小説」の曲が流れると同時に、この画像のように柴咲コウさんが映る画面が白黒になり「35歳の少女」の文字が映し出される

ROS, OpenCV, WEBカメラなどを使用し、人の顔を認識すると「35歳の少女」を表示するプログラムを作成し、再現した

---
# 実演動画

[![](http://img.youtube.com/vi/8VfxVXgFEdg/0.jpg)](http://www.youtube.com/watch?v=8VfxVXgFEdg "robosys2020 ros demo video")

---
## 環境・使用機材

- Raspberry Pi4 Model B
- WEBカメラ(USB接続)
- Ubuntu 20.04
- ROS Noetic
- OpenCV　4.2.0

加えてOpenCV, ROS Noetic, cv_camera, web_video_serverが使用可能であることを前提とする

RyuichiUeda氏の[講義資料](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)に従いインストールを行った

---
## インストール・実行方法

    $ cd ~/catkin_ws/src
    $ git clone https://github.com/TakumiKawamoto/robosys_ros.git
    $ cd ~/catkin_ws
    $ catkin_make
    $ cd ~/catkin_ws/src/robosys_ros
    $ ./setup.bash      #実行
    同一ネットワーク内の別端末で http://ラズパイのIPアドレス:8080 にアクセス
---
## 参考

https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md

https://qiita.com/FukuharaYohei/items/ec6dce7cc5ea21a51a82

https://qiita.com/wakaba130/items/d3a041164c316a9e7a97

---
## ライセンス

[BSD 3-Clause License](https://github.com/TakumiKawamoto/robosys_ros/blob/main/LICENSE)
