export default function RootLayout({ children }) {
  return (
    <html lang="id">
      <head>
        <script src="https://cdn.tailwindcss.com"></script>
        <title>Rekomendasi Jurusan</title>
      </head>
      <body>{children}</body>
    </html>
  );
}
