import cv2 
import numpy as np

def convolve2D(image, kernel, padding=0, strides=1):

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]
    print("Kernel:",xKernShape, "x", yKernShape, "\nImage:", xImgShape, "x", yImgShape)

    # Shape of Output Convolution
    # START TODO ###################
    xOutput = int((xImgShape + 2*padding - xKernShape + 1 ) / strides)
    yOutput = int((yImgShape + 2*padding - yKernShape + 1 ) / strides)
    # END TODO ###################
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        # START TODO ###################
        imagePadded = np.pad(image, padding)  # standard is 0-padding
        # END TODO ###################
    else:
        imagePadded = image

    # Iterate through image
    for y in range(1, image.shape[1]+1):
        # Exit Convolution
        # START TODO ###################
        # raise NotImplementedError
        # END TODO ###################
        
        # Only Convolve if y has gone down by the specified Strides
        # START TODO ###################
        if (y + np.floor(yKernShape/2) ) % strides == 0:
            for x in range(1, image.shape[0]+1):
                if (x + np.floor(xKernShape / 2)) % strides == 0:
                    xout  = int((x + np.floor(xKernShape/2)) / strides)-1
                    yout  = int((y + np.floor(yKernShape/2)) / strides)-1
                    yimstart = int(y - np.floor(yKernShape / 2))
                    yimend = int(y + np.floor(yKernShape / 2))+1
                    ximend = int(x + np.floor(xKernShape / 2))+1
                    ximstart = int(x - np.floor(xKernShape / 2))
                    teilimage = imagePadded[ximstart : ximend, yimstart : yimend] * kernel
                    output[xout][yout] = np.sum(teilimage)
        # END TODO ###################

    return output


if __name__ == '__main__':
    # Grayscale Image
    image = cv2.imread('image.png',0)

    # Edge Detection Kernel
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Convolve and Save Output
    output = convolve2D(image, kernel, padding=2)
    cv2.imwrite('2DConvolved.png', output)
