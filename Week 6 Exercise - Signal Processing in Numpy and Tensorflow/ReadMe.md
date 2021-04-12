# Week 6 Exercise - Signal Processing in Numpy and Tensorflow
 
> * NOTEBOOK: https://github.com/ual-cci/MSc-Coding-2/blob/master/Week-6-Exercise-intro-to-image-data-and-tensorflow.ipynb
> * Make a version of the Notebook with at least one major difference that you have introduced yourself (as follows):
> * First, you must do some transformation on the image dataset that isn't included in the above document. You must use numpy to do this transformation.

And here is my Notebook 👇👇


# Dream by Picasso ✨

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/dream.jpg)

**I processed this image using numpy**

* 1. Gray

```
gray= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
plt.subplot(121)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(gray)
plt.title("Gray Image")
plt.show()
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/gray.png)

* 2. Fliplr

```
plt.subplot(131) 
plt.title("Original Image") 
plt.imshow(img)

hflipped_image= np.fliplr(img) #fliplr reverse the order of columns of pixels in matrix
plt.subplot(132) 
plt.title("Horizontally flipped")
plt.imshow(hflipped_image)

vflipped_image= np.flipud(img) #flipud reverse the order of rows of pixels in matrix
plt.subplot(133)
plt.title("Vertically flipped")
plt.imshow(vflipped_image)
plt.show()
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/fliplr.png)

* 3. Rotate

```
r_image = rotate(img, angle=45) # angle value is positive for anticlockwise rotation 
r_image1 = rotate(img, angle=-45) #angle value is negative for clockwise rotation
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/rotate.png)

* 4. Wrap

```
transform = AffineTransform(translation=(-200,0))  
warp_image = warp(img,transform, mode="wrap") #mode parameter is optional
# mode= {'constant', 'edge', 'symmetric', 'reflect', 'wrap'}

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(img)
plt.subplot(1,2,2)
plt.title('Wrap Shift')
plt.imshow(warp_image)
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/wrap.png)

* 5. Symmetric

```
transform = AffineTransform(translation=(-200,0))  
symmetric_image = warp(img,transform, mode="symmetric") #mode parameter is optional
# mode= {'constant', 'edge', 'symmetric', 'reflect', 'wrap'}

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(img)
plt.subplot(1,2,2)
plt.title('Symmetric Shift')
plt.imshow(symmetric_image)
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/symmetric.png)

* 6. Noise

```
noisy_image= random_noise(img)
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/noise.png)

* 7. Blurry

```
blur_image= cv2.GaussianBlur(img, (11,11),0)
```

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%206%20Exercise%20-%20Signal%20Processing%20in%20Numpy%20and%20Tensorflow/image/blurry.png)

Image augmentation is a strategy that enables practitioners to significantly increase the diversity of images available for training models, without actually collecting new images. For training any Machine Learning model and specifically Deep Learning model, having a large dataset is very important and can improve the performance of the model dramatically. When we train a deep learning model on images, we need at least tens of thousands of images to generalise the pattern of the images.

Generating image data is expensive and tedious work. Machines are blind without data. In such a case, we can generate more images from existing images by applying different transformations techniques on it. There are different techniques like rotation, flipping, shifting, etc. which can help us to diversify the image data. We can generate more than 10X or 100X images if we have at least 4–5 transformations techniques. We can also use methods to blur the image and add random noise to image, to generate more images.📝

