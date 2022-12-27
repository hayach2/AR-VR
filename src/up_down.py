import cv2
import glfw
import face_recognition

myfile = "test.txt"
viewerfile = "viewerfile.txt"

def head_movements():
    Camera = cv2.VideoCapture(0)
    _, frame = Camera.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    box = face_recognition.face_locations(frameRGB)
    if len(box) < 1 or len(box[0]) < 4:
        head_movements()
    reset = 1
    var = 0
    begin = 1
    MIN_MOVE = 25

    while True:
        _, frame = Camera.read()

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        box = face_recognition.face_locations(frameRGB)

        f = open("viewerfile.txt", "r")
        if (box != []):
            if f.read() == "1":
                f.close()
                if reset:
                    print('RESET')
                    cx_ = (box[0][3] + box[0][1]) / 2
                    cy_ = (box[0][0] + box[0][2]) / 2
                    cx = cx_
                    cy = cy_
                else:
                    cx = (box[0][3] + box[0][1]) / 2
                    cy = (box[0][0] + box[0][2]) / 2

                f = open("test.txt", "w")
                f.write("")
                print(cx_, cy_)
                print(cx, cy)

                #if abs(cx - cx_) > 100 or abs(cy - cy_) > 100:
                #    print('MOVEMENT TOO WIDE ---> NEW POSITION')
                #    reset = 1

                if abs(cx - cx_) < abs(cy - cy_):   # VERTICAL
                    if cy - cy_ > MIN_MOVE and (begin == 1 or var == 1):
                        if begin:
                            var = 1
                            begin = 0
                        f.write("0")
                        print('DOWN')
                    elif cy - cy_ < -MIN_MOVE and (begin == 1 or var == 2):
                        if begin:
                            var = 2
                            begin = 0
                        f.write("1")
                        print('UP')
                else:                               # HORIZONTAL
                    if cx - cx_ > MIN_MOVE and (begin == 1 or var == 3):
                        if begin:
                            var = 3
                            begin = 0
                        f.write("2")
                        print('LEFT')
                    elif cx - cx_ < -MIN_MOVE and (begin == 1 or var == 4):
                        if begin:
                            var = 4
                            begin = 0
                        f.write("3")
                        print('RIGHT')
                reset = 0
                f.close()
            else:
                reset = 1
                var = 0
                begin = 1
                print('TOOL DEACTIVATED')
                f.close()
                f = open("test.txt", "w")
                f.write("")
                f.close()

        cv2.imshow("unlock Face", frame)

head_movements()
