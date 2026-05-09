# Fuente de datos: Ubigeo RENIEC (Geodir)

## Archivo usado en este repositorio

- Archivo local: data/geodir-ubigeo-reniec.xlsx
- Estado: cargado manualmente al proyecto para enriquecer analisis geografico con coordenadas.

## Procedencia

Este archivo fue extraido de:

- https://account.geodir.co/resources/file/recursos/geodir-ubigeo-reniec.xlsx

## Estructura reportada del archivo

Columnas disponibles:

- Ubigeo
- Distrito
- Provincia
- Departamento
- Poblacion
- Superficie
- Y
- X

## Ejemplo de registros

| Ubigeo | Distrito    | Provincia    | Departamento | Poblacion | Superficie | Y       | X        |
|--------|-------------|--------------|--------------|-----------|------------|---------|----------|
| 010101 | Chachapoyas | Chachapoyas  | Amazonas     | 29,171    | 153.78     | -6.2294 | -77.8714 |
| 010102 | Asuncion    | Chachapoyas  | Amazonas     | 288       | 25.71      | -6.0317 | -77.7122 |

## Notas de uso

- Y y X se usan como coordenadas para analisis espacial.
- Para mantener trazabilidad, conservar nombre de archivo y fecha de incorporacion en commits.

## Referencias para claridad

- Recurso fuente (XLSX): https://account.geodir.co/resources/file/recursos/geodir-ubigeo-reniec.xlsx
