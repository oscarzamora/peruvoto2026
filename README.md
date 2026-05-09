# peruvoto2026

Repositorio del proyecto Power BI.

## Origen de la data (fuente oficial)

Este repositorio incluye copias locales de archivos descargados desde fuentes externas.
La procedencia exacta es la siguiente:

| Archivo local en este repo | Origen exacto | Referencia de formato |
|---|---|---|
| data/onpe_eg2026_mesas_20260420T074202Z.csv | https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/blob/main/onpe_eg2026_mesas_20260420T074202Z.csv | https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/blob/main/README.md |
| data/geodir-ubigeo-reniec.xlsx | https://account.geodir.co/resources/file/recursos/geodir-ubigeo-reniec.xlsx | [docs/fuente_datos_ubigeo_reniec.md](docs/fuente_datos_ubigeo_reniec.md) |

Referencias principales del dataset electoral:

- https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa
- https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/tree/main

## Estructura

- reports/ - archivos .pbix y .pbit
- data/ - archivos de datos locales de ejemplo (solo no sensibles)
- docs/ - notas, requerimientos y decisiones

## Notas de Git

- Los archivos .pbix se versionan con Git LFS (ver [.gitattributes](.gitattributes)).
- Evita subir credenciales o exportaciones sensibles.

## Documentacion de datos

- CSV ONPE EG2026: [docs/fuente_datos_onpe_eg2026.md](docs/fuente_datos_onpe_eg2026.md)
- XLSX ubigeo RENIEC: [docs/fuente_datos_ubigeo_reniec.md](docs/fuente_datos_ubigeo_reniec.md)

## Contenido del reporte

### Panel General
Expone los votos recibidos por todos los candidatos en la primera vuelta de las Elecciones Generales 2026 del Perú.
Incluye filtros por:
- Departamento
- Provincia  
- Distrito

También muestra métricas de votos en blanco, votos nulos y cantidad total de mesas.

### Otros paneles
- **Candidato**: Análisis por candidato presidencial
- **Mesas 900K**: Mesas especiales (centros excepcionales con 900k+ votantes)
- **13 de Abel**: [Descripción por completar]
- **Mapa 900K**: Visualización geográfica de mesas especiales

## Inicio rápido

1. Coloca tus archivos de reporte de Power BI en reports/.
2. Haz commit de los cambios.
3. Haz push a tu repositorio remoto de Git.
