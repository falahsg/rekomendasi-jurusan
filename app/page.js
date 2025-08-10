"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [formData, setFormData] = useState({
    nilai_mat: "",
    nilai_ipa: "",
    nilai_ing: "",
    minat: "Teknologi",
    bakat: "Komunikatif",
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);
    setLoading(true);

    try {
      const response = await axios.post(
        "http://103.150.92.168/:5000/predict",
        {
          nilai_mat: parseFloat(formData.nilai_mat),
          nilai_ipa: parseFloat(formData.nilai_ipa),
          nilai_ing: parseFloat(formData.nilai_ing),
          minat: formData.minat,
          bakat: formData.bakat,
        }
      );
      setResult(response.data);
    } catch (err) {
      setError(
        "Gagal terhubung ke server. Pastikan backend berjalan di http://localhost:5000"
      );
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-blue-700 to-blue-500 flex items-center justify-center p-6">
      <div className="max-w-lg w-full bg-white/20 backdrop-blur-lg rounded-3xl shadow-2xl p-8 space-y-6 border border-white/30 animate-fade-in">
        <h1 className="text-4xl font-extrabold text-center text-white drop-shadow-lg">
          🎓 Rekomendasi Jurusan
        </h1>
        <form onSubmit={handleSubmit} className="space-y-5">
          {[
            { label: "Nilai Matematika", name: "nilai_mat" },
            { label: "Nilai IPA", name: "nilai_ipa" },
            { label: "Nilai Bahasa Inggris", name: "nilai_ing" },
          ].map((field) => (
            <div key={field.name}>
              <label className="block text-sm font-semibold text-white drop-shadow">
                {field.label}
              </label>
              <input
                type="number"
                name={field.name}
                value={formData[field.name]}
                onChange={handleChange}
                required
                className="mt-1 block w-full px-4 py-3 border border-white/40 rounded-xl bg-white/30 text-white placeholder-white/70 shadow-inner focus:ring-4 focus:ring-blue-300 focus:border-white outline-none transition"
                placeholder="Masukkan nilai (0-100)"
              />
            </div>
          ))}
          <div>
            <label className="block text-sm font-semibold text-white drop-shadow">
              Minat
            </label>
            <div className="relative">
              <select
                name="minat"
                value={formData.minat}
                onChange={handleChange}
                className="w-full px-4 py-3 rounded-lg border border-white/30 bg-white/10 backdrop-blur-md text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-blue-300 appearance-none"
              >
                <option className="text-gray-800" value="Teknologi">
                  Teknologi
                </option>
                <option className="text-gray-800" value="Kesehatan">
                  Kesehatan
                </option>
                <option className="text-gray-800" value="Sosial">
                  Sosial
                </option>
                <option className="text-gray-800" value="Seni">
                  Seni
                </option>
                <option className="text-gray-800" value="Bisnis">
                  Bisnis
                </option>
              </select>

              <span className="absolute right-3 top-1/2 -translate-y-1/2 text-white pointer-events-none">
                ▼
              </span>
            </div>
          </div>
          <div>
            <label className="block text-sm font-semibold text-white drop-shadow">
              Bakat
            </label>
            <div className="relative">
              <select
                name="bakat"
                value={formData.bakat}
                onChange={handleChange}
                className="w-full px-4 py-3 rounded-lg border border-white/30 bg-white/10 backdrop-blur-md text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-blue-300 appearance-none"
              >
                <option className="text-gray-800" value="Komunikatif">
                  Komunikatif
                </option>
                <option className="text-gray-800" value="Analitis">
                  Analitis
                </option>
                <option className="text-gray-800" value="Praktis">
                  Praktis
                </option>
                <option className="text-gray-800" value="Kreatif">
                  Kreatif
                </option>
              </select>

              <span className="absolute right-3 top-1/2 -translate-y-1/2 text-white pointer-events-none">
                ▼
              </span>
            </div>
          </div>
          <button
            type="submit"
            disabled={loading}
            className={`w-full py-3 px-4 bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-bold rounded-xl shadow-lg hover:scale-[1.02] focus:ring-4 focus:ring-blue-300 transition transform duration-300 ${
              loading ? "opacity-50 cursor-not-allowed" : ""
            }`}
          >
            {loading ? "Memproses..." : "🚀 Prediksi Jurusan"}
          </button>
        </form>

        {error && (
          <div className="p-4 bg-red-500/80 text-white rounded-lg text-center shadow-md animate-fade-in">
            {error}
          </div>
        )}

        {result && (
          <div className="p-6 bg-white/30 rounded-xl shadow-inner text-center space-y-2 animate-fade-in border border-white/40">
            <h2 className="text-2xl font-bold text-white drop-shadow">
              Hasil Prediksi
            </h2>
            <p className="text-lg text-white">
              <span className="font-medium">Jurusan:</span>{" "}
              <span className="text-yellow-300 font-semibold">
                {result.jurusan}
              </span>
            </p>
            <p className="text-lg text-white">
              <span className="font-medium">Akurasi:</span>{" "}
              {result.akurasi.toFixed(2)}%
            </p>
            <p className="text-lg text-white">
              <span className="font-medium">Probabilitas:</span>{" "}
              {result.probabilitas.toFixed(2)}%
            </p>
          </div>
        )}
      </div>

      <style jsx>{`
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(15px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fade-in {
          animation: fade-in 0.5s ease-out;
        }
      `}</style>
    </div>
  );
}
