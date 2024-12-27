import os
import cv2
import pandas as pd
from PIL import Image
from ultralytics import YOLO

#fill this with path to your model
model = YOLO("/home/joey_pwns/ctfs/mini-ctf-alphabit/Alphabit_minictf_2k25/forensics/FreshEngineer/challenge/detect/train2/weights/best.pt")

#fill this with path to the test images directory
test_images_dir = "/home/joey_pwns/ctfs/mini-ctf-alphabit/Alphabit_minictf_2k25/forensics/FreshEngineer/challenge/test"
#fill this with the output path of your result csv
csv_output_path = "/home/joey_pwns/ctfs/mini-ctf-alphabit/Alphabit_minictf_2k25/forensics/FreshEngineer/challenge/results.csv"


results = []


for image_file in os.listdir(test_images_dir):
    if image_file.endswith(".png"):  
        image_path = os.path.join(test_images_dir, image_file)
        
        
        img = cv2.imread(image_path)

        
        prediction = model.predict(img)[0]
        
        
        for pred in prediction.boxes.xywh:  
            
            x_center, y_center, width, height = pred.tolist()
            
            
            image_id_flag = os.path.splitext(image_file)[0] + "_flag"  
            
            
            results.append([image_id_flag, x_center, y_center, width, height])


df = pd.DataFrame(results, columns=["ImageID_flag", "x_center", "y_center", "width", "height"])


df.to_csv(csv_output_path, index=False)

