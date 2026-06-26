import json
from google import genai
from config import GOOGLE_API_KEY


client = genai.Client(api_key=GOOGLE_API_KEY)


def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


def clean_json_response(raw_text: str) -> dict:
    """
    Limpia la respuesta de Gemini y la convierte en diccionario.
    Es necesario porque a veces Gemini devuelve el JSON dentro de ```json.
    """
    try:
        cleaned = raw_text.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned)
    except Exception:
        return {}


def analyze_report(description: str, location: str, category: str) -> dict:
    """
    Analiza un reporte ciudadano.
    La IA clasifica el tipo de problema, gravedad, confianza y recomendación.
    """

    prompt = f"""
Eres una IA que analiza reportes ciudadanos en Bolivia.

Tu tarea es convertir reportes escritos por personas en información estructurada.

Categoría seleccionada por el usuario:
{category}

Ubicación:
{location}

Reporte:
{description}

Devuelve SOLO JSON válido con esta estructura exacta:

{{
  "type": "",
  "location": "",
  "severity": "",
  "confidence": 0,
  "summary": "",
  "recommendation": "",
  "affected_people": "",
  "is_reliable": true,
  "ai_classification": {{
    "detected_category": "",
    "category_reason": "",
    "detected_location": "",
    "severity_reason": "",
    "reliability_reason": "",
    "keywords_detected": []
  }}
}}

Reglas:
- "type" debe ser una de estas opciones:
  bloqueo, tramite, gasolina, transporte, agua_luz, educacion, seguridad, otro.
- "severity" debe ser: baja, media o alta.
- "confidence" debe ser un número entre 0 y 100.
- "summary" debe ser corto y claro.
- "recommendation" debe decir qué debería hacer el usuario.
- "affected_people" debe explicar a quién afecta.
- "is_reliable" debe ser true o false.
- No escribas nada fuera del JSON.
"""

    raw_response = ask_gemini(prompt)
    data = clean_json_response(raw_response)

    if data:
        return data

    # Respuesta de respaldo si Gemini no devuelve JSON válido
    return {
        "type": category.lower(),
        "location": location,
        "severity": "media",
        "confidence": 60,
        "summary": description,
        "recommendation": "Revisar esta situación antes de salir.",
        "affected_people": "Personas cercanas a la zona reportada.",
        "is_reliable": False,
        "ai_classification": {
            "detected_category": category,
            "category_reason": "No se pudo procesar completamente con IA.",
            "detected_location": location,
            "severity_reason": "Clasificación por defecto.",
            "reliability_reason": "Se necesita más información.",
            "keywords_detected": []
        }
    }


def generate_my_day(user_profile: dict, tasks: list, reports: list) -> str:
    """
    Genera el resumen personalizado de Mi Día.
    Usa tareas del usuario y reportes relevantes.
    """

    prompt = f"""
Eres el copiloto personal de Bolivia360.

Tu objetivo es ayudar a una persona en Bolivia a organizar su día.

Perfil del usuario:
{user_profile}

Tareas del día:
{tasks}

Reportes ciudadanos relevantes:
{reports}

Genera un resumen breve y útil con este formato:

1. Saludo corto.
2. Checklist del día.
3. Alertas que podrían afectar al usuario.
4. Recomendaciones concretas.

No seas largo. Escribe como una app diaria, clara y práctica.
"""

    return ask_gemini(prompt)


def edit_my_day(user_message: str, current_tasks: list) -> dict:
    """
    Permite que el Copiloto IA edite Mi Día.
    Por ejemplo: agregar tareas, mover tareas o cancelar tareas.
    """

    prompt = f"""
Eres el Copiloto IA de Bolivia360.

El usuario quiere modificar su día.

Mensaje del usuario:
{user_message}

Tareas actuales:
{current_tasks}

Devuelve SOLO JSON válido con esta estructura exacta:

{{
  "action": "",
  "task": "",
  "time": "",
  "recommendation": ""
}}

Reglas:
- "action" debe ser una de estas opciones:
  add_task, remove_task, move_task, explain.
- Si el usuario quiere agregar algo, usa "add_task".
- Si el usuario quiere cancelar algo, usa "remove_task".
- Si el usuario quiere cambiar horario, usa "move_task".
- Si solo necesita consejo, usa "explain".
- "task" debe ser la tarea detectada.
- "time" debe ser la hora o fecha si aparece.
- "recommendation" debe explicar qué hiciste o qué recomiendas.
- No escribas nada fuera del JSON.
"""

    raw_response = ask_gemini(prompt)
    data = clean_json_response(raw_response)

    if data:
        return data

    return {
        "action": "explain",
        "task": user_message,
        "time": "",
        "recommendation": "No pude modificar automáticamente tu día, pero registré tu solicitud."
    }