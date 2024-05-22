import cv2 as cv
import connection


camera=cv.VideoCapture(0)
times=0
past_data=[]


while True:
    if not camera:
        break
    ret,frame= camera.read()

    if not ret:
        break
    #QR code detection
    detector=cv.QRCodeDetector()
    data,point,_=detector.detectAndDecode(frame)

    #Drawing the shape around the QR code
    if  point is not None:
        points = point[0].astype(int)
        for i in range(len(points)):
            cv.line(frame, tuple(points[i]), tuple(points[(i + 1) % len(points)]), color=(0, 255, 0), thickness=3)


    if data:
       # print(data)
        values=list(data.split())
        result=connection.Data_updation(values)
        
        if result=="incorrect password":
            #result=connection.Data_updation(values)
            pass
           
        if result =="Updated Already" or result== "Updated successfully":
            print(result)
            break
        elif result=="Error":
            break
        else:
            if past_data!=values or result =="incorrect password":

                print(result)
            past_data=values
            

    cv.imshow('Camera - QR Code Detection', frame)

    if cv.waitKey(100) & 0xFF == 27: 
        break
    times+=1
    if times==50:
        print("Invalid code or unable to scan the code")
        break