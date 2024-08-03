import cv2
import numpy as np
import os

def calculate_WB(image_path):
    img = cv2.imread(image_path)
    img_float32 = img.astype('float32')

    avgB = np.mean(img_float32[:,:,0])
    avgG = np.mean(img_float32[:,:,1])
    avgR = np.mean(img_float32[:,:,2])

    scale = 255 / (avgR + avgG + avgB)
    kB = scale * avgB
    kG = scale * avgG
    kR = scale * avgR

    return (kB, kG, kR)

calculate_WB(f"C:/Users/Simon.Luttmann/Documents/binning.jpg")

def debayer_image(path):
    pass

def main(path):
    print(os.path.join(path,'white_paper.tiff'))
    rgb_wb_image = debayer_white_balance_image(raw_wb_image)
    whiteBalance = calculate_WB(rgb_wb_image)

   
    
    for entry in os.listdir(path):
        file_path = os.path.join(path, entry)
        print(file_path)
        rgb_image = debayer_image(file_path)
        rgb_image_wb = apply_wb(rgb_image, whiteBalance)
        store_image(rgb_image_wb)
        for factor in DOWNSAMPLING_FACTORS:
            resized_img = downsize(rgb_image_wb, factor)
            store_image(resized_img)
        downsize(rgb_image_wb, DOWNSAMPLING_FACTORS)


DOWNSAMPLING_FACTORS = [8, 5, 4, 2]

if __name__ == '__main__':
    folder_path = 'C:/Users/Simon.Luttmann/Documents'
    
    #main(folder_path)