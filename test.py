import cv2 
c= cv2.VideoCapture(1)

while(1) :
	_,f = c.read()
	gray_frame = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
	cv2.imshow('e2', f)
	if cv2.waitKey(5)==27:
		break

cv2.destroyAllWindows()
