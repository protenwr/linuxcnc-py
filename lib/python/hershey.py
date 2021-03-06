#    This is a component of AXIS, a front-end for emc
#    Copyright 2005, 2006 Chris Radek <chris@timeguy.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import itertools
from OpenGL.GL import *
from OpenGL.GLU import *

translate = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '-': 10, '.': 11, 'X': 12, 'Y': 13, 'Z': 14, 'G': 15,
        'U': 16, 'V': 17, 'W': 18}

class Hershey:
    def __init__(self):
        self.hershey = (
    # 0
        [[(240.0, 20.0), (180.0, 40.0), (140.0, 100.0), (120.0, 200.0),
          (120.0, 260.0), (140.0, 360.0), (180.0, 420.0), (240.0, 440.0),
          (280.0, 440.0), (340.0, 420.0), (380.0, 360.0), (400.0, 260.0),
          (400.0, 200.0), (380.0, 100.0), (340.0, 40.0), (280.0, 20.0),
          (240.0, 20.0)]], 
    # 1
        [[(120.0, 100.0), (160.0, 80.0), (220.0, 20.0), (220.0, 440.0)]], 
    # 2
        [[(140.0, 120.0), (140.0, 100.0), (160.0, 60.0), (180.0, 40.0),
          (220.0, 20.0), (300.0, 20.0), (340.0, 40.0), (360.0, 60.0),
          (380.0, 100.0), (380.0, 140.0), (360.0, 180.0), (320.0, 240.0),
          (120.0, 440.0), (400.0, 440.0)]], 
    # 3
        [[(160.0, 20.0), (380.0, 20.0), (260.0, 180.0), (320.0, 180.0),
          (360.0, 200.0), (380.0, 220.0), (400.0, 280.0), (400.0, 320.0),
          (380.0, 380.0), (340.0, 420.0), (280.0, 440.0), (220.0, 440.0),
          (160.0, 420.0), (140.0, 400.0), (120.0, 360.0)]], 
    # 4
        [[(320.0, 20.0), (120.0, 300.0), (420.0, 300.0)], [(320.0, 20.0),
          (320.0, 440.0)]], 
    # 5
        [[(360.0, 20.0), (160.0, 20.0), (140.0, 200.0), (160.0, 180.0),
          (220.0, 160.0), (280.0, 160.0), (340.0, 180.0), (380.0, 220.0),
          (400.0, 280.0), (400.0, 320.0), (380.0, 380.0), (340.0, 420.0),
          (280.0, 440.0), (220.0, 440.0), (160.0, 420.0), (140.0, 400.0),
          (120.0, 360.0)]], 
    # 6
        [[(380.0, 80.0), (360.0, 40.0), (300.0, 20.0), (260.0, 20.0),
          (200.0, 40.0), (160.0, 100.0), (140.0, 200.0), (140.0, 300.0),
          (160.0, 380.0), (200.0, 420.0), (260.0, 440.0), (280.0, 440.0),
          (340.0, 420.0), (380.0, 380.0), (400.0, 320.0), (400.0, 300.0),
          (380.0, 240.0), (340.0, 200.0), (280.0, 180.0), (260.0, 180.0),
          (200.0, 200.0), (160.0, 240.0), (140.0, 300.0)]], 
    # 7
        [[(400.0, 20.0), (200.0, 440.0)], [(120.0, 20.0), (400.0, 20.0)]], 
    # 8
        [[(220.0, 20.0), (160.0, 40.0), (140.0, 80.0), (140.0, 120.0),
          (160.0, 160.0), (200.0, 180.0), (280.0, 200.0), (340.0, 220.0),
          (380.0, 260.0), (400.0, 300.0), (400.0, 360.0), (380.0, 400.0),
          (360.0, 420.0), (300.0, 440.0), (220.0, 440.0), (160.0, 420.0),
          (140.0, 400.0), (120.0, 360.0), (120.0, 300.0), (140.0, 260.0),
          (180.0, 220.0), (240.0, 200.0), (320.0, 180.0), (360.0, 160.0),
          (380.0, 120.0), (380.0, 80.0), (360.0, 40.0), (300.0, 20.0),
          (220.0, 20.0)]], 
    # 9
        [[(380.0, 160.0), (360.0, 220.0), (320.0, 260.0), (260.0, 280.0),
          (240.0, 280.0), (180.0, 260.0), (140.0, 220.0), (120.0, 160.0),
          (120.0, 140.0), (140.0, 80.0), (180.0, 40.0), (240.0, 20.0),
          (260.0, 20.0), (320.0, 40.0), (360.0, 80.0), (380.0, 160.0),
          (380.0, 260.0), (360.0, 360.0), (320.0, 420.0), (260.0, 440.0),
          (220.0, 440.0), (160.0, 420.0), (140.0, 380.0)]], 
    # -
        [[(80, 260), (440, 260)]], 
    # .
        [[(120, 400), (100, 420), (120, 440), (140, 420), (120, 400)]], 
    # X
        [[(60, 20), (340, 440)], [(340, 20), (60, 440)]], 
    # Y
        [[(40, 20), (200, 220), (200, 440)], [(360, 20), (200, 220)]], 
    # Z
        [[(340, 20), (60, 440)], [(60, 20), (340, 20)], 
         [(60, 440), (340, 440)]],
    # G
        [[(380.0, 80.0), (360.0, 40.0), (300.0, 20.0), (260.0, 20.0),
          (200.0, 40.0), (160.0, 100.0), (140.0, 200.0), (140.0, 300.0),
          (160.0, 380.0), (200.0, 420.0), (260.0, 440.0), (280.0, 440.0),
          (340.0, 420.0), (380.0, 380.0), (400.0, 320.0),
          (400.0, 280.0), (270.0, 280.0)]],
    # U
        [[(60, 20), (60, 400), (95, 410), (130, 420), (165, 430),
          (200, 440), (200, 440), (235, 430), (270, 420), (305, 410),
          (340, 400), (340, 20)]],
    # V
        [[(60, 20), (200, 440), (340, 20)]],
    # W
        [[(60, 20), (60, 400), (100, 440), (160, 440), (200, 400),
          (240, 440), (300, 440), (340, 400), (340, 20)],
         [(200, 400), (200, 300)]],
       ) 
        self.lists = glGenLists(len(self.hershey))

        for i in range(len(self.hershey)):
            digit = self.hershey[i]
            glNewList(self.lists + i, GL_COMPILE)
            for stroke in digit:
                glBegin(GL_LINE_STRIP)
                for point in stroke:
                    glVertex3f(point[0], 440-point[1], 0)
                glEnd()
            glEndList()

    def plot_digit(self, n):
        glPushMatrix()
        glScalef(1/440.0, 1/440.0, 1/440.0)
        glCallList(self.lists + n)
        glPopMatrix()

    def plot_string(self, s, frac=0, bbox=0):
        glPushMatrix()
        mat = glGetDoublev(GL_MODELVIEW_MATRIX)
        mat = [i for i in itertools.chain(*mat.tolist())]
        if mat[10] < -.001:
            glTranslatef(0, .5, 0)
            glRotatef(180, 0, 1, 0)
            glTranslatef(0, -.5, 0)
            frac = 1 - frac
            mat = glGetDoublev(GL_MODELVIEW_MATRIX)
            mat = [i for i in itertools.chain(*mat.tolist())]
        if mat[5] < -.001:
            glTranslatef(0, .5, 0)
            glRotatef(180, 0, 0, 1)
            glTranslatef(0, -.5, 0)
            frac = 1 - frac
        if frac:
            len = self.string_len(s)
            glTranslatef(-len*frac, 0, 0)
        glScalef(1/440.0, 1/440.0, 1/440.0)
        if bbox:
            glBegin(GL_LINE_STRIP)
            glVertex3f(-140, -140, 0)
            glVertex3f(self.string_len(s)*440.0 + 140, -140, 0)
            glVertex3f(self.string_len(s)*440.0 + 140, 580.0, 0)
            glVertex3f(-140, 580.0, 0)
            glVertex3f(-140, -140, 0)
            glEnd()
        for c in s:
            glCallList(self.lists + translate[c])
            if c == '1':
                glTranslatef(260, 0, 0)
            elif c == '.':
                glTranslatef(180, 0, 0)
            else:
                glTranslatef(400, 0, 0)
        glPopMatrix()

    def string_len(self, s):
        l = 0.0
        for c in s:
            if c == '1':
                l += 260.0
            elif c == '.':
                l += 180.0
            else:
                l += 400.0

        return l/440.0

    def center_string(self, s):
        len = self.string_len(s)
        glTranslatef(-len/2, -.5, 0)

