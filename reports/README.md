# Reportes

Esta carpeta contiene los dos entregables analíticos del proyecto.

## Archivos

- `onpe_peru_2026-1.pbix`: dashboard en Power BI.
- `onpe_peru_2026-1.xlsx`: analítico en Excel con Power Query y pivotes.

## Fuente de datos

Ambos reportes se alimentan del output de:

- https://github.com/oscarzamora/onpeescraper

Salidas usadas:

- `output/mesas_data.txt`
- `output/votos.txt`
- `output/agrupaciones.txt`
- `output/extranjero-ubigeo-continente-pais-ciudad.csv`
- `output/extranjero-continente-pais-ciudad-lat-lon.csv`

`onpeescraper` también provee ubigeo para extranjero y Power Query ya incluye esa información.

En el cruce de ubigeos del Perú hay muy pocos casos sin correspondencia, aparentemente por desactualización del catálogo RENIEC de referencia. Fuera de esos casos puntuales, el resto queda igual.

## Mantenimiento

Para refrescar reportes, seguir la guía en:

- `docs/refresh-reportes.md`
