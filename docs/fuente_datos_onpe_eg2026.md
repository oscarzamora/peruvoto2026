# Fuente de datos: ONPE EG2026 mesa a mesa

## Archivo usado en este repositorio

- Archivo local: `data/onpe_eg2026_mesas_20260420T074202Z.csv`
- Estado: cargado manualmente al proyecto para analisis en Power BI.

## Procedencia

Este CSV fue extraido del dataset publico:

- https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/tree/main

Dataset card (descripcion principal):

- https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa

Archivo de referencia (mismo timestamp de captura):

- https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/blob/main/onpe_eg2026_mesas_20260420T074202Z.csv

README oficial del dataset (documentacion de formato y metodologia):

- https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/blob/main/README.md

## Formato del dataset (segun README oficial)

Descripcion general reportada por la fuente:

- Estructura long-format: 1 fila = mesa x partido.
- Cobertura reportada: 92,766 mesas.
- Contexto: resultados presidenciales primera vuelta EG 2026.

Campos documentados:

- `codigo_mesa` (str): codigo ONPE de 6 digitos.
- `ubigeo` (str): ubigeo de 6 digitos (depto+prov+dist).
- `departamento` (str): nombre del departamento.
- `estado_acta` (str): D/I/P/O.
- `electores_habiles` (Int64): padron habilitado en la mesa.
- `votos_emitidos` (Int64): total votos emitidos.
- `votos_validos` (Int64): votos validos (excluye nulos/blancos).
- `pct_participacion` (float32): porcentaje de participacion.
- `local_votacion` (str): nombre del local.
- `partido_codigo` (str): codigo ONPE del partido (80=BLANCOS, 81=NULOS, 82=IMPUGNADOS).
- `partido` (str): nombre del partido.
- `candidato` (str): candidato presidencial.
- `votos` (Int64): votos obtenidos (null si acta impugnada).
- `pct_votos_validos` (float32): porcentaje sobre votos validos.
- `es_voto_especial` (bool): marca para filas de votos especiales.

## Licencia y notas de uso

- Licencia reportada en dataset card: CC-BY-4.0.
- Fuente base declarada: API publica de ONPE (resultadoelectoral.onpe.gob.pe).
- Para trazabilidad, mantener el nombre del archivo con timestamp original cuando se actualice el dataset.

## Referencias para claridad

- Dataset (Files): https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/tree/main
- Dataset card: https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa
- README fuente: https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/blob/main/README.md
- CSV usado (origen): https://huggingface.co/datasets/Neuracode/onpe-eg2026-mesa-a-mesa/blob/main/onpe_eg2026_mesas_20260420T074202Z.csv
