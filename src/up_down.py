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
    cx_ = (box[0][3] + box[0][1]) / 2
    cy_ = (box[0][0] + box[0][2]) / 2
    cx = cx_
    cy = cy_

    MIN_MOVE = 50
    MIN_MOVE_V = 25

    while True:
        _, frame = Camera.read()

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        box = face_recognition.face_locations(frameRGB)

        hor = 0
        f = open("viewerfile.txt", "r")
        if (box != []):
            if f.read() == "1":
                f.close()
                cx = (box[0][3] + box[0][1]) / 2
                cy = (box[0][0] + box[0][2]) / 2
                # cv2.rectangle(frame, (box[0][3], box[0][2]), (box[0][1], box[0][0]), (0, 0, 255), 2)

                # if person moves head to right or left: disable the navigation
                # if person doesn't go left and right for 1 second, then he's focused
                f = open("test.txt", "w")
                f.write("")
                print(cx_, cy_)
                print(cx, cy)

                if abs(cx - cx_) > 110 or abs(cy - cy_) > 110:
                    print('MOVEMENT TOO WIDE ---> NEW POSITION')
                    cx_ = (box[0][3] + box[0][1]) / 2
                    cy_ = (box[0][0] + box[0][2]) / 2
                    hor = 0

                if abs(cx - cx_) < abs(cy - cy_):
                    if hor == 0:
                        if cy - cy_ > MIN_MOVE_V:
                            f.write("0")
                            print('DOWN')
                        elif cy - cy_ < -MIN_MOVE_V:
                            f.write("1")
                            print('UP')
                    else:
                        hor = hor-1
                        cy_ = cy
                    cx_ = cx
                else:
                    hor=3
                    if cx - cx_ > MIN_MOVE:
                        f.write("2")
                        print('LEFT')
                    elif cx - cx_ < -MIN_MOVE:
                        f.write("3")
                        print('RIGHT')
                f.close()
            else:
                cx_ = (box[0][3] + box[0][1]) / 2
                cy_ = (box[0][0] + box[0][2]) / 2
                f.close()

        cv2.imshow("unlock Face", frame)

head_movements()
