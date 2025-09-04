import React, { useState, useEffect } from 'react';

export default function Surveys() {
  const [surveys, setSurveys] = useState([]);
  const [newTitle, setNewTitle] = useState('');
  const [preguntas, setPreguntas] = useState([{ dimension: '', texto: '' }]);
  const [error, setError] = useState(null);

  // Carga inicial de encuestas
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/v1/surveys/')
      .then(r => r.json())
      .then(setSurveys)
      .catch(setError);
  }, []);

  // Añadir un campo nuevo de pregunta
  const addPregunta = () => {
    setPreguntas([...preguntas, { dimension: '', texto: '' }]);
  };

  // Actualizar un campo de pregunta
  const updatePregunta = (idx, field, value) => {
    const copy = [...preguntas];
    copy[idx][field] = value;
    setPreguntas(copy);
  };

  // Enviar encuesta + preguntas al endpoint anidado
  const handleCreateFull = () => {
    if (!newTitle.trim()) return;
    // validar que cada pregunta tenga dimensión y texto
    for (let p of preguntas) {
      if (!p.dimension || !p.texto.trim()) {
        setError(new Error('Todas las preguntas deben tener dimensión y texto.'));
        return;
      }
    }
    const payload = {
      titulo: newTitle.trim(),
      preguntas: preguntas.map(p => ({
        dimension: Number(p.dimension),
        texto: p.texto.trim()
      }))
    };

    fetch('http://127.0.0.1:8000/api/v1/surveys-full/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(r => {
        if (!r.ok) throw new Error(`Error ${r.status}`);
        return r.json();
      })
      .then(created => {
        // refresca la lista simple
        return fetch('http://127.0.0.1:8000/api/v1/surveys/')
          .then(r => r.json())
          .then(setSurveys)
          .then(() => created);
      })
      .then(() => {
        // reset del formulario
        setNewTitle('');
        setPreguntas([{ dimension: '', texto: '' }]);
        setError(null);
      })
      .catch(setError);
  };

  return (
    <div style={{ marginTop: '2rem' }}>
      <h2>Encuestas</h2>

      {/* Formulario nested */}
      <div style={{ marginBottom: '1rem' }}>
        <input
          type="text"
          placeholder="Título de nueva encuesta"
          value={newTitle}
          onChange={e => setNewTitle(e.target.value)}
        />
        <button onClick={handleCreateFull} style={{ marginLeft: '0.5rem' }}>
          Crear con preguntas
        </button>

        {preguntas.map((p, idx) => (
          <div key={idx} style={{ marginTop: '0.5rem' }}>
            <select
              value={p.dimension}
              onChange={e => updatePregunta(idx, 'dimension', e.target.value)}
            >
              <option value="">-- Dimensión --</option>
              {dims.map(d => (  // dims viene de App.jsx: pásalo como prop si no existe aquí
                <option key={d.id} value={d.id}>{d.nombre}</option>
              ))}
            </select>
            <input
              type="text"
              placeholder="Texto de la pregunta"
              value={p.texto}
              onChange={e => updatePregunta(idx, 'texto', e.target.value)}
              style={{ marginLeft: '0.5rem' }}
            />
          </div>
        ))}

        <button onClick={addPregunta} style={{ marginTop: '0.5rem' }}>
          + Añadir Pregunta
        </button>
      </div>

      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}

      {/* Lista simple de encuestas */}
      <ul>
        {surveys.map(s => (
          <li key={s.id}>
            #{s.id} — {s.titulo}
          </li>
        ))}
      </ul>
    </div>
  );
}
