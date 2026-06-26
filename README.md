# Bolivia 360

Tu guía inteligente para explorar Bolivia, construida con Streamlit y Claude AI.

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

## Variables de entorno

| Variable | Descripción |
|---|---|
| `ANTHROPIC_API_KEY` | API key de Anthropic (Claude) |
| `SUPABASE_URL` | URL de tu proyecto Supabase |
| `SUPABASE_KEY` | Anon key de Supabase |
| `APP_ENV` | `development` (usa mock data) o `production` |

## Ejecutar la app

```bash
streamlit run app/main.py
```

En modo `development` (por defecto), la app usa datos mock sin necesidad de Supabase.

## Tecnologias

- **Frontend**: Streamlit
- **IA**: Anthropic Claude (claude-sonnet-4-6)
- **Base de datos**: Supabase (PostgreSQL)
- **Landing**: HTML + CSS vanilla
