import os
import cv2
import numpy as np

def add_padding(img_path, ann_path, maxH=0, maxW=0):

    images = os.listdir(img_path.split("\\")[0])
    for image in images:
        h,w,c=cv2.imread("Images\\" + image).shape
        if maxH < h:
            maxH = h
            img_with_height = image
        if maxW < w:
            maxW = w
            img_with_width = image

    print("img width = "+str(img_with_width))
    print("img height = "+str(img_with_height))

    image = cv2.imread(img_path)
    padd_img = image

    ann_file = ann_path + "gt_" + img_path.split("\\")[-1].split(".")[0]+".txt"
    with open(ann_file, encoding='utf-8') as f:
        boxes = f.readlines()

    #print(boxes[0].split(",")[0])
    print(image.shape)

    box1 = boxes[0].split(",")
    print(box1)
    one = image[int(box1[1]):int(box1[5]),int(box1[0]):int(box1[2])]

    ht,wd,c = image.shape
    result = np.full((maxH,maxW,c), (255,255,255), dtype=np.uint8)

    xx = (maxW - wd) // 2
    yy = (maxH - ht) // 2

    result[yy:yy+ht, xx:xx+wd] = image
    two = result[yy + int(box1[1]):yy + int(box1[5]),xx + int(box1[0]):xx + int(box1[2])]

    cv2.imshow('image', one)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('image', two)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #return padd_img

if __name__ == '__main__':
    img_path = r"Images\X00016469612.jpg"
    ann_path = r"GT\\"
    add_padding(img_path, ann_path)