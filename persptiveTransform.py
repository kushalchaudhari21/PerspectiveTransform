import cv2
import numpy as np
import time

#to take a webam shot for perspective transform use following command
#cap = cv2.VideoCapture(1)

time.sleep(1.1)
#_,img = cap.read()
#path to input file
mypath = "/Users/Desktop/tutorials and git/git ready codes/persp/"
img = cv2.imread(mypath + "img.jpeg")
img = cv2.resize(img, (768,576))
#initialising indexes to store inputs from clicks
pts = [(0,0),(0,0),(0,0),(0,0)]
pointIndex = 0
AR = (740,1280)
oppts = np.float32([[0,0],[AR[1],0],[0,AR[0]],[AR[1],AR[0]]])

#function to select four points on a image to capture desired region
def draw_circle(event,x,y,flags,param):
	global img
	global pointIndex
	global pts

	if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img,(x,y),5,(0,255,0),-1)
                pts[pointIndex] = (x,y)
                #print(pointIndex)
                pointIndex = pointIndex + 1
               
def show_window():                       
        while True:
                #print(pts,pointIndex-1)
                cv2.imshow('img', img)
                
                if(pointIndex == 4):
                        break
                
                if (cv2.waitKey(20) & 0xFF == 27) :
                        break

def get_persp(image,pts):
        ippts = np.float32(pts)
        Map = cv2.getPerspectiveTransform(ippts,oppts)
        warped = cv2.warpPerspective(image, Map, (AR[1], AR[0]))
        return warped

cv2.namedWindow('img')
cv2.setMouseCallback('img',draw_circle)
print('Top left, Top right, Bottom Right, Bottom left')

show_window()

while True:
        #_, frame = cap.read()
        warped = get_persp(img, pts)
        cv2.imshow("output",warped)
        #save output file in same path
        cv2.imwrite(mypath + "output.jpg",warped)
        key = cv2.waitKey(10) & 0xFF
        if key == 27:
                break
cv2.destroyAllWindows()
#cap.release()
                  

                  
