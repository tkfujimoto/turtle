# -*- coding: utf-8 -*-

import turtle # 組み込みのturtleモジュールの読み込み
import random # 組み込みのRandomモジュールの読み込み
import math # 組み込みのmathモジュールの読み込み

# 左右上下のウィンドウ枠線と亀の軌跡の交点座標を求めるメソッドを持つLineクラスの生成
class Line:
    def __init__(self,slp,x0,y0):
        self.slp = float(slp)
        self.x0 = x0
        self.y0 = y0

    # 左右の垂直軸と亀の軌跡との交点のy座標を求めるメソッド
    def get_y(self,x):
        return self.slp*(x-self.x0)+self.y0

    # 上下の水平軸と亀の軌跡との交点のx座標を求めるメソッド
    def get_x(self,y):
        return self.x0+(y-self.y0)/self.slp

# Turtleクラスを継承したKameクラスの生成
class Kame(turtle.Turtle): # Turtleクラスを継承したKameクラスの定義
    def __init__(self): # Kameクラスの初期化関数の定義
        super(Kame,self).__init__() # Kame型の親クラスの初期化関数の実行
        self.shape('turtle') # ターゲットの形状を亀の形にする。
        self.shapesize(2,2) # 亀のサイズを縦・横2倍にし、輪郭線の太さはデフォルト
        self.radians() # 弧度法モードに変更
        self.width(10) # ペン幅(亀の軌跡幅)を10
        self.getscreen().bgcolor('gray') # キャンバスの背景色を灰色
        self.pencolor('white') # ペンの色(亀の軌跡の色)は白
        self.w_2 = self.window_width() / 2.0 # ウィンドウ幅の半分
        self.h_2 = self.window_height() / 2.0 # ウィンドウ高さの半分

    # 任意点にいる亀を壁際の点(des_x,des_y)まで移動させるメソッド
    def hit_wall(self):
        line = Line(math.tan(self.heading()),self.xcor(),self.ycor())
        rand_angle = math.pi * random.random()
        # 上辺に衝突する場合
        if self.towards(-self.w_2,self.h_2)>self.heading()>=self.towards(self.w_2,self.h_2):
            des_x = line.get_x(self.h_2)
            des_y = self.h_2
            turn_angle = self.heading() + rand_angle # 亀の頭を右回りに戻す角度

        # 左辺に衝突する場合
        elif self.towards(-self.w_2,-self.h_2)>self.heading()>self.towards(-self.w_2,self.h_2):
            des_x = -self.w_2
            des_y = line.get_y(-self.w_2)
            turn_angle = self.heading() + rand_angle -math.pi / 2.0 # 亀の頭を右回りに戻す角度

        # 下辺に衝突する場合
        elif self.towards(-self.w_2,-self.h_2)<self.heading()<self.towards(self.w_2,-self.h_2):
            des_x = line.get_x(-self.h_2)
            des_y = -self.h_2
            turn_angle = self.heading() - rand_angle # 亀の頭を右回りに戻す角度

        # 右辺に衝突する場合
        else:
            des_x = self.w_2
            des_y = line.get_y(self.w_2)
            turn_angle = math.pi / 2  + rand_angle # 亀の頭を右回りに戻す角度
        # 壁に当たる点まで移動
        self.goto(des_x,des_y)
        # 回転して、亀の頭を内側に向ける
        self.right(turn_angle)


    def run(self):
        try:
            while True:
                self.hit_wall()
        except KeyboardInterrupt:
            pass

    def click_on_move(self,x,y):
        # self.getscreen().bgcolor('gray')
        self.goto(x,y)


kame = Kame()
kame.getscreen().onclick(kame.click_on_move)
#kame.run()

