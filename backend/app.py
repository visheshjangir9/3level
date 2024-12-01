# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # from utils.hashing import hash_input
# # from utils.otp import generate_otp
# # from utils.biometrics import verify_biometrics_data, store_biometrics_data
# # from mock_data.users_db import users_db

# # app = Flask(__name__)
# # CORS(app)

# # from flask import send_from_directory

# # @app.route('/')
# # def serve_frontend():
# #     return send_from_directory('../frontend', 'index.html')

# # @app.route('/<path:path>')
# # def serve_static(path):
# #     return send_from_directory('../frontend', path)

# # @app.route('/api/signup', methods=['POST'])
# # def signup():
# #     data = request.json
# #     username = data.get("username")
# #     password = data.get("password")
# #     photo = data.get("photo")

# #     if username in users_db:
# #         return jsonify({"success": False, "message": "Username already exists."}), 400

# #     hashed_password = hash_input(password)
# #     users_db[username] = {
# #         "password": hashed_password,
# #         "otp": None,
# #         "biometric_data": photo,  # Store the base64 photo data
# #     }

# #     return jsonify({"success": True, "message": "User registered successfully."})

# # @app.route('/api/login', methods=['POST'])
# # def login():
# #     data = request.json
# #     username = data.get("username")
# #     password = data.get("password")

# #     if username not in users_db or hash_input(password) != users_db[username]["password"]:
# #         return jsonify({"success": False, "message": "Invalid username or password."}), 401

# #     otp = generate_otp()
# #     users_db[username]["otp"] = otp

# #     return jsonify({"success": True, "message": "Password verified.", "otp": otp})

# # @app.route('/api/verify-otp', methods=['POST'])
# # def verify_otp():
# #     data = request.json
# #     username = data.get("username")
# #     otp = data.get("otp")

# #     if username in users_db and users_db[username]["otp"] == int(otp):
# #         return jsonify({"success": True, "message": "OTP verified."})
# #     return jsonify({"success": False, "message": "Invalid OTP."}), 401

# # @app.route('/api/verify-biometrics', methods=['POST'])
# # def verify_biometrics():
# #     data = request.json
# #     username = data.get("username")
# #     image_data = data.get("biometric_data")

# #     if username not in users_db:
# #         return jsonify({"success": False, "message": "User not found."}), 404

# #     stored_biometric_data = users_db[username]["biometric_data"]

# #     if stored_biometric_data is None:
# #         store_biometrics_data(username, image_data)
# #         return jsonify({"success": True, "message": "Biometric data registered successfully."})

# #     if verify_biometrics_data(image_data, stored_biometric_data):
# #         return jsonify({"success": True, "message": "Biometric verification successful."})
# #     return jsonify({"success": False, "message": "Biometric verification failed."}), 401

# # if __name__ == '__main__':
# #     app.run(debug=True)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from utils.hashing import hash_input
# from utils.otp import generate_otp
# from utils.biometrics import verify_biometrics_data, store_biometrics_data
# from mock_data.users_db import users_db

# app = Flask(__name__)
# CORS(app)

# from flask import send_from_directory

# @app.route('/')
# def serve_frontend():
#     return send_from_directory('../frontend', 'index.html')

# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory('../frontend', path)

# @app.route('/api/signup', methods=['POST'])
# def signup():
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")
#     biometric_data = data.get("biometric_data")

#     if username in users_db:
#         return jsonify({"success": False, "message": "Username already exists."}), 400

#     hashed_password = hash_input(password)
#     users_db[username] = {
#         "password": hashed_password,
#         "otp": None,
#         "biometric_data": biometric_data,  # Store biometric data directly at signup
#     }

#     return jsonify({"success": True, "message": "User registered successfully."})

# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")

#     if username not in users_db or hash_input(password) != users_db[username]["password"]:
#         return jsonify({"success": False, "message": "Invalid username or password."}), 401

#     otp = generate_otp()
#     users_db[username]["otp"] = otp

#     return jsonify({"success": True, "message": "Password verified.", "otp": otp})

# @app.route('/api/verify-otp', methods=['POST'])
# def verify_otp():
#     data = request.json
#     username = data.get("username")
#     otp = data.get("otp")

#     if username in users_db and users_db[username]["otp"] == int(otp):
#         return jsonify({"success": True, "message": "OTP verified."})
#     return jsonify({"success": False, "message": "Invalid OTP."}), 401

# @app.route('/api/verify-biometrics', methods=['POST'])
# def verify_biometrics():
#     data = request.json
#     username = data.get("username")
#     image_data = data.get("biometric_data")

#     if username not in users_db:
#         return jsonify({"success": False, "message": "User not found."}), 404

#     stored_biometric_data = users_db[username]["biometric_data"]

#     if stored_biometric_data is None:
#         store_biometrics_data(username, image_data)
#         return jsonify({"success": True, "message": "Biometric data registered successfully."})

#     if verify_biometrics_data(image_data, stored_biometric_data):
#         return jsonify({"success": True, "message": "Biometric verification successful."})
#     return jsonify({"success": False, "message": "Biometric verification failed."}), 401

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.hashing import hash_input
from utils.otp import generate_otp
from utils.biometrics import verify_biometrics_data, store_biometrics_data
from mock_data.users_db import users_db

app = Flask(__name__)
CORS(app)

from flask import send_from_directory

@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    biometric_data = data.get("biometric_data")

    if username in users_db:
        return jsonify({"success": False, "message": "Username already exists."}), 400

    hashed_password = hash_input(password)
    users_db[username] = {
        "password": hashed_password,
        "otp": None,
        "biometric_data": biometric_data,  # Store biometric data directly at signup
    }

    return jsonify({"success": True, "message": "User registered successfully."})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username not in users_db or hash_input(password) != users_db[username]["password"]:
        return jsonify({"success": False, "message": "Invalid username or password."}), 401

    otp = generate_otp()
    users_db[username]["otp"] = otp

    return jsonify({"success": True, "message": "OTP sent successfully.", "otp": otp})

@app.route('/api/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    username = data.get("username")
    otp = data.get("otp")

    if username not in users_db or users_db[username]["otp"] != otp:
        return jsonify({"success": False, "message": "Invalid OTP."}), 400

    return jsonify({"success": True, "message": "OTP verified successfully."})

@app.route('/api/verify-biometrics', methods=['POST'])
def verify_biometrics():
    data = request.json
    username = data.get("username")
    biometric_data = data.get("biometric_data")

    if username not in users_db:
        return jsonify({"success": False, "message": "User not found."}), 404

    stored_biometric_data = users_db[username]["biometric_data"]

    # Verify biometric data
    if verify_biometrics_data(stored_biometric_data, biometric_data):
        return jsonify({"success": True, "message": "Biometric verification successful."})
    else:
        return jsonify({"success": False, "message": "Biometric verification failed."}), 400

if __name__ == '__main__':
    app.run(debug=True)
