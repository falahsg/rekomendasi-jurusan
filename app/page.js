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
      const response = await axios.post("http://localhost:5000/predict", {
        nilai_mat: parseFloat(formData.nilai_mat),
        nilai_ipa: parseFloat(formData.nilai_ipa),
        nilai_ing: parseFloat(formData.nilai_ing),
        minat: formData.minat,
        bakat: formData.bakat,
      });
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
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-blue-700 to-blue-500 flex items-center justify-center p-4">
      <div className="max-w-lg w-full bg-white rounded-2xl shadow-xl p-8 space-y-6">
        <h1 className="text-3xl font-bold text-center text-gray-800">
          Rekomendasi Jurusan
        </h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Nilai Matematika
            </label>
            <input
              type="number"
              name="nilai_mat"
              value={formData.nilai_mat}
              onChange={handleChange}
              required
              className="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
              placeholder="Masukkan nilai (0-100)"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Nilai IPA
            </label>
            <input
              type="number"
              name="nilai_ipa"
              value={formData.nilai_ipa}
              onChange={handleChange}
              required
              className="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
              placeholder="Masukkan nilai (0-100)"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Nilai Bahasa Inggris
            </label>
            <input
              type="number"
              name="nilai_ing"
              value={formData.nilai_ing}
              onChange={handleChange}
              required
              className="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
              placeholder="Masukkan nilai (0-100)"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Minat
            </label>
            <select
              name="minat"
              value={formData.minat}
              onChange={handleChange}
              className="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="Teknologi">Teknologi</option>
              <option value="Kesehatan">Kesehatan</option>
              <option value="Sosial">Sosial</option>
              <option value="Seni">Seni</option>
              <option value="Bisnis">Bisnis</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Bakat
            </label>
            <select
              name="bakat"
              value={formData.bakat}
              onChange={handleChange}
              className="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="Komunikatif">Komunikatif</option>
              <option value="Analitis">Analitis</option>
              <option value="Praktis">Praktis</option>
              <option value="Kreatif">Kreatif</option>
            </select>
          </div>
          <button
            type="submit"
            disabled={loading}
            className={`w-full py-3 px-4 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-300 ${
              loading ? "opacity-50 cursor-not-allowed" : ""
            }`}
          >
            {loading ? "Memproses..." : "Prediksi Jurusan"}
          </button>
        </form>

        {error && (
          <div className="p-4 bg-red-100 text-red-700 rounded-lg text-center">
            {error}
          </div>
        )}

        {result && (
          <div className="p-6 bg-blue-50 rounded-lg shadow-inner text-center space-y-2 animate-fade-in">
            <h2 className="text-2xl font-semibold text-gray-800">
              Hasil Prediksi
            </h2>
            <p className="text-lg">
              <span className="font-medium">Jurusan:</span>{" "}
              <span className="text-blue-600">{result.jurusan}</span>
            </p>
            <p className="text-lg">
              <span className="font-medium">Akurasi:</span>{" "}
              {result.akurasi.toFixed(2)}%
            </p>
            <p className="text-lg">
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
            transform: translateY(10px);
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
