import face_recognition
from origin_encoding import enc


# image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
# image_of_bill = face_recognition.load_image_file('origin.jpg')
# bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]
# print(bill_face_encoding)
# bill_face_encoding = enc
#
#
# unknown_image = face_recognition.load_image_file('sample2.jpg')
# # unknown_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
# # unknown_image = face_recognition.load_image_file('origin.jpg')
# unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#
# print(unknown_face_encoding)
# # Compare faces
# results = face_recognition.compare_faces(
#     [bill_face_encoding], unknown_face_encoding)
#
#
# if results[0]:
#     print('This is origin')
# else:
#     print('This is NOT origin')


def faceCompare(imageToCompare, imageOrigin):
    # image_of_bill = face_recognition.load_image_file(imageOrigin)
    # bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]
    # print(bill_face_encoding)
    print("==================")
    bill_face_encoding = enc
    unknown_image = face_recognition.load_image_file(imageToCompare)
    try:
        print("before unknown_face_encoding")
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        print("after unknown_face_encoding")
        print(unknown_face_encoding)
        print("before compare_faces")

        # Compare faces
        results, accuracy = face_recognition.compare_faces(
            [bill_face_encoding], unknown_face_encoding)
        print("after compare_faces")
        # import math
        # def face_distance_to_conf(face_distance, face_match_threshold=0.6):
        #     if face_distance > face_match_threshold:
        #         range = (1.0 - face_match_threshold)
        #         linear_val = (1.0 - face_distance) / (range * 2.0)
        #         return linear_val
        #     else:
        #         range = face_match_threshold
        #         linear_val = 1.0 - (face_distance / (range * 2.0))
        #         return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

        # if results[0]:
        #     print('This is origin')
        # else:
        #     print('This is NOT origin')

        return results[0], accuracy
    except:
        return False, ['Faces not found, cant encoding']