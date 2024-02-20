import cv2
import numpy as np
from keras.models import model_from_json
                          # 7 adet class oluşturuluyor ekrana basılacak olan durumlar
duyguKutuphanesi = {0: "Sinirli", 1: "Igrenmis", 2: "Korkmus", 3: "Mutlu", 4: "Dogal", 5: "Uzgun", 6: "Sasirmis"}
                          # json'u yükleyin ve model oluşturun
jsonDosyasi = open(r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\model\emotion_model.json')
yuklenmisJasonModel = jsonDosyasi.read()
jsonDosyasi.close()
duyguModeli = model_from_json(yuklenmisJasonModel)
                          # Ağırlıkları modele yükleyin
duyguModeli.load_weights(r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\model\emotion_model.h5')
print("Model başarı ile yüklendi kamera açılıyor...")
                          # Kamerayı başlat
yapakala = cv2.VideoCapture(0) # 0 kamerayı başlatır. / 1 herhangi bir video başlatmak içindir ( beta )
while True:
                          # Kameradan alınan verileri işle
    ret, frame = yapakala.read()
    if not ret:
        break
                          # Frame de yüzü bul bunun için HAARCASCADES'i kullan
    yuzCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    griFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    yuz = yuzCascade.detectMultiScale(griFrame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                          # Yüz boyutlarını bul
    for (x, y, w, h) in yuz:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gri = griFrame[y:y + h, x:x + w]
        roi_gri = cv2.resize(roi_gri, (48, 48))
        roi_gri = np.expand_dims(roi_gri, axis=0)
        roi_gri = np.expand_dims(roi_gri, axis=-1)
                          # Duyguyu tahmin et
        duyugTahmini = duyguModeli.predict(roi_gri)
        max_index = int(np.argmax(duyugTahmini[0]))
        duyguBaslik = duyguKutuphanesi[max_index]
        cv2.putText(frame, duyguBaslik, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                         # 'q' ile kamerayı kapat
    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
yapakala.release()
cv2.destroyAllWindows()