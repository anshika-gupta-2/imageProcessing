import streamlit as st 
import pandas as pd 
import cv2 
import numpy as np  
import os 
from PIL import Image ,ImageDraw 
st.title("Process your Image here") 
 
st.header("upload an image") 
 
# user to upload an image  
uploaded_file = st.file_uploader(".....",type = ["jpg","png","jpeg"]) 
print(uploaded_file) 
 
 
if uploaded_file is not None: 
    # Converting the file into opencv image 
    file = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8) 
    img = cv2.imdecode(file,1) 
    
 
    # Display the original image 
    st.image(img, channels="BGR", use_column_width = True) 
     
    # error / colourful msg 
    st.success("successful done") 
 
    navigation= st.sidebar.radio("Select",["original","RGB","Grayscale","Threshold","brightness/contrast","shape"]) 
     
    if navigation == "original": 
        st.write("original")  
        
    if navigation == "RGB": 
 
        img_rgb= cv2.cvtColor(img , cv2.COLOR_BGR2RGB) 
        st.image(Image.fromarray(img_rgb), caption="RGB Image", use_column_width=True) 
        st.write("RGB") 
    if navigation == "Grayscale": 
         
            grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            st.image(grayscale_image, caption="After Grayscale Image", use_column_width=True) 
    if navigation == "Threshold": 
    # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        
        # Apply thresholding
        threshold_valuex = st.slider("Threshold Valuex", 0, 255, 128)
        threshold_valuey = st.slider("Threshold Valuey", 0, 255, 128)  # You can adjust the default range and value
        _, thresholded_image = cv2.threshold(grayscale_image, threshold_valuex,threshold_valuey , cv2.THRESH_BINARY)
        
        # Display the thresholded image
        st.image(thresholded_image, caption=f"After Thresholding ", use_column_width=True) 
        st.write("Threshold")

 
    if navigation == "brightness/contrast": 
        brightness = st.slider("Brightness", 10.0, 20.0, 15.0) 
        contrast = st.slider("Contrast", 0.0, 2.0, 1.0) 
        adjusted_image = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness) 
        st.image(adjusted_image, caption="After Adjustment", use_column_width=True) 
        st.write("br") 
 
    if navigation == "shape": 
        draw = ImageDraw.Draw(Image.fromarray(img)) 
        pil_image = Image.fromarray(img) 
        st.write("sh") 
     
        gr = st.selectbox("options",["Rectangle","triangle","circle","line"]) 
        #if gr  == "Rectangle": 
            #top_left = tuple(st.text_input("Top Left (x, y)", value="0, 0").split(',')) 
            #bottom_right = tuple(st.text_input("Bottom Right (x, y)", value="50, 50").split(',')) 
        # scaling the line (max value, default value ) 
            #scale = st.slider("line scale",1,10,1) 
            #draw.rectangle([int(top_left[0]), int(top_left[1]), int(bottom_right[0]), int(bottom_right[1])], outline="blue", width=scale) 
        if gr == "Rectangle":
            top_left = tuple(map(int, st.text_input("Top Left (x, y)", value="0, 0").split(',')))
            bottom_right = tuple(map(int, st.text_input("Bottom Right (x, y)", value="50, 50").split(',')))
            scale = st.slider("Line scale", 1, 10, 1)

            # Draw the rectangle
            cv2.rectangle(img, top_left, bottom_right, color=(0, 255, 0), thickness=scale)
            
            # Display the image with the drawn rectangle
            st.image(img, caption="Image with Drawn Rectangle", use_column_width=True)


        if gr == "circle":
            center = tuple(map(int, st.text_input("Center (x, y)", value="50, 50").split(',')))
            radius = st.slider("Radius", 1, 50, 10)
            color = (0, 0, 255)  # Color is set to red in BGR format

            # Draw the circle
            cv2.circle(img, center, radius, color, thickness=2)
            
            # Display the image with the drawn circle
            st.image(img, caption="Image with Drawn Circle", use_column_width=True)

        if gr == "line": 
            start_point = tuple(map(int, st.text_input("Start Point (x, y)", value="0, 0").split(',')))
            end_point = tuple(map(int, st.text_input("End Point (x, y)", value="50, 50").split(',')))
            scale = st.slider("Line scale", 1, 10, 1)

            # Draw the line
            cv2.line(img, start_point, end_point, color=(255, 0, 0), thickness=scale)
            
            # Display the image with the drawn line
            st.image(img, caption="Image with Drawn Line", use_column_width=True)
        if gr == "triangle":
            # Input three vertices as (x, y) tuples
            vertex1 = tuple(map(int, st.text_input("Vertex 1 (x, y)", value="50, 10").split(',')))
            vertex2 = tuple(map(int, st.text_input("Vertex 2 (x, y)", value="10, 50").split(',')))
            vertex3 = tuple(map(int, st.text_input("Vertex 3 (x, y)", value="90, 50").split(',')))
            
            # Combine the vertices into a list
            vertices = [vertex1, vertex2, vertex3]

            color = (255, 0, 255)  # Color is set to purple in BGR format

            # Draw the filled triangle
            cv2.polylines(img, [np.array(vertices)], isClosed=True, color=color, thickness=2, lineType=cv2.LINE_AA)
            
            # Display the image with the drawn triangle
            st.image(img, caption="Image with Drawn Triangle", use_column_width=True)

