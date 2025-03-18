import numpy as np, cv2

src = cv2.imread("images/coins.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 50, minRadius = 10, maxRadius = 150)
print(circles)

for i in circles[0]:
    pt1 = int(i[0])
    pt2 = int(i[1])
    pt3 = int(i[2])

    cv2.circle(dst, (pt1, pt2), pt3, (0, 0, 0), 10)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
