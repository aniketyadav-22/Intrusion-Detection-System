Intrusion Detection System (IDS) — Streamlit + Machine Learning





A lightweight, production-ready Intrusion Detection System built with Streamlit for interactive analysis and scikit-learn / PyTorch for ML. It supports training and inference on tabular IDS datasets (KDD Cup ’99, NSL-KDD, and optionally CIC-IDS-2017), real-time CSV uploads, and clear visualizations for security monitoring.

<img alt="demo" src="🔧/assets/demo.gif" width="800"/>
✨ Features
One-click web app with Streamlit for training, evaluation, and live predictions

Multi-model support: Logistic Regression, Random Forest, XGBoost, LightGBM, and (optional) simple DNN (PyTorch)

Preprocessing pipeline (imputation, scaling, encoding) with sklearn Pipeline

Imbalanced data handling (class weights / SMOTE)

Explainability via feature importance + SHAP (optional)

Metrics dashboard: accuracy, precision/recall/F1 (macro & per-class), ROC-AUC, confusion matrix

Batch prediction: upload CSV with raw features, get labeled outputs

Reproducible training scripts + saved artifacts (.pkl / .pt)

Dockerfile for portable deployment

