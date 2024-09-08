#ЗАВДАННЯ 1
def total_salary(path):
    total_salary = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str) 
                
                total_salary += salary
                count += 1

        average_salary = total_salary / count if count > 0 else 0
        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0 
    except ValueError as e:
        print(f"Помилка у даних файлу: {e}")
        return 0, 0 
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return 0, 0 

total, average = total_salary(r"D:\Projects\goit-algo-hw-04\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")