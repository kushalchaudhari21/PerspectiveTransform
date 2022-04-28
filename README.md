## Description

This is an python script to get a perspective transformed version for given input image

The demo for the project can be found in folder [demo](https://github.com/kushalchaudhari21/PerspectiveTransform/tree/master/demo).

## Sample Invocation

In the terminal, in the project directory input the following to execute the script
```
python perspectiveTransform.py
```
![executionCommand](https://github.com/kushalchaudhari21/PerspectiveTransform/blob/master/demo/executionCommand.png)

## Usage

**1.** Refer to the sample invocation section and run the program.

**2.** Next, a window pops up on the screen on which you can select 4 points in given sequence to select the region of interest(ROI).

![selectPoints](https://github.com/kushalchaudhari21/PerspectiveTransform/blob/master/demo/selectPoints.gif) 

**3.** Perspective transform function is written as:
```
def get_persp(image,pts):
        ippts = np.float32(pts)
        Map = cv2.getPerspectiveTransform(ippts,oppts)
        warped = cv2.warpPerspective(image, Map, (AR[1], AR[0]))
        return warped
```

**4.** After the execution, the output image is added in same directory.

## Important Insights

* Order in which points are selected can be changed using different value of pointIndex.
* These points can be stored as annotations by exporting them into different file formats like csv.
