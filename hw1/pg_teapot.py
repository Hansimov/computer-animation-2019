# 用PyOpenGL叩开3D的心扉——OpenGL全解析（3）
#   https://eyehere.net/2011/learn-opengl-3d-by-pyopengl-3/

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # glRotatef(1, 0, 1, 0)
    glutWireTeapot(0.5)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("First")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()