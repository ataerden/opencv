import cv2
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml')
eyeGlasses_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray [y:y + h, x:x+w]
        eyes = eyeGlasses_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 13)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 0, 255), 2)

    cv2.imshow('face detection', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()