# -*- coding: cp932 -*-

import turtle # �g�ݍ��݂�turtle���W���[���̓ǂݍ���
import random # �g�ݍ��݂�Random���W���[���̓ǂݍ���
import math # �g�ݍ��݂�math���W���[���̓ǂݍ���

# ���E�㉺�̃E�B���h�E�g���ƋT�̋O�Ղ̌�_���W�����߂郁�\�b�h������Line�N���X�̐���
class Line:
    def __init__(self,slp,x0,y0):
        self.slp = float(slp)
        self.x0 = x0
        self.y0 = y0

    # ���E�̐������ƋT�̋O�ՂƂ̌�_��y���W�����߂郁�\�b�h
    def get_y(self,x):
        return self.slp*(x-self.x0)+self.y0

    # �㉺�̐������ƋT�̋O�ՂƂ̌�_��x���W�����߂郁�\�b�h
    def get_x(self,y):
        return self.x0+(y-self.y0)/self.slp

# Turtle�N���X���p������Kame�N���X�̐���
class Kame(turtle.Turtle): # Turtle�N���X���p������Kame�N���X�̒�`
    def __init__(self): # Kame�N���X�̏������֐��̒�`
        super(Kame,self).__init__() # Kame�^�̐e�N���X�̏������֐��̎��s
        self.shape('turtle') # �^�[�Q�b�g�̌`����T�̌`�ɂ���B
        self.shapesize(2,2) # �T�̃T�C�Y���c�E��2�{�ɂ��A�֊s���̑����̓f�t�H���g
        self.radians() # �ʓx�@���[�h�ɕύX
        self.width(10) # �y����(�T�̋O�Օ�)��10
        self.getscreen().bgcolor('gray') # �L�����o�X�̔w�i�F���D�F
        self.pencolor('white') # �y���̐F(�T�̋O�Ղ̐F)�͔�
        self.w_2 = self.window_width() / 2.0 # �E�B���h�E���̔���
        self.h_2 = self.window_height() / 2.0 # �E�B���h�E�����̔���

    # �C�ӓ_�ɂ���T��Ǎۂ̓_(des_x,des_y)�܂ňړ������郁�\�b�h
    def hit_wall(self):
        line = Line(math.tan(self.heading()),self.xcor(),self.ycor())
        rand_angle = math.pi * random.random()
        # ��ӂɏՓ˂���ꍇ
        if self.towards(-self.w_2,self.h_2)>self.heading()>=self.towards(self.w_2,self.h_2):
            des_x = line.get_x(self.h_2)
            des_y = self.h_2
            turn_angle = self.heading() + rand_angle # �T�̓����E���ɖ߂��p�x

        # ���ӂɏՓ˂���ꍇ
        elif self.towards(-self.w_2,-self.h_2)>self.heading()>self.towards(-self.w_2,self.h_2):
            des_x = -self.w_2
            des_y = line.get_y(-self.w_2)
            turn_angle = self.heading() + rand_angle -math.pi / 2.0 # �T�̓����E���ɖ߂��p�x

        # ���ӂɏՓ˂���ꍇ
        elif self.towards(-self.w_2,-self.h_2)<self.heading()<self.towards(self.w_2,-self.h_2):
            des_x = line.get_x(-self.h_2)
            des_y = -self.h_2
            turn_angle = self.heading() - rand_angle # �T�̓����E���ɖ߂��p�x

        # �E�ӂɏՓ˂���ꍇ
        else:
            des_x = self.w_2
            des_y = line.get_y(self.w_2)
            turn_angle = math.pi / 2  + rand_angle # �T�̓����E���ɖ߂��p�x
        # �ǂɓ�����_�܂ňړ�
        self.goto(des_x,des_y)
        # ��]���āA�T�̓�������Ɍ�����
        self.right(turn_angle)


    def run(self):
        try:
            while True:
                self.hit_wall()
        except KeyboardInterrupt:
            pass

    def click_on_move(self,x,y):
        self.getscreen().bgcolor('gray')
        self.goto(x,y)


kame = Kame()
kame.getscreen().onclick(kame.click_on_move)
kame.run()

