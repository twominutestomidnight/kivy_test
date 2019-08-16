from Image import getImageFromCamera
import time
from facematch import faceCompare


if __name__ == '__main__':
    while True:
        getImageFromCamera()
        result, accuracy = faceCompare(imageToCompare='sample2.jpg',
                                       imageOrigin='origin.jpg')
        if result:
            person = " its origin"
        else:
            person = "no face or fake"
        print("person : ", person,"accuracy", accuracy )
        time.sleep(5)