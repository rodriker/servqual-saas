import React, { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('Cargando…');

  useEffect(() => {
    // Llama al backend Django
    fetch('http://127.0.0.1:8000/api/v1/hello/')
      .then((resp) => resp.json())
      .then((data) => setMessage(data.message))
      .catch((err) => setMessage('Error al conectar'));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Mensaje desde el backend:</h1>
      <p style={{ fontSize: 24, color: '#007ACC' }}>{message}</p>
    </div>
  );
}

export default App;
