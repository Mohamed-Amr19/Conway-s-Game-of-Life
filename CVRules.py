import numpy as np
import cv2 as cv
# Create a black image
rule1="1)The game takes place on a grid (the grid must be 50x50 squares at least)"
rule2="2)Each cell (square) in the grid can be in one of two possible states:"
rule22="  Alive or Dead. A living state is indicated by a blue square a dead state by a blank square"
rule3="3)Every simulation begins with a set of live cells. This is referred to as the initial\n population" 
rule32="Technically, you could begin with all cells being dead, but that would make for a dull simulation"
rule4="4)Every simulation begins with a set of live cells. This is referred to as the initial"
rule42="population. (Technically, you could begin with all cells being dead, but that would make"
rule43="for a dull simulation.)"
rule5="5)Then, the pattern evolves according to a certain set of rules. The set of rules determines"
rule52="what happens to each cell from one generation (configuration of live and dead cells) to"
rule53="the next. vi. The rules:"
img = np.zeros((750,1024,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,rule1,(10,100), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule2,(10,130), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule22,(10,150), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule3,(10,180), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule32,(10,200), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule4,(10,230), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule42,(10,250), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule43,(10,270), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule5,(10,300), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule52,(10,320), font, 0.65,(255,255,255),2,cv.LINE_AA)
cv.putText(img,rule53,(10,340), font, 0.65,(255,255,255),2,cv.LINE_AA)

for i in range(0,200,40):
    cv.line(img,(40+i,380),(40+i,590),(255,255,255),2)
for i in range(0,200,40):
    cv.line(img,(10,410+i),(220,410+i),(255,255,255),2)

cv.circle(img,(60,470),10,(255,255,255))
cv.circle(img,(60,510),10,(255,255,255))
cv.circle(img,(100,550),10,(255,255,255))

cv.circle(img,(180,510),10,(255,255,255))
cv.circle(img,(180,470),10,(255,255,255))
cv.circle(img,(140,430),10,(255,255,255))

cv.line(img,(250,500),(400,500),(255,255,255),2)
cv.line(img,(400,500),(350,470),(255,255,255),2)
cv.line(img,(400,500),(350,530),(255,255,255),2)

cv.putText(img,"Next Gen",(265,495), font, 0.65,(255,255,255),2,cv.LINE_AA)

for i in range(0,200,40):
    cv.line(img,(440+i,380),(440+i,590),(255,255,255),2)
for i in range(0,200,40):
    cv.line(img,(420,410+i),(620,410+i),(255,255,255),2)

cv.circle(img,(460,510),10,(255,255,255))
cv.circle(img,(500,510),10,(255,255,255))
cv.circle(img,(540,510),10,(255,255,255))

cv.circle(img,(540,470),10,(255,255,255))
cv.circle(img,(500,470),10,(255,255,255))
cv.circle(img,(580,470),10,(255,255,255))

cv.imshow("window_name", img)
cv.waitKey(0)