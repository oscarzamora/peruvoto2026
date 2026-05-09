# Screenshots de los Paneles

Esta carpeta contiene capturas de pantalla de los 5 paneles del reporte Power BI peruvoto2026.

## Archivos

| Panel | Archivo | Descripción |
|-------|---------|-------------|
| General | `01-panel-general.png` | Visión consolidada de votos por candidato con filtros geográficos |
| Candidato | `02-panel-candidato.png` | Análisis por candidato con tabla de votos por localidad |
| Mesas 900K | `03-panel-mesas-900k.png` | Resultados de mesas especiales |
| 13 de Abril | `04-panel-13-abril.png` | Snapshot de resultados del 13 de abril de 2026 |
| Mapa 900K | `05-panel-mapa-900k.png` | Visualización geográfica de mesas 900K |

## Cómo agregar screenshots

1. Abre el PBIX en Power BI Desktop (`reports/onpe.pbix`)
2. Para cada panel, toma una captura de pantalla (PrintScreen)
3. Pega la imagen en una herramienta como Paint o captura de pantalla
4. Guarda como PNG en esta carpeta con el nombre especificado arriba
5. Haz commit y push

Ej:
```bash
git add assets/screenshots/*.png
git commit -m "Agregar screenshots de paneles"
git push
```
