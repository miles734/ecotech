import json
from datetime import datetime
from pathlib import Path
from urllib import request

HISTORIAL_PATH = Path(__file__).resolve().parents[1] / "historial_divisas.json"
TASAS_FALLBACK = {"CLP": 980.5, "ARS": 1000.0, "BRL": 5.2}


def obtener_tasas_dolar():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=CLP,ARS,BRL"
    try:
        peticion = request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with request.urlopen(peticion, timeout=10) as respuesta:
            datos = json.loads(respuesta.read().decode("utf-8"))
        tasas = datos.get("rates") or {}
        if all(moneda in tasas for moneda in ("CLP", "ARS", "BRL")):
            return {
                "CLP": float(tasas["CLP"]),
                "ARS": float(tasas["ARS"]),
                "BRL": float(tasas["BRL"]),
            }
    except Exception:
        pass
    return TASAS_FALLBACK.copy()


def registrar_historial_consulta(cantidad_usd: float, resultado: dict):
    historial = obtener_historial_divisas()
    historial.append(
        {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cantidad_usd": float(cantidad_usd),
            "resultado": resultado,
        }
    )
    HISTORIAL_PATH.write_text(json.dumps(historial[-20:], ensure_ascii=False, indent=2), encoding="utf-8")


def obtener_historial_divisas():
    if not HISTORIAL_PATH.exists():
        return []
    try:
        with HISTORIAL_PATH.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos if isinstance(datos, list) else []
    except Exception:
        return []


def consultar_cotizacion_dolar(cantidad_usd: float):
    cantidad = float(cantidad_usd)
    if cantidad < 0:
        raise ValueError("La cantidad en USD no puede ser negativa.")

    tasas = obtener_tasas_dolar()
    conversion = {
        "CLP": round(cantidad * tasas["CLP"], 2),
        "ARS": round(cantidad * tasas["ARS"], 2),
        "BRL": round(cantidad * tasas["BRL"], 2),
    }
    registrar_historial_consulta(cantidad, conversion)
    return conversion
