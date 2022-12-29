# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:16:19 2022

@author: erdem
"""

import cv2
import numpy as np

img = cv2.imread("coins.jpg")
img2 = cv2.imread("balLs.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#bozuklukları düzeltmek için softlamak için blur atıyoruz
img_blur= cv2.medianBlur(gray, 5)
img2_blur= cv2.medianBlur(gray2, 5)
#HOUGH_GRADIENT DAN BAŞKA DAİRE BELİRLEME ALGORİTMASI YOK
#1 ise çözünürlük oranı
#çemberler arası min emsafe giirlicek 
#ve bu min değeri img.shape[0]dan alınan değerleri 64 bölerek buluruz ve sonuçç min değeri olur
#param1 gradyandır param2 ise trashold value dur bu değerler bu metoda özel tanımlanmıştır 
#minRadius ve maxRadius Çemberllerin min max çevre değerleridir buna göre alınır çemberler
circle = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=15,maxRadius=80)

if circle is not None: #circle içindeki değerler boş değil ise
    circle = np.uint16(np.around(circle)) #circle da gelen ondalıklı değerleri yuvalrıyıp tekrar aynı değişkene atıyorum
    
    for i in circle[0,:]:#0.indexden son indexe kadar i gezicek
    
    #buradan gelicek ilk iki değer i[0] ,i [1] çemberin merkezini 
    #üçüncü gelecek değer i[2] ile yarı çaıpını belirliyorum
        cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),4)
cv2.imshow("img",img)
    









