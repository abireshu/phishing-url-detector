
Phishing URL Detection Using Machine Learning

A simple but powerful tool that detects whether a URL is **legitimate** or **phishing** using machine learning and URL feature extraction.

>  Built as part of a Internship project.

 Overview:

Phishing attacks are one of the most common threats on the internet. In this project, I built a machine learning-based system that detects potentially harmful URLs based on extracted features. The tool includes:

- Feature extraction from URLs (like URL length, use of HTTPS, subdomains, etc.)
- Model training using **Random Forest classifier**
- Real-time URL prediction using a **Tkinter GUI**

 Objectives:

- Train a model to classify URLs as *phishing* or *legitimate*
- Extract intelligent features that are common in phishing URLs
- Allow users to test any URL via a simple GUI
- Improve accuracy and understanding of ML in real-world problems

 Technologies Used:

| Technology | Purpose                         |
|------------|----------------------------------|
| Python     | Programming language             |
| pandas     | Data manipulation                |
| scikit-learn | Model training & evaluation    |
| joblib     | Model saving/loading             |
| Tkinter    | GUI interface                    |

Features Used for Model Training:

The following features were extracted and used for training the model:

- URLLength – Total number of characters in the URL
- NoOfSubDomain – Count of subdomains used
- IsDomainIP – Checks if domain is an IP address
- IsHTTPS – Whether the URL uses HTTPS
- NoOfOtherSpecialCharsInURL – Special characters count
- NoOfQMarkInURL – Number of "?" in the URL
- ObfuscationRatio – Ratio of suspicious characters in the URL

 GUI Tool

- Built using **Tkinter**
- User enters a URL
- Model instantly classifies it as **Phishing** (🔴) or **Legitimate** (🟢)
- Designed with a modern and clean interface

 How to Run?

1. Clone the Repository
   bash
   git clone https://github.com/abireshu/phishing-url-detector.git
   cd phishing-url-detector


2. Install Requirements
   pip install -r requirements.txt
   
3.feature exttraction
   download feature extraction.py

4. Run the Model Training
    model.py

5. Start the GUI
    phishing url detector.py

 Results

* **Model Accuracy**: \~97.9%
* Trained on thousands of labeled phishing and legitimate URLs
* Evaluated using precision, recall, and f1-score

--------------------
I have used new prediction.py for testing my model with  new phishing and legitimate url's else it is not needed.
the model score here is used to show the accuracy of the model for better understanding.


