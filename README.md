# Bolivia 360

Hacer Bolivia predecible

## Estructura

```
bolivia360/
├── app/
│   ├── main.py              # Pantalla de inicio
│   ├── ai.py                # Integración con Claude AI
│   ├── database.py          # Capa de datos (Supabase)
│   ├── recommender.py       # Motor de recomendaciones
│   ├── mock_data.py         # Datos de prueba
│   └── pages/
│       ├── mi_dia.py        # Generador de itinerarios
│       ├── reportar.py      # Reporte de experiencias
│       ├── bolivia_en_vivo.py  # Eventos y tendencias
│       └── copiloto_ia.py   # Chat con IA
├── landing/
│   ├── index.html           # Página de presentación
│   └── styles.css
├── docs/
│   ├── pitch.md             # Pitch del proyecto
│   └── demo_script.md       # Script para demo
├── config.py                # Configuración (no commitear con secrets)
├── config.example.py        # Plantilla de configuración
└── requirements.txt
```

## Configuración

1. Clona el repositorio
2. Crea un entorno virtual: `python -m venv .venv && .venv\Scripts\activate`
3. Instala dependencias: `pip install -r requirements.txt`
4. Copia la configuración: copia `config.example.py` a `config.py` y llena tus credenciales
5. Alternativamente, crea un archivo `.env` con las variables de entorno


## Tecnologias

- **Frontend**: Streamlit
- **IA**: Gemini API
- **Base de datos**: Supabase 
- **Landing**: HTML + CSS vanilla
