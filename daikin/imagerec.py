# import the necessary packages
from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import InceptionV3
import numpy as np



print("[INFO] loading and preprocessing image...")
image = image_utils.load_img('/Users/i037762/Desktop/crop_1535446553033.jpg', target_size=(224, 224))
image = image_utils.img_to_array(image)
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

#image=cv2.imread()
model = InceptionV3(include_top=True, weights="imagenet")
preds = model.predict(image)
P = decode_predictions(preds)
for (i, (imagenetID, label, prob)) in enumerate(P[0]):
    print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))