import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)
image = np.full((300, 700, 3), white, np.uint8)

pt1, pt2 = (180, 150), (550, 150)
size = (120, 60)

cv2.circle(image, pt1, 1, 0, 2)
cv2.circle(image, pt2, 1, 0, 2)

cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1)      # 타원 그리기
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 4)   # 호 그리기
cv2.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

cv2.imshow("문자열", image)
cv2.waitKey()