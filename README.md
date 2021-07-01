# python_image_to_character

使用Python的PIL庫的Image模組，PIL(Python Imaging Library)庫

1.  先將彩色圖片轉換為黑白圖片，然後直接將每個畫素點的灰度值與字符集建立對映。

2. 獲取圖片的RGB值，利用公式：
Gray = R*0.299 + G*0.587 + B*0.114
計算可得每個畫素點的灰度值，之後再建立對映即可。