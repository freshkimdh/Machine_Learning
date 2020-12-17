import cv2

# img_basic = cv2.imread('cat1.jpg', cv2.IMREAD_COLOR)
img = 'Python_openCV/cat1.jpg'
img_basic = cv2.imread(img)

# print('shape:',img_basic.shape)
cv2.imshow('image Basic', img_basic)
cv2.waitKey(0)
cv2.release()
cv2.destroyAllWindows()


