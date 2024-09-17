import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('PoseVideos/5.mp4')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1280, 720)
detector = PoseDetector()
posList = []

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)


    if bboxInfo:
        lmString = ''
        for lm in lmList:
            # print(lm)
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        posList.append(lmString)


    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if(key == ord('s')):
        with open("AnimationFile.txt",'w') as f:
            f.writelines(["%s\n" % item for item in posList])