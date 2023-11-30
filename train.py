import glob2
import os
import pandas as pd
import cv2
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load annotations from CSV
annotations_csv = '_annotations.csv'
df = pd.read_csv(annotations_csv)

# Initialize empty lists to store images and labels
images = []
labels = []

image_dir = 'unlabeled_images'
for index, row in df.iterrows():
    image_path = os.path.join(image_dir, row['filename'])
    
    # Check if the image file exists
    if os.path.exists(image_path):
        img = cv2.imread(image_path)
        
        # Resize the image (if needed)
        img = cv2.resize(img, (256, 256))
        
        # Flatten image data
        flattened_img = img.flatten()

        # Append flattened image to the list
        images.append(flattened_img)
        
        # Append corresponding label to the list
        labels.append(row['class'])
    else:
        print(f"Warning: Image file not found at {image_path}")


# for x in os.listdir():
#     if x.endswith(".jpg"):
#         img = cv2.imread(x)
#         img = cv2.resize(img, (256, 256))
#         flattened_img = img.flatten()
#         images.append(flattened_img)
#         labels.append(row['class'])
# print(images)    


# Encode class labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, y, test_size=0.2, random_state=42)

# Train a simple model (Random Forest as an example)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')

# Save the trained model as a pickle file
with open('trained_model.pkl', 'wb') as model_file:
    pickle.dump((model, label_encoder), model_file)
