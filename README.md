# PeruVoto 2026

Analitico basico para transparencia electoral en Peru, construido sobre data publica de ONPE y alimentado por el output del scraper:

- https://github.com/oscarzamora/onpeescraper

Este repo concentra dos entregables:

1. Reporte Power BI: `reports/onpe_peru_2026-1.pbix`
2. Reporte Excel (Power Query + pivotes): `reports/onpe_peru_2026-1.xlsx`

Ambos archivos de reporte ya estan apuntando a la fuente de datos publica proveniente de `onpeescraper` (archivos de `output/` y apoyo de `source_data/`).

## Objetivo

Poner a disposicion de cualquier ciudadano una forma simple de explorar la data electoral publica, con foco en:

- Transparencia
- Trazabilidad de origen
- Reproducibilidad del analisis

## Fuente de datos

La fuente de verdad de este proyecto es el directorio `output/` generado por onpeescraper, en particular:

- `output/mesas_data.txt`
- `output/votos.txt`
- `output/agrupaciones.txt`

Como insumos de apoyo para enriquecimiento:

- `source_data/geodir-ubigeo-reniec.xlsx`
- `source_data/candidato.txt` (mapeo manual opcional)

Todo lo anterior proviene de data publica.

En este proyecto, `onpeescraper` ya esta corrido: aqui no se ejecuta scraping.
Se usa unicamente como fuente de datos de entrada para el analitico.

## Flujo recomendado

No se requiere correr ningun proceso adicional para usar este repositorio.
Los reportes ya estan predeterminados y apuntan a la fuente publica de datos de `onpeescraper`.

Operacion habitual:

1. Abrir `reports/onpe_peru_2026-1.xlsx` y refrescar Power Query.
2. Abrir `reports/onpe_peru_2026-1.pbix` y refrescar el modelo.

## Estructura actual

```
peruvoto2026/
|-- README.md
|-- assets/
|   |-- 1-PanelGeneral.jpg
|   |-- 2-PanelCandidatos.jpg
|   `-- 3-MapaPeru.jpg
|-- reports/
    |-- onpe_peru_2026-1.pbix
    `-- onpe_peru_2026-1.xlsx

## Reporte Power BI

`reports/onpe_peru_2026-1.pbix` representa 3 vistas principales (ver screenshots):

1. Panel general
2. Panel de candidatos
3. Mapa Peru

Adicionalmente, el reporte incluye filtros predeterminados para:

- Mesas 900K
- Mesas que abrieron el 13 de abril

Esto permite revisar esos subconjuntos de forma directa para los suspicaces, sin tener que armar filtros manuales desde cero.

## Reporte Excel

`reports/onpe_peru_2026-1.xlsx` contiene:

- Power Query para ingesta y transformacion basica del output del scraper.
- Tablas dinamicas para analitica simple por candidato y geografia.

## Nota de transparencia

Este repositorio no inventa data electoral ni reemplaza resultados oficiales. Solo organiza y visualiza data publica para facilitar su lectura y fiscalizacion ciudadana.

## Screenshots finales

### 1. Panel General

![Panel General](assets/1-PanelGeneral.jpg)

### 2. Panel Candidatos

![Panel Candidatos](assets/2-PanelCandidatos.jpg)

### 3. Mapa Peru

![Mapa Peru](assets/3-MapaPeru.jpg)


