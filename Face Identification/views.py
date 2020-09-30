from django.shortcuts import render, redirect
import cv2
import numpy as np
from . import dataset_fetch as df
from . import cascade as casc
from PIL import Image



from . settings import BASE_DIR

def index(request):
    return render(request, 'index.html')
def errorImg(request):
    return render(request, 'error.html')

def create_dataset(request):
    
    userId = request.POST['userId']
    print(("cv2.__version__"))
    
    faceDetect = cv2.CascadeClassifier(BASE_DIR+'/ml/haarcascade_frontalface_default.xml')
    
    cam = cv2.VideoCapture(0)

    
    id = userId
    
    sampleNum = 0
    
    while(True):
        
        ret, img = cam.read()
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        
        for(x,y,w,h) in faces:
            
            sampleNum = sampleNum+1
            
            cv2.imwrite(BASE_DIR+'/ml/dataset/user.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y:y+h,x:x+w])
            
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)
            
            cv2.waitKey(250)

        
        cv2.imshow("Face",img)
        cv2.waitKey(1)
       
        if(sampleNum>35):
            break
    
    cam.release()
    cv2.destroyAllWindows()

    return redirect('/')

def trainer(request):
    
    import os    
    from PIL import Image

  
    recognizer = cv2.face.LBPHFaceRecognizer_create()
  
    path = BASE_DIR+'/ml/dataset'

    def getImagesWithID(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        

        faces = []
        Ids = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L') 
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1]) 
            
            faces.append(faceNp)
            Ids.append(ID)
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return np.array(Ids), np.array(faces)

    ids, faces = getImagesWithID(path)

    recognizer.train(faces, ids)

    recognizer.save(BASE_DIR+'/ml/recognizer/trainingData.yml')
    cv2.destroyAllWindows()

    return redirect('/')


def detect(request):
    faceDetect = cv2.CascadeClassifier(BASE_DIR+'/ml/haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read(BASE_DIR+'/ml/recognizer/trainingData.yml')
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

            getId,conf = rec.predict(gray[y:y+h, x:x+w]) 
            
            if conf<35:
                userId = getId
                cv2.putText(img, "Detected",(x,y+h), font, 2, (0,255,0),2)
            else:
                cv2.putText(img, "Unknown",(x,y+h), font, 2, (0,0,255),2)

            

        cv2.imshow("Face",img)
        if(cv2.waitKey(1) == ord('q')):
            break
        elif(userId != 0):
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()
            return redirect('/records/details/'+str(userId))

    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')

