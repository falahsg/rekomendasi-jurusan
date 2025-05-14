import pandas as pd
import numpy as np
import random

# Daftar jurusan berdasarkan kategori
jurusan_teknologi = [
    "Teknik Informatika", "Sistem Informasi", "Teknik Elektro", "Teknik Mesin",
    "Teknik Sipil", "Arsitektur", "Teknik Lingkungan", "Teknik Nuklir"
]
jurusan_kesehatan = [
    "Kedokteran", "Ilmu Gizi", "Farmasi", "Kesehatan Masyarakat"
]
jurusan_sosial = [
    "Psikologi", "Ilmu Komunikasi", "Hukum", "Ilmu Politik", "Pendidikan Guru Sekolah Dasar"
]
jurusan_seni = ["Desain Komunikasi Visual", "Seni Rupa", "Desain Interior"]
jurusan_bisnis = ["Akuntansi", "Manajemen", "Ekonomi Pembangunan"]

# Semua jurusan
all_jurusan = jurusan_teknologi + jurusan_kesehatan + jurusan_sosial + jurusan_seni + jurusan_bisnis

# Fungsi untuk menghasilkan data dengan aturan ketat
def generate_data(n_samples):
    data = []
    samples_per_jurusan = n_samples // len(all_jurusan)

    for jurusan in all_jurusan:
        for _ in range(samples_per_jurusan):
            if jurusan == "Teknik Informatika":
                nilai_mat = random.randint(90, 100)
                nilai_ipa = random.randint(88, 95)
                nilai_ing = random.randint(85, 95)
                minat = "Teknologi"
                bakat = random.choice(["Analitis"] * 7 + ["Komunikatif"] * 3)
            elif jurusan == "Sistem Informasi":
                nilai_mat = random.randint(85, 89)
                nilai_ipa = random.randint(80, 85)
                nilai_ing = random.randint(90, 97)
                minat = "Teknologi"
                bakat = random.choice(["Analitis"] * 4 + ["Komunikatif"] * 6)
            elif jurusan == "Teknik Elektro":
                nilai_mat = random.randint(90, 95)
                nilai_ipa = random.randint(93, 100)
                nilai_ing = random.randint(70, 80)
                minat = "Teknologi"
                bakat = "Praktis"
            elif jurusan == "Teknik Mesin":
                nilai_mat = random.randint(90, 95)
                nilai_ipa = random.randint(93, 100)
                nilai_ing = random.randint(65, 75)
                minat = "Teknologi"
                bakat = "Praktis"
            elif jurusan == "Teknik Sipil":
                nilai_mat = random.randint(85, 90)
                nilai_ipa = random.randint(88, 93)
                nilai_ing = random.randint(65, 75)
                minat = "Teknologi"
                bakat = "Praktis"
            elif jurusan == "Arsitektur":
                nilai_mat = random.randint(80, 85)
                nilai_ipa = random.randint(80, 85)
                nilai_ing = random.randint(85, 95)
                minat = "Teknologi"
                bakat = "Kreatif"
            elif jurusan == "Teknik Lingkungan":
                nilai_mat = random.randint(80, 85)
                nilai_ipa = random.randint(88, 93)
                nilai_ing = random.randint(80, 90)
                minat = "Teknologi"
                bakat = "Analitis"
            elif jurusan == "Teknik Nuklir":
                nilai_mat = random.randint(95, 100)
                nilai_ipa = random.randint(95, 100)
                nilai_ing = random.randint(80, 90)
                minat = "Teknologi"
                bakat = random.choice(["Analitis"] * 9 + ["Komunikatif"] * 1)
            elif jurusan == "Kedokteran":
                nilai_mat = random.randint(95, 100)
                nilai_ipa = random.randint(97, 100)
                nilai_ing = random.randint(85, 95)
                minat = "Kesehatan"
                bakat = "Analitis"
            elif jurusan == "Ilmu Gizi":
                nilai_mat = random.randint(80, 85)
                nilai_ipa = random.randint(93, 100)
                nilai_ing = random.randint(85, 95)
                minat = "Kesehatan"
                bakat = "Analitis"
            elif jurusan == "Farmasi":
                nilai_mat = random.randint(90, 95)
                nilai_ipa = random.randint(93, 100)
                nilai_ing = random.randint(85, 95)
                minat = "Kesehatan"
                bakat = "Analitis"
            elif jurusan == "Kesehatan Masyarakat":
                nilai_mat = random.randint(75, 80)
                nilai_ipa = random.randint(88, 93)
                nilai_ing = random.randint(88, 97)
                minat = "Kesehatan"
                bakat = "Komunikatif"
            elif jurusan == "Psikologi":
                nilai_mat = random.randint(65, 75)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(95, 100)
                minat = "Sosial"
                bakat = "Komunikatif"
            elif jurusan == "Ilmu Komunikasi":
                nilai_mat = random.randint(60, 70)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(95, 100)
                minat = "Sosial"
                bakat = "Komunikatif"
            elif jurusan == "Hukum":
                nilai_mat = random.randint(75, 85)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(95, 100)
                minat = "Sosial"
                bakat = "Analitis"
            elif jurusan == "Ilmu Politik":
                nilai_mat = random.randint(65, 75)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(95, 100)
                minat = "Sosial"
                bakat = "Komunikatif"
            elif jurusan == "Pendidikan Guru Sekolah Dasar":
                nilai_mat = random.randint(75, 85)
                nilai_ipa = random.randint(65, 75)
                nilai_ing = random.randint(90, 97)
                minat = "Sosial"
                bakat = "Komunikatif"
            elif jurusan == "Desain Komunikasi Visual":
                nilai_mat = random.randint(60, 70)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(90, 97)
                minat = "Seni"
                bakat = "Kreatif"
            elif jurusan == "Seni Rupa":
                nilai_mat = random.randint(60, 70)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(85, 92)
                minat = "Seni"
                bakat = "Kreatif"
            elif jurusan == "Desain Interior":
                nilai_mat = random.randint(65, 75)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(85, 95)
                minat = "Seni"
                bakat = "Kreatif"
            elif jurusan == "Akuntansi":
                nilai_mat = random.randint(95, 100)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(85, 95)
                minat = "Bisnis"
                bakat = "Analitis"
            elif jurusan == "Manajemen":
                nilai_mat = random.randint(85, 90)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(90, 97)
                minat = "Bisnis"
                bakat = "Komunikatif"
            elif jurusan == "Ekonomi Pembangunan":
                nilai_mat = random.randint(90, 95)
                nilai_ipa = random.randint(60, 70)
                nilai_ing = random.randint(90, 97)
                minat = "Bisnis"
                bakat = "Analitis"

            data.append([nilai_mat, nilai_ipa, nilai_ing, minat, bakat, jurusan])

    # Tambahkan sisa sampel dengan aturan ketat
    remaining_samples = n_samples - len(data)
    for _ in range(remaining_samples):
        jurusan = random.choice(all_jurusan)
        if jurusan == "Teknik Informatika":
            nilai_mat = random.randint(90, 100)
            nilai_ipa = random.randint(88, 95)
            nilai_ing = random.randint(85, 95)
            minat = "Teknologi"
            bakat = random.choice(["Analitis"] * 7 + ["Komunikatif"] * 3)
        elif jurusan == "Sistem Informasi":
            nilai_mat = random.randint(85, 89)
            nilai_ipa = random.randint(80, 85)
            nilai_ing = random.randint(90, 97)
            minat = "Teknologi"
            bakat = random.choice(["Analitis"] * 4 + ["Komunikatif"] * 6)
        elif jurusan == "Teknik Elektro":
            nilai_mat = random.randint(90, 95)
            nilai_ipa = random.randint(93, 100)
            nilai_ing = random.randint(70, 80)
            minat = "Teknologi"
            bakat = "Praktis"
        elif jurusan == "Teknik Mesin":
            nilai_mat = random.randint(90, 95)
            nilai_ipa = random.randint(93, 100)
            nilai_ing = random.randint(65, 75)
            minat = "Teknologi"
            bakat = "Praktis"
        elif jurusan == "Teknik Sipil":
            nilai_mat = random.randint(85, 90)
            nilai_ipa = random.randint(88, 93)
            nilai_ing = random.randint(65, 75)
            minat = "Teknologi"
            bakat = "Praktis"
        elif jurusan == "Arsitektur":
            nilai_mat = random.randint(80, 85)
            nilai_ipa = random.randint(80, 85)
            nilai_ing = random.randint(85, 95)
            minat = "Teknologi"
            bakat = "Kreatif"
        elif jurusan == "Teknik Lingkungan":
            nilai_mat = random.randint(80, 85)
            nilai_ipa = random.randint(88, 93)
            nilai_ing = random.randint(80, 90)
            minat = "Teknologi"
            bakat = "Analitis"
        elif jurusan == "Teknik Nuklir":
            nilai_mat = random.randint(95, 100)
            nilai_ipa = random.randint(95, 100)
            nilai_ing = random.randint(80, 90)
            minat = "Teknologi"
            bakat = random.choice(["Analitis"] * 9 + ["Komunikatif"] * 1)
        elif jurusan == "Kedokteran":
            nilai_mat = random.randint(95, 100)
            nilai_ipa = random.randint(97, 100)
            nilai_ing = random.randint(85, 95)
            minat = "Kesehatan"
            bakat = "Analitis"
        elif jurusan == "Ilmu Gizi":
            nilai_mat = random.randint(80, 85)
            nilai_ipa = random.randint(93, 100)
            nilai_ing = random.randint(85, 95)
            minat = "Kesehatan"
            bakat = "Analitis"
        elif jurusan == "Farmasi":
            nilai_mat = random.randint(90, 95)
            nilai_ipa = random.randint(93, 100)
            nilai_ing = random.randint(85, 95)
            minat = "Kesehatan"
            bakat = "Analitis"
        elif jurusan == "Kesehatan Masyarakat":
            nilai_mat = random.randint(75, 80)
            nilai_ipa = random.randint(88, 93)
            nilai_ing = random.randint(88, 97)
            minat = "Kesehatan"
            bakat = "Komunikatif"
        elif jurusan == "Psikologi":
            nilai_mat = random.randint(65, 75)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(95, 100)
            minat = "Sosial"
            bakat = "Komunikatif"
        elif jurusan == "Ilmu Komunikasi":
            nilai_mat = random.randint(60, 70)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(95, 100)
            minat = "Sosial"
            bakat = "Komunikatif"
        elif jurusan == "Hukum":
            nilai_mat = random.randint(75, 85)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(95, 100)
            minat = "Sosial"
            bakat = "Analitis"
        elif jurusan == "Ilmu Politik":
            nilai_mat = random.randint(65, 75)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(95, 100)
            minat = "Sosial"
            bakat = "Komunikatif"
        elif jurusan == "Pendidikan Guru Sekolah Dasar":
            nilai_mat = random.randint(75, 85)
            nilai_ipa = random.randint(65, 75)
            nilai_ing = random.randint(90, 97)
            minat = "Sosial"
            bakat = "Komunikatif"
        elif jurusan == "Desain Komunikasi Visual":
            nilai_mat = random.randint(60, 70)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(90, 97)
            minat = "Seni"
            bakat = "Kreatif"
        elif jurusan == "Seni Rupa":
            nilai_mat = random.randint(60, 70)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(85, 92)
            minat = "Seni"
            bakat = "Kreatif"
        elif jurusan == "Desain Interior":
            nilai_mat = random.randint(65, 75)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(85, 95)
            minat = "Seni"
            bakat = "Kreatif"
        elif jurusan == "Akuntansi":
            nilai_mat = random.randint(95, 100)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(85, 95)
            minat = "Bisnis"
            bakat = "Analitis"
        elif jurusan == "Manajemen":
            nilai_mat = random.randint(85, 90)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(90, 97)
            minat = "Bisnis"
            bakat = "Komunikatif"
        elif jurusan == "Ekonomi Pembangunan":
            nilai_mat = random.randint(90, 95)
            nilai_ipa = random.randint(60, 70)
            nilai_ing = random.randint(90, 97)
            minat = "Bisnis"
            bakat = "Analitis"

        data.append([nilai_mat, nilai_ipa, nilai_ing, minat, bakat, jurusan])

    return pd.DataFrame(data, columns=[
        "Nilai_Matematika", "Nilai_IPA", "Nilai_Bahasa_Inggris",
        "Minat", "Bakat", "Jurusan"
    ])

# Generate 20.000 data
dataset = generate_data(20000)

# Pastikan distribusi seimbang
balanced_dataset = pd.DataFrame()
samples_per_jurusan = 20000 // len(all_jurusan)
for jurusan in all_jurusan:
    jurusan_data = dataset[dataset["Jurusan"] == jurusan].sample(samples_per_jurusan, replace=True, random_state=42)
    balanced_dataset = pd.concat([balanced_dataset, jurusan_data])

# Tambahkan sisa sampel jika perlu
remaining_samples = 20000 - len(balanced_dataset)
if remaining_samples > 0:
    additional_data = dataset.sample(remaining_samples, random_state=42)
    balanced_dataset = pd.concat([balanced_dataset, additional_data])

# Simpan ke CSV
balanced_dataset.to_csv("dataset_jurusan.csv", index=False)
print("Dataset berhasil disimpan ke 'dataset_jurusan.csv'")
print("Distribusi jurusan:")
print(balanced_dataset["Jurusan"].value_counts())