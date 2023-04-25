// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-app.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
apiKey: "AIzaSyBGdMQ5SRLPdOQ1noaABXMrSiZiZgAuBUE",
authDomain: "nsi-ocr.firebaseapp.com",
projectId: "nsi-ocr",
storageBucket: "nsi-ocr.appspot.com",
messagingSenderId: "453878755971",
appId: "1:453878755971:web:884e65de91ab5a644821b6",
measurementId: "G-T7R01X0YBM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);