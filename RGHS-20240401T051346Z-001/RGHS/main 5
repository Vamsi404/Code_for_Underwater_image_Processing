import cv2
vidcap = cv2.VideoCapture('C:\\Users\\dell\\Desktop\\RGHS\\video input\\WhatsApp Video 2022-06-05 at 5.56.56 PM - Copy.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
