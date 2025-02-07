import sys, cv2
import numpy as np

# 컬러 영상의 히스토그램 평활화
src = cv2.imread('images_ch06/dolls.jpg')

if src is None:
    print("Image load failed")
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)   # 색감 유지
y_planes, cr_planes, cb_planes = cv2.split(src_ycrcb)

y_planes = cv2.equalizeHist((y_planes))              # 밝기만 평활화

dst = cv2.merge((y_planes, cr_planes, cb_planes))
dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()