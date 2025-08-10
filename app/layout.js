import "./globals.css"; // Impor CSS lokal

export default function RootLayout({ children }) {
  return (
    <html lang="id">
      <head>
        {/* Hapus <script src="https://cdn.tailwindcss.com"> */}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Sistem Rekomendasi Jurusan</title> {/* Judul opsional */}
      </head>
      <body>{children}</body>
    </html>
  );
}
