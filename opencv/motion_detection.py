import cv2
import cv2 as cv

cap = cv.VideoCapture('images/street_cam.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(cap.get(5))
while cap.isOpened():
    diff = cv.absdiff(frame1,frame2)
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 20,255, cv2.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours,_ = cv.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv.contourArea(contour) < 1000 or w > h:
            continue
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.putText(frame1, 'There is movement', (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    # cv.drawContours(frame1, contours,-1, (0,255,0),2)
    cv.imshow("motion detector",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv.waitKey(40) == ord('q'):
        print("error")
        break

cv2.destroyAllWindows()
