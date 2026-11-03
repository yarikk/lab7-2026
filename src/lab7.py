try:
    with open("grades.txt", "w", encoding="utf-8") as f:
        f.write("Іванов,Петро,85\n")
        f.write("Петренко,Олена,92\n")
        f.write("Сидоренко,Анна,78\n")
        f.write("Коваленко,Максим,96\n")
        f.write("Бондаренко,Ірина,88\n")
except IOError as e:
    print(f"Помилка при створенні файлу grades.txt: {e}")


print("--- Завдання 1-2: Читання файлу grades.txt та обчислення середнього бала ---")
total_grades = 0
count = 0
students_data = []

try:
    with open("grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Пропускаємо порожні рядки
            
            parts = line.split(",")
            if len(parts) != 3:
                raise ValueError(f"Невірний формат рядка у файлі: '{line}'. Очікується 'Прізвище,Ім’я,Оцінка'.")
            
            surname, name, grade_str = parts[0], parts[1], parts[2]
            
            # Конвертуємо оцінку в число
            grade = float(grade_str)
            
            total_grades += grade
            count += 1
            students_data.append({"surname": surname, "name": name, "grade": grade})
            
    if count > 0:
        average_grade = total_grades / count
        print(f"Середній бал студентів: {average_grade:.2f}")
    else:
        print("Файл grades.txt виявився порожнім.")

except FileNotFoundError:
    print("Помилка: Файл 'grades.txt' не знайдено!")
except ValueError as e:
    print(f"Помилка обробки даних (ValueError): {e}")
except IOError as e:
    print(f"Помилка вводу-виводу (IOError): {e}")


print("\n--- Завдання 3: Пошук студента за прізвищем та запис у student_grade.txt ---")
try:
    search_surname = input("Введіть прізвище студента для пошуку: ").strip()
    found = False
    
    with open("student_grade.txt", "w", encoding="utf-8") as out_file:
        for student in students_data:
            if student["surname"].lower() == search_surname.lower():
                out_file.write(f"{student['surname']},{student['name']},{student['grade']}\n")
                print(f"Знайдено та записано у 'student_grade.txt': {student['surname']} {student['name']} — {student['grade']}")
                found = True
        
        if not found:
            print(f"Студента з прізвищем '{search_surname}' не знайдено.")
            out_file.write(f"Студента з прізвищем '{search_surname}' не знайдено.\n")

except IOError as e:
    print(f"Помилка запису у файл student_grade.txt: {e}")


print("\n--- Завдання 4: Пошук студента з найвищою оцінкою у введеному файлі ---")
try:
    filename = input("Введіть ім'я файлу для пошуку (наприклад, grades.txt): ").strip()
    if not filename:
        filename = "grades.txt"  # Значення за замовчуванням
        
    highest_grade = -1
    best_student = None
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(",")
            if len(parts) != 3:
                continue
            
            surname, name, grade_str = parts[0], parts[1], parts[2]
            grade = float(grade_str)
            
            if grade > highest_grade:
                highest_grade = grade
                best_student = {"surname": surname, "name": name, "grade": grade}
                
    if best_student:
        print(f"Студент з найвищою оцінкою у файлі '{filename}':")
        print(f"Прізвище: {best_student['surname']}, Ім'я: {best_student['name']}, Оцінка: {best_student['grade']}")
    else:
        print("У файлі не знайдено жодних коректних даних про студентів.")

except FileNotFoundError:
    print(f"Помилка: Файл '{filename}' не знайдено!")
except ValueError as e:
    print(f"Помилка формату даних у файлі (ValueError): {e}")
except IOError as e:
    print(f"Помилка вводу-виводу (IOError): {e}")