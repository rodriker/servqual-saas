import React, { useState, useEffect } from 'react'
import Surveys from './Surveys';  // Importa tu componente de encuestas

function App() {
  const [dims, setDims] = useState([]);

useEffect(() => {
  fetch('http://127.0.0.1:8000/api/v1/dimensions/')
    .then(r => r.json())
    .then(data => {
      console.log('dimensiones desde React:', data);
      setDims(data);
    })
    .catch(err => {
      console.error('error al cargar dimensiones:', err);
      setDims([]);
    });
}, []);


  return (
    <div style={{ padding: '2rem' }}>
      <h1>Dimensiones SERVQUAL</h1>
      <ul>
        {dims.map(d => (
          <li key={d.id}>
            <strong>{d.nombre}</strong>: {d.descripcion}
          </li>
        ))}
      </ul>

      {/* Aquí insertamos el componente Surveys y le pasamos las dimensiones */}
      <Surveys dims={dims} />
    </div>
  );
}

export default App;
