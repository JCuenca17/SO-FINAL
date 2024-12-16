import os
import shutil
import time
from datetime import datetime

def create_backup(source_dir, backup_dir):
    """
    Crear un backup de un directorio
    """
    # Crear directorio de backup si no existe
    os.makedirs(backup_dir, exist_ok=True)
    
    # Nombre del backup con timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'backup_{timestamp}'
    full_backup_path = os.path.join(backup_dir, backup_name)
    
    try:
        # Copiar directorio
        shutil.copytree(source_dir, full_backup_path)
        
        print(f"Backup creado: {full_backup_path}")
        
        # Listar archivos en el backup
        print("\nArchivos respaldados:")
        for root, dirs, files in os.walk(full_backup_path):
            level = root.replace(full_backup_path, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
        
        return True
    except Exception as e:
        print(f"Error al crear backup: {e}")
        return False

def cleanup_old_backups(backup_dir, days_to_keep=7):
    """
    Eliminar backups antiguos
    """
    current_time = time.time()
    
    for filename in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, filename)
        
        # Verificar si es un directorio de backup
        if os.path.isdir(file_path):
            # Obtener tiempo de modificación
            file_modified = os.path.getmtime(file_path)
            
            # Calcular días transcurridos
            days_passed = (current_time - file_modified) / (24 * 3600)
            
            if days_passed > days_to_keep:
                try:
                    shutil.rmtree(file_path)
                    print(f"Backup antiguo eliminado: {filename}")
                except Exception as e:
                    print(f"Error al eliminar backup: {e}")

def main():
    # Directorios a respaldar (ajustar según necesidad)
    source_directories = [
        '/home/usuario/documentos',
        '/home/usuario/proyectos'
    ]
    
    backup_base_dir = '/home/usuario/backups'
    
    for source_dir in source_directories:
        create_backup(source_dir, backup_base_dir)
    
    # Limpiar backups antiguos
    cleanup_old_backups(backup_base_dir)

if __name__ == '__main__':
    main()