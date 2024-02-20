# KÜTÜPHANELER
import numpy as np
from keras.models import model_from_json
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
# 7 adet class oluşturuluyor ekrana basılacak olan durumlar
duyguKutuphanesi = {0: "Sinirli", 1: "Igrenmis", 2: "Korkmus", 3: "Mutlu", 4: "Dogal", 5: "Uzgun", 6: "Sasirmis"}
# json'u yükleyin ve model oluşturun
jsonDosyasi = open(
    r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\model\emotion_model.json')
jsonModelYukle = jsonDosyasi.read()
jsonDosyasi.close()
duyguModeli = model_from_json(jsonModelYukle)
# Ağırlıkları modele yükleyin
duyguModeli.load_weights(
    r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\model\emotion_model.h5')
print("Model başarı ile yüklendi...")
# Yeniden ölçeklendirmeyle görüntü veri oluşturucuyu başlat
testVeriGen1 = ImageDataGenerator(rescale=1. / 255)
# Tüm test görüntülerini önceden işleyin
testGeneratoru = testVeriGen1.flow_from_directory(
    r'C:\Users\ahmet\OneDrive\Masaüstü\DERS\bitirmeProjesi\KOD\duyguDurumAnalizi\data\test',
    target_size=(48, 48),
    batch_size=64,
    color_mode="grayscale",
    class_mode='categorical'
)
# Test verileri üzerinde tahmin yapın
tahmin = duyguModeli.predict(testGeneratoru)
# Tahminlere bakınız.
# for result in predictions:
#     max_index = int(np.argmax(result))
#     print(emotion_dict[max_index])
print("-----------------------------------------------------------------")
# Karışıklık matrisi
c_matrix = confusion_matrix(testGeneratoru.classes, tahmin.argmax(axis=1))
print(c_matrix)
cm_display = ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=duyguKutuphanesi)
cm_display.plot(cmap=plt.cm.Blues)
plt.show()
# Sınıflandırma raporu
print("-----------------------------------------------------------------")
print(classification_report(testGeneratoru.classes, tahmin.argmax(axis=1)))