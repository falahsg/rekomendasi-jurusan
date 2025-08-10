import "./globals.css";

export default function RootLayout({ children }) {
  return (
    <html lang="id">
      <head>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Sistem Rekomendasi Jurusan</title>
      </head>
      <body>{children}</body>
    </html>
  );
}
