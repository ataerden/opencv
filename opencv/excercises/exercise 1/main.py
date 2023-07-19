import cv2
video = cv2.VideoCapture("scenery.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
print("The fps of the video is " + str(fps))
totalFrame = video.get(cv2.CAP_PROP_FRAME_COUNT)
print("number of total frames is " + str(totalFrame))
frame_id = 0
captureRate = fps//5

while video.isOpened() and frame_id <= totalFrame-2:
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    # cv2.imshow("camera", frame)
    cv2.imwrite('frames\\' + str(frame_id//5) + '.png', frame)
    if  not ret:
        break

    else:
        print('Position:', int(video.get(cv2.CAP_PROP_POS_FRAMES)))
    frame_id += captureRate

print("The capturing process is finished.")
video.release()
# cv2.destroyAllWindows()
