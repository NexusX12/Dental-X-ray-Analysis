import cv2
import pickle

# Load the trained model and label encoder from the pickle file
with open('trained_model.pkl', 'rb') as model_file:
    model, label_encoder = pickle.load(model_file)

def detect_and_mark(image_path):
    # Print the image path for debugging
    print(f'Image Path: {image_path}')

    # Load the input image
    img = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if img is None:
        print(f"Error: Couldn't load image from {image_path}")
        return

    # Resize the image (if needed)
    img = cv2.resize(img, (256, 256))

    # Flatten image data
    flattened_img = img.flatten()

    # Predict class label using the trained model
    predicted_label = model.predict([flattened_img])[0]

    # Map the predicted label to the corresponding class
    predicted_class = label_encoder.classes_[predicted_label]

    # Draw a rectangle around the detected area
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)  # Adjust coordinates as needed

    # Display the predicted class name
    cv2.putText(img, f'Class: {predicted_class}', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Detected Area', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage: Detect and mark areas in a new image
image_to_detect = 'test.jpg'
detect_and_mark(image_to_detect)
