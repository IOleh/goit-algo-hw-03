import os
import shutil
import sys

def list_files_and_dirs(path):
    """Cписок файлів та директорій"""
    print(f"\nВміст теки {path}:")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

def parse_args():
    """Парсинг аргументів командного рядка"""
    if len(sys.argv) < 2:
        print("Вкажіть шлях до вихідної директорії.")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'
    
    return src_dir, dest_dir

def copy_and_sort_files(src_dir, dest_dir):
    """Рекурсивно копіює та сортує файли за розширеннями"""
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                ext = file.split('.')[-1] if '.' in file else 'no_extension'
                target_dir = os.path.join(dest_dir, ext)
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                
                shutil.copy(file_path, target_dir)
    
    except Exception as e:
        print(f"Помилка під час копіювання: {e}")

def main():
    # Парсинг аргументів
    src_dir, dest_dir = parse_args()

    # Вивести список файлів і директорій у вихідній директорії до сортування
    list_files_and_dirs(src_dir)

    # Копіювання та сортування файлів
    copy_and_sort_files(src_dir, dest_dir)

    # Вивести список файлів і директорій у новій директорії після сортування
    list_files_and_dirs(dest_dir)

if __name__ == "__main__":
    main()

# Приклад: Запуск прогами: python sort_files.py "D:\Downloads" "D:\Downloads_sorted"
