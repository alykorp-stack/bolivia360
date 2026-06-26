user_profile = {
    "name": "Natalia",
    "city": "La Paz",
    "zone": "Zona Sur",
    "common_routes": ["Obrajes", "Calacoto", "UPB", "Sopocachi"]
}

tasks = [
    {"task": "Clase en la universidad", "time": "08:00"},
    {"task": "Pagar internet", "time": "Hoy"},
    {"task": "Gimnasio", "time": "18:00"}
]

reports = [
    {
        "type": "Bloqueo",
        "location": "Obrajes, La Paz",
        "severity": "alta",
        "confidence": 90,
        "summary": "Bloqueo parcial en Obrajes",
        "recommendation": "Salir 20 minutos antes o buscar ruta alterna.",
        "repeat_count": 10
    },
    {
        "type": "Fila en trámite",
        "location": "SEGIP Sopocachi",
        "severity": "media",
        "confidence": 82,
        "summary": "Fila larga en SEGIP Sopocachi",
        "repeat_count": 5,
        "recommendation": "Evitar ir por la mañana. Mejor después de las 14:00."

    },
    {
        "type": "Gasolina",
        "location": "Miraflores",
        "severity": "media",
        "confidence": 75,
        "summary": "Fila larga en estación de servicio",
        "repeat_count": 2,
        "recommendation": "Buscar otra estación o cargar más tarde."
    }
]


