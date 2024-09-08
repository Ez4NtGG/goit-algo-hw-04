#ЗАВДАННЯ 2
def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cats_list.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_list

cats_info = get_cats_info(r"D:\Projects\goit-algo-hw-04\salary_file2.txt")
print(cats_info)