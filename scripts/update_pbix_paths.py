#!/usr/bin/env python3
r"""
Actualizar rutas hardcodeadas en PBIX a rutas relativas.
Cambia rutas absolutas como 'C:\Users\...\data\archivo.csv' a '../data/archivo.csv'
"""

import os
import shutil
import zipfile
import json
import re
import sys
from pathlib import Path
from datetime import datetime

def backup_pbix(pbix_path):
    """Crear backup del PBIX antes de modificar."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{pbix_path}.backup_{timestamp}"
    shutil.copy2(pbix_path, backup_path)
    print(f"✓ Backup creado: {backup_path}")
    return backup_path

def extract_pbix(pbix_path, extract_dir):
    """Extraer PBIX (es un ZIP)."""
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    os.makedirs(extract_dir, exist_ok=True)
    
    with zipfile.ZipFile(pbix_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"✓ PBIX extraído a: {extract_dir}")

def find_and_replace_paths(extract_dir, replacements):
    """Buscar y reemplazar rutas en archivos de configuración."""
    changes_made = []
    
    # Buscar en TODOS los archivos (excepto binarios comprimidos)
    exclude_files = {'DataModel', 'SecurityBindings', 'Layout'}
    
    for root, dirs, files in os.walk(extract_dir):
        for filename in files:
            if filename in exclude_files:
                continue
            
            filepath = os.path.join(root, filename)
            try:
                # Intentar leer como texto
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Si está mayormente vacío, saltar
                if len(content) < 10:
                    continue
                
                original_content = content
                
                # Aplicar reemplazos
                for old, new in replacements:
                    if old in content:
                        content = content.replace(old, new)
                        rel_path = os.path.relpath(filepath, extract_dir)
                        changes_made.append(f"{rel_path}: {old} → {new}")
                
                # Guardar si hubo cambios
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    rel_path = os.path.relpath(filepath, extract_dir)
                    print(f"  ✓ Actualizado: {rel_path}")
            
            except Exception as e:
                # Silencioso para archivos binarios
                pass
    
    return changes_made

def recompress_pbix(extract_dir, pbix_path):
    """Recomprimir PBIX desde archivos extraídos."""
    # Remover archivo existente
    if os.path.exists(pbix_path):
        os.remove(pbix_path)
    
    # Crear nuevo ZIP
    with zipfile.ZipFile(pbix_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, extract_dir)
                zipf.write(file_path, arcname)
    
    print(f"✓ PBIX recomprimido: {pbix_path}")

def main():
    # Configuración
    pbix_path = "reports/onpe.pbix"
    extract_dir = "reports/onpe_extracted_temp"
    
    # Validar que PBIX existe
    if not os.path.exists(pbix_path):
        print(f"✗ Error: No se encontró {pbix_path}")
        return False
    
    print("=" * 70)
    print("ACTUALIZADOR DE RUTAS EN PBIX")
    print("=" * 70)
    
    # 1. Backup
    print("\n[1/5] Creando backup...")
    backup_pbix(pbix_path)
    
    # 2. Extraer
    print("\n[2/5] Extrayendo PBIX...")
    extract_pbix(pbix_path, extract_dir)
    
    # 3. Detectar rutas a cambiar
    print("\n[3/5] Buscando rutas hardcodeadas...")
    
    # Buscar todas las rutas que contengan 'data/' en archivos extraídos
    patterns_to_replace = []
    
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            if file in ['DiagramLayout', 'Metadata', 'Settings']:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Buscar rutas absolutas con 'data/'
                    matches = re.finditer(r'[C-Z]:\\[^"]*?data\\[^"]*', content)
                    for match in matches:
                        old_path = match.group(0)
                        # Convertir a ruta relativa
                        if 'onpe_eg2026_mesas' in old_path:
                            new_path = '../data/onpe_eg2026_mesas_20260420T074202Z.csv'
                        elif 'geodir-ubigeo' in old_path or 'ubigeo' in old_path.lower():
                            new_path = '../data/geodir-ubigeo-reniec.xlsx'
                        else:
                            new_path = old_path.replace('\\', '/').split('data/')
                            if len(new_path) > 1:
                                new_path = f'../data/{new_path[-1]}'
                            else:
                                continue
                        
                        patterns_to_replace.append((old_path, new_path))
                        print(f"  Encontrado: {old_path}")
                        print(f"             → {new_path}")
                
                except Exception as e:
                    print(f"  ⚠ Error leyendo {file}: {e}")
    
    if not patterns_to_replace:
        print("  ⚠ No se encontraron rutas hardcodeadas a reemplazar")
    
    # 4. Reemplazar
    print("\n[4/5] Reemplazando rutas...")
    changes = find_and_replace_paths(extract_dir, patterns_to_replace)
    
    if changes:
        for change in changes:
            print(f"  • {change}")
    else:
        print("  (Sin cambios detectados en archivos de texto)")
    
    # 5. Recomprimir
    print("\n[5/5] Recomprimiendo PBIX...")
    recompress_pbix(extract_dir, pbix_path)
    
    # Limpiar temporal
    print("\nLimpiando archivos temporales...")
    shutil.rmtree(extract_dir)
    
    print("\n" + "=" * 70)
    print("✓ Actualización completada exitosamente")
    print("=" * 70)
    print("\nProximos pasos:")
    print("1. Abre el PBIX en Power BI Desktop")
    print("2. Aparecerá un aviso de rutas movidas")
    print("3. Selecciona 'Cargar' para actualizar las referencias")
    print("4. Guarda el archivo")
    print("\nSi algo falla, tienes el backup:")
    print(f"  - Busca archivos .backup_* en la carpeta reports/")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
