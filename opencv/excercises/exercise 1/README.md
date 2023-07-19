ÖDEV 1

-Sistem Gereksinimleri:
    
    -python                        3.7 ya da daha üstü
    -opencv-python                 4.8.0.74


-Kodun buludnuğu klasörün içine istediğiniz dosyayı attıktan sonra,
        
    video = cv2.VideoCapture("sample.mp4")
kodunun içine video ismini vererek kod çalıştırıldığında saniyede 
beş kere ekran görüntüsü alarak onları frames dosyasına verir.



-Soru 1

    fps = video.get(cv2.CAP_PROP_FPS)
    print("The fps of the video is " + str(fps))
kod bloğu ile videonun fps'i .ekilir ve bastırılır.




-Soru 2

Video fps'i 5'e bölünüp assign edildikten sonra bir döngü ile video
bitene kadar o sayı kadar bulunduğumuz frame'e eklenir  yeni frame kaydedilir ve döngü devam eder.
    