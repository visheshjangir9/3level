// // // const backendUrl = "http://127.0.0.1:5000";

// // async function login() {
// //     const username = document.getElementById("username").value;
// //     const password = document.getElementById("password").value;

// //     if (!username || !password) {
// //         alert("Please enter your username and password.");
// //         return;
// //     }

// //     const response = await fetch(`${backendUrl}/api/login`, {
// //         method: "POST",
// //         headers: { "Content-Type": "application/json" },
// //         body: JSON.stringify({ username, password }),
// //     });

// //     const data = await response.json();

// //     if (data.success) {
// //         alert(data.message);
// //         document.getElementById("step1").style.display = "none";
// //         document.getElementById("step2").style.display = "block";
// //         document.getElementById("otp-display").innerText = `Your OTP is: ${data.otp}`;
// //     } else {
// //         alert(data.message);
// //     }
// // }

// // async function verifyOtp() {
// //     const username = document.getElementById("username").value;
// //     const otp = document.getElementById("otp").value;

// //     const response = await fetch(`${backendUrl}/api/verify-otp`, {
// //         method: "POST",
// //         headers: { "Content-Type": "application/json" },
// //         body: JSON.stringify({ username, otp }),
// //     });

// //     const data = await response.json();

// //     if (data.success) {
// //         alert(data.message);
// //         document.getElementById("step2").style.display = "none";
// //         document.getElementById("step3").style.display = "block";
// //     } else {
// //         alert(data.message);
// //     }
// // }

// // async function biometricVerify() {
// //     const username = document.getElementById("username").value;
// //     const biometricData = "base64encodedBiometricData";  // Example; Replace with actual biometric data

// //     const response = await fetch(`${backendUrl}/api/biometric-verify`, {
// //         method: "POST",
// //         headers: { "Content-Type": "application/json" },
// //         body: JSON.stringify({ username, biometric_data: biometricData }),
// //     });

// //     const data = await response.json();

// //     if (data.success) {
// //         alert(data.message);
// //     } else {
// //         alert(data.message);
// //     }
// // }
// const backendUrl = "http://127.0.0.1:5000"; // Make sure this points to your backend

// async function login() {
//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;

//     if (!username || !password) {
//         alert("Please enter your username and password.");
//         return;
//     }

//     const response = await fetch(`${backendUrl}/api/login`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ username, password }),
//     });

//     const data = await response.json();

//     if (data.success) {
//         alert(data.message);
//         document.getElementById("step1").style.display = "none";  // Hide login step
//         document.getElementById("step2").style.display = "block"; // Show OTP step
//         document.getElementById("otp-display").innerText = `Your OTP is: ${data.otp}`;
//     } else {
//         alert(data.message);
//     }
// }

//  async function signUp() {
//     const username = document.getElementById("signup-username").value;
//     const password = document.getElementById("signup-password").value;

//     if (!username || !password) {
//         alert("Please fill out all fields.");
//         return;
//     }

//     const imageData = captureImage(); // Capture the image

//     if (!imageData) {
//         alert("Please capture a photo.");
//         return;
//     }

//     const response = await fetch(`${backendUrl}/api/signup`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ username, password, biometric_data: imageData }),
//     });

//     const data = await response.json();

//     if (data.success) {
//         alert(data.message);
//         document.getElementById("signup").style.display = "none";  // Hide signup section
//         document.getElementById("step1").style.display = "block";  // Show login section
//     } else {
//         alert(data.message);
//     }
//  }

// function captureImage() {
//     const canvas = document.getElementById("signup-canvas");
//     const video = document.getElementById("signup-video");
//     const context = canvas.getContext("2d");
//     canvas.width = video.videoWidth;
//     canvas.height = video.videoHeight;
//     context.drawImage(video, 0, 0, canvas.width, canvas.height);
//     return canvas.toDataURL("image/jpeg").split(',')[1]; // Return base64 image string
// }

// async function startCamera() {
//     const video = document.getElementById("signup-video");
//     const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//     video.srcObject = stream;
// }

// window.onload = startCamera;


// async function verifyOtp() {
//     const username = document.getElementById("username").value;
//     const otp = document.getElementById("otp").value;

//     const response = await fetch(`${backendUrl}/api/verify-otp`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ username, otp }),
//     });

//     const data = await response.json();

//     if (data.success) {
//         alert(data.message);
//         document.getElementById("step2").style.display = "none";  // Hide OTP step
//         document.getElementById("step3").style.display = "block"; // Show biometric step
//     } else {
//         alert(data.message);
//     }
// }

// async function biometricVerify() {
//     const username = document.getElementById("username").value;
//     const biometricData = "base64encodedBiometricData";  // Example; Replace with actual biometric data

//     const response = await fetch(`${backendUrl}/api/verify-biometrics`, {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ username, biometric_data: biometricData }),
//     });

//     const data = await response.json();

//     if (data.success) {
//         alert(data.message);
//     } else {
//         alert(data.message);
//     }
// };

// function convertToBase64(file, callback) {
//     const reader = new FileReader();
//     reader.onloadend = function () {
//         callback(reader.result.split(',')[1]); // Strip the "data:image/jpeg;base64," part
//     };
//     reader.readAsDataURL(file);
// }
const backendUrl = "http://127.0.0.1:5000"; // Make sure this points to your backend

async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) {
        alert("Please enter your username and password.");
        return;
    }

    const response = await fetch(`${backendUrl}/api/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (data.success) {
        alert(data.message);
        document.getElementById("step1").style.display = "none";  // Hide login step
        document.getElementById("step2").style.display = "block"; // Show OTP step
        document.getElementById("otp-display").innerText = `Your OTP is: ${data.otp}`;
    } else {
        alert(data.message);
    }
}

async function signUp() {
    const username = document.getElementById("signup-username").value;
    const password = document.getElementById("signup-password").value;

    if (!username || !password) {
        alert("Please fill out all fields.");
        return;
    }

    const imageData = captureImage(); // Capture the image

    if (!imageData) {
        alert("Please capture a photo.");
        return;
    }

    const response = await fetch(`${backendUrl}/api/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password, biometric_data: imageData }),
    });

    const data = await response.json();

    if (data.success) {
        alert(data.message);
        document.getElementById("signup").style.display = "none";  // Hide signup section
        document.getElementById("step1").style.display = "block";  // Show login section
    } else {
        alert(data.message);
    }
}

async function verifyOtp() {
    const username = document.getElementById("username").value;
    const otp = document.getElementById("otp").value;

    const response = await fetch(`${backendUrl}/api/verify-otp`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, otp }),
    });

    const data = await response.json();

    if (data.success) {
        alert(data.message);
        document.getElementById("step2").style.display = "none";  // Hide OTP step
        document.getElementById("step3").style.display = "block"; // Show biometric step
    } else {
        alert(data.message);
    }
}

async function biometricVerify() {
    const username = document.getElementById("username").value;
    const biometricData = captureBiometric(); // Capture biometric data

    if (!biometricData) {
        alert("Please capture a biometric photo.");
        return;
    }

    const response = await fetch(`${backendUrl}/api/verify-biometrics`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, biometric_data: biometricData }),
    });

    const data = await response.json();

    if (data.success) {
        alert(data.message);
    } else {
        alert(data.message);
    }
};

function captureImage() {
    const canvas = document.getElementById("signup-canvas");
    const video = document.getElementById("signup-video");
    const context = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL("image/jpeg").split(',')[1]; // Return base64 image string
}

function captureBiometric() {
    const canvas = document.getElementById("biometric-canvas");
    const video = document.getElementById("biometric-video");
    const context = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL("image/jpeg").split(',')[1]; // Return base64 image string
}

async function startCamera() {
    const video = document.getElementById("signup-video");
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
}

async function startBiometricCamera() {
    const video = document.getElementById("biometric-video");
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
}

window.onload = function() {
    startCamera();  // Start camera for sign-up
    startBiometricCamera();  // Start camera for biometric verification
};
