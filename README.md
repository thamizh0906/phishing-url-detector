#Phishing URL Detector

A Python-based tool to detect phishing URLs using two approches:
  1.**Rule-based detection** - checks URL features like length, special charactes, use of IP address, etc.
  2.**Machine Learning model** - trained using RandomForest on the PhiUSIIL Phishing URL dataset, achieving ~99% accuracy.

  ## Files
  - 'detector.py' - Rule-based phishing URL detector
  - 'ml_detector.py' - Machine Learning based detector (RandomForest)

  ## Dataset
  [PhiUSIIL Phishing URL Dataset](https://www.kaggle.com/datasets/ndarvind/phiusiil-phishing-url-dataset) (from Kaggle) - used for trainingthe ML model.

  ## How to Run
  '''bash
  python detector.py
  python ml_detector.py

    
