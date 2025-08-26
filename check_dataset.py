import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("dataset_jurusan.csv")

# Tampilkan distribusi jurusan
print("Distribusi jurusan:")
print(data["Jurusan"].value_counts())
print(f"\nTotal sampel: {len(data)}")

# Encode target (Jurusan)
le = LabelEncoder()
data["Jurusan"] = le.fit_transform(data["Jurusan"])  # ubah jurusan ke angka

# Pisahkan fitur & target
X = data.drop(columns=["Jurusan"])
y = data["Jurusan"]

# Ubah semua fitur string → angka (get_dummies = OneHotEncoding otomatis)
X = pd.get_dummies(X)

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

# Evaluasi
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Hitung AUC (multi-class one-vs-rest)
try:
    auc = roc_auc_score(y_test, y_proba, multi_class="ovr")
    print(f"AUC: {auc:.4f}")
except Exception as e:
    print("AUC tidak bisa dihitung:", e)
