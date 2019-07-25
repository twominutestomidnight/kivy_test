import face_recognition

# image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
image_of_bill = face_recognition.load_image_file('origin.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image_file(
    'sample.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

print(unknown_face_encoding)
# Compare faces
results = face_recognition.compare_faces(
    [bill_face_encoding], unknown_face_encoding)



if results[0]:
    print('This is origin')
else:
    print('This is NOT origin')
