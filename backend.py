from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import logging
import time
import numpy as np

app = Flask(__name__)

# Konfigurasi CORS untuk mendukung semua origin
CORS(app, resources={r"/predict": {"origins": "*"}})  # Izinkan semua origin untuk endpoint /predict

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Validasi file dataset
if not os.path.exists("dataset_jurusan.csv"):
    raise FileNotFoundError("File 'dataset_jurusan.csv' tidak ditemukan. Jalankan generate_dataset.py terlebih dahulu.")

# Load dataset
logging.info("Memuat dataset...")
data = pd.read_csv("dataset_jurusan.csv")

# Periksa kolom dataset
expected_columns = ["Nilai_Matematika", "Nilai_IPA", "Nilai_Bahasa_Inggris", "Minat", "Bakat", "Jurusan"]
if not all(col in data.columns for col in expected_columns):
    raise ValueError(f"Dataset harus memiliki kolom: {expected_columns}")

# Pisahkan fitur dan target
X = data.drop("Jurusan", axis=1)
y = data["Jurusan"]

# Definisikan preprocessing
categorical_features = ["Minat", "Bakat"]
numeric_features = ["Nilai_Matematika", "Nilai_IPA", "Nilai_Bahasa_Inggris"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(sparse_output=False, handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features)
    ])

# Buat pipeline dengan Random Forest
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42, n_jobs=-1))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tuning parameter Random Forest
logging.info("Melakukan tuning parameter...")
start_time = time.time()
param_grid = {
    "classifier__n_estimators": [100, 150],
    "classifier__max_depth": [20, 30],
    "classifier__min_samples_split": [2, 5],
    "classifier__min_samples_leaf": [1, 2]
}
grid_search = GridSearchCV(model, param_grid, cv=3, scoring="accuracy", n_jobs=-1)
grid_search.fit(X_train, y_train)

# Model terbaik
best_model = grid_search.best_estimator_
logging.info(f"Parameter terbaik: {grid_search.best_params_}")
logging.info(f"Waktu tuning: {time.time() - start_time:.2f} detik")

# Simpan model
joblib.dump(best_model, "model_jurusan.pkl")

# Evaluasi akurasi
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
logging.info(f"Akurasi model: {accuracy * 100:.2f}%")

# Tampilkan laporan klasifikasi
logging.info("Laporan klasifikasi:")
logging.info(classification_report(y_test, y_pred))

# Tampilkan fitur penting
feature_names = (best_model.named_steps["preprocessor"]
                 .named_transformers_["cat"]
                 .get_feature_names_out(categorical_features)
                 .tolist() + numeric_features)
importances = best_model.named_steps["classifier"].feature_importances_
feature_importance = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
logging.info("Fitur penting:")
for name, importance in feature_importance:
    logging.info(f"{name}: {importance:.4f}")

# Endpoint untuk prediksi
@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json
        logging.info(f"Input diterima: {input_data}")

        # Validasi input
        required_fields = ["nilai_mat", "nilai_ipa", "nilai_ing", "minat", "bakat"]
        for field in required_fields:
            if field not in input_data:
                logging.error(f"Field '{field}' tidak ditemukan")
                return jsonify({"error": f"Field '{field}' diperlukan"}), 400

        # Konversi dan validasi input
        try:
            nilai_mat = float(input_data["nilai_mat"])
            nilai_ipa = float(input_data["nilai_ipa"])
            nilai_ing = float(input_data["nilai_ing"])
        except ValueError:
            logging.error("Nilai harus berupa angka")
            return jsonify({"error": "Nilai harus berupa angka"}), 400

        # Validasi rentang nilai
        if not (0 <= nilai_mat <= 100 and 0 <= nilai_ipa <= 100 and 0 <= nilai_ing <= 100):
            logging.error("Nilai di luar rentang 0-100")
            return jsonify({"error": "Nilai harus antara 0 dan 100"}), 400

        # Validasi kategori
        valid_minat = data["Minat"].unique()
        valid_bakat = data["Bakat"].unique()
        if input_data["minat"] not in valid_minat:
            logging.error(f"Minat tidak valid: {input_data['minat']}")
            return jsonify({"error": f"Minat tidak valid. Pilih dari: {list(valid_minat)}"}), 400
        if input_data["bakat"] not in valid_bakat:
            logging.error(f"Bakat tidak valid: {input_data['bakat']}")
            return jsonify({"error": f"Bakat tidak valid. Pilih dari: {list(valid_bakat)}"}), 400

        # Siapkan data untuk prediksi
        input_df = pd.DataFrame([{
            "Nilai_Matematika": nilai_mat,
            "Nilai_IPA": nilai_ipa,
            "Nilai_Bahasa_Inggris": nilai_ing,
            "Minat": input_data["minat"],
            "Bakat": input_data["bakat"]
        }])

        # Prediksi
        pred = best_model.predict(input_df)
        jurusan = pred[0]

        # Dapatkan probabilitas
        probas = best_model.predict_proba(input_df)[0]
        max_proba = np.max(probas)

        logging.info(f"Prediksi: {jurusan}, Akurasi: {accuracy * 100:.2f}%, Probabilitas: {max_proba * 100:.2f}")

        return jsonify({
            "jurusan": jurusan,
            "akurasi": accuracy * 100,
            "probabilitas": max_proba * 100
        })
    except Exception as e:
        logging.error(f"Error saat prediksi: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)