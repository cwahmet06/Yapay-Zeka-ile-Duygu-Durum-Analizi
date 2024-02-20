                          # KÜTÜPHANELER
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
                          # Görüntü veri oluşturucuyu yeniden ölçeklendirmeyle başlat
egitimVeriGen1 = ImageDataGenerator(rescale=1./255)
dogrulamaVeriGen1 = ImageDataGenerator(rescale=1./255)
                          # Tüm test görüntülerini önceden işleyin
egitimGeneratoru = egitimVeriGen1.flow_from_directory(
        r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\data\train',
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')
                          # Tüm eğitim görüntülerini önceden işleyin
dogrulamaGeneratoru = dogrulamaVeriGen1.flow_from_directory(
        r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\data\test',
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

                          # Model yapısı oluştur
duyguModeli = Sequential()

duyguModeli.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
duyguModeli.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
duyguModeli.add(MaxPooling2D(pool_size=(2, 2)))

duyguModeli.add(Dropout(0.25))
duyguModeli.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
duyguModeli.add(MaxPooling2D(pool_size=(2, 2)))
duyguModeli.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
duyguModeli.add(MaxPooling2D(pool_size=(2, 2)))
duyguModeli.add(Dropout(0.25))

duyguModeli.add(Flatten())
duyguModeli.add(Dense(1024, activation='relu'))
duyguModeli.add(Dropout(0.5))
duyguModeli.add(Dense(7, activation='softmax'))
cv2.ocl.setUseOpenCL(False)

                          # Optimize ediciyi ayarlayın
duyguModeli.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), metrics=['accuracy'])
                          # Sinir ağını/modelini eğitin
duyguModelBilgi = duyguModeli.fit(
        egitimGeneratoru,
        steps_per_epoch=28709 // 64,
        epochs=200,
        validation_data=dogrulamaGeneratoru,
        validation_steps=7178 // 64)
                          # Model yapısını json dosyasına kaydet
modelJson = duyguModeli.to_json()
with open("../model/emotion_model.json", "w") as json_file:
    json_file.write(modelJson)
                         # Eğitilmiş model ağırlığını .h5 dosyasına kaydedin
duyguModeli.save_weights('emotion_model.h5')