# # import base64
# # import numpy as np
# # import cv2

# # def decode_image(image_data):
# #     """Decodes a base64 image string into a numpy array."""
# #     decoded_image = base64.b64decode(image_data)
# #     np_image = np.frombuffer(decoded_image, np.uint8)
# #     return cv2.imdecode(np_image, cv2.IMREAD_COLOR)

# # def verify_biometrics_data(new_image_data, stored_image_data):
# #     """Compares two biometric images for similarity."""
# #     new_image = decode_image(new_image_data)
# #     stored_image = decode_image(stored_image_data)

# #     # In a real-world application, use advanced comparison algorithms
# #     return np.array_equal(new_image, stored_image)

# # def store_biometrics_data(username, image_data):
# #     """Stores biometric data for a user."""
# #     from mock_data.users_db import users_db
# #     users_db[username]["biometric_data"] = image_data


# import base64
# import numpy as np
# import cv2

# def decode_image(image_data):
#     """Decodes a base64 image string into a numpy array."""
#     # Add padding to base64 string if necessary
#     padding = len(image_data) % 4
#     if padding != 0:
#         image_data += "=" * (4 - padding)

#     decoded_image = base64.b64decode(image_data)
#     np_image = np.frombuffer(decoded_image, np.uint8)
#     return cv2.imdecode(np_image, cv2.IMREAD_COLOR)

# def verify_biometrics_data(new_image_data, stored_image_data):
#     """Compares two biometric images for similarity."""
#     new_image = decode_image(new_image_data)
#     stored_image = decode_image(stored_image_data)

#     # In a real-world application, use advanced comparison algorithms
#     return np.array_equal(new_image, stored_image)

# def store_biometrics_data(username, image_data):
#     """Stores biometric data for a user."""
#     from mock_data.users_db import users_db
#     users_db[username]["biometric_data"] = image_data
import base64
from io import BytesIO
from PIL import Image

def verify_biometrics_data(stored_data, incoming_data):
    stored_image = base64.b64decode(stored_data)
    incoming_image = base64.b64decode(incoming_data)

    stored_image = Image.open(BytesIO(stored_image))
    incoming_image = Image.open(BytesIO(incoming_image))

    # Perform biometric comparison logic (e.g., image comparison using a library)
    return stored_image == incoming_image  # For demo purposes, compare directly

def store_biometrics_data(username, biometric_data):
    # Save the biometric data into your database for later comparison
    pass
