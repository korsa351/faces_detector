import cv2, os
from django.contrib.staticfiles import finders

number = 0
images = []
blurimages = []


def VIDEO():
    face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml. ")

    path = os.path.abspath("./media/videos/rtr.mp4")
    cap = cv2.VideoCapture(path)
    flag = True
    frame = 0
    # Im = cv2.imread(os.path.abspath("./static/img/TTR.png"))
    # Im = cv2.resize(Im, (400, 300))
    n = 0
    f = 0

    # for i in range(11):
    #     put = os.path.abspath('./media/img/')
    #     name = f'{put}\\images{n}.png'
    #     cv2.imwrite(name, Im)
    #     name = f'{put}\\BLUR_images{n}.png'
    #     cv2.imwrite(name, Im)
    #     n += 1

    def BLUR(img):
        (h, w) = img.shape[:2]
        dw = int(w / 3.0)
        dh = int(h / 3.0)
        if dw % 2 == 0:
            dw -= 1
        if dh % 2 == 0:
            dh -= 1
        return cv2.GaussianBlur(img, (dw, dh), 0)

    def SAVE(img, img_1):
        global number, blurimages, images
        put = os.path.abspath('./static/img/')
        img = cv2.resize(img, (400, 300))
        File_name = f'{put}\\image{number}.png'
        cv2.imwrite(File_name, img)
        img_1 = cv2.resize(img_1, (400, 300))
        File_name = f'{put}\\BLUR_image{number}.png'
        cv2.imwrite(File_name, img_1)
        images.append(f"img\\image{number}.png")
        blurimages.append(f"img\\BLUR_image{number}.png")
        number += 1

    while True:
        success, img = cap.read()
        face = face_cascade_db.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1)
        try:
            img_1 = img.copy()
        except:
            return images, blurimages
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
            img[y:y + h, x:x + w] = BLUR(img[y:y + h, x:x + w])
        cv2.imshow('rez', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        if flag:
            SAVE(img_1, img)
            flag = False
        if frame == 25:
            SAVE(img_1, img)
            frame = 0
            f += 25
        else:
            frame += 1

    cap.release()
    cv2.destroyAllWindows()
    return images, blurimages
