#!/usr/bin/env python3

import glfw
from viewer import Viewer
from skybox import Skybox

def main():
    viewer = Viewer(width=1920, height=1080)
    # -------------------------------------------------
    field = [
        '../resources/skybox/ft.jpg',
        '../resources/skybox/ft.jpg',
        '../resources/skybox/ft.jpg',
        '../resources/skybox/ft.jpg',
        '../resources/skybox/ft.jpg',
        '../resources/skybox/ft.jpg']

    viewer.add(Skybox(field))
    f = open("viewerfile.txt", "w")
    f.write("1")
    f.close()
    viewer.run()


if __name__ == '__main__':
    glfw.init()  # initialize window system glfw
    main()  # main function keeps variables locally scoped
    glfw.terminate()  # destroy all glfw windows and GL contexts
