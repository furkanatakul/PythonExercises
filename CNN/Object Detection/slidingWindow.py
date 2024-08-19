import cv2 as cv

def slidingWindow(image,step,ws):

    for y in range(0,image.shape[0] - ws[1],step):
        for x in range(0,image.shape[1] - ws[0], step):
            yield(x,y,image[y:y+ws[1], x:x+ws[0]])

# img = cv.imread("Images/kus.jpg")
# im = slidingWindow(img, 5, (200,150))
#
# for i,image in enumerate(im):
#     print(i)