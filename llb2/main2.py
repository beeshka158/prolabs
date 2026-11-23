def vibration_diagnostic(vibe_data):
     #Функция классифицирует замеры виброскорости.
     #vibe_data: список чисел (замеры)
     if not vibe_data: # Проверка на пустой список
         return 0.0

     avaria_count = 0 # Счетчик аварий

     for v in vibe_data:
         # Классификация по условию
         if v < 2.8:
              status = "Замечательно"
         elif 2.8 <= v < 7.1:
              status = "Допустимо"
         else: # v >= 7.1
              status = "Авария"
              avaria_count += 1

         # Вывод результата для каждого замера
         print(f"Замер {v} мм/с: {status}")

     # Расчет процента аварий
     percent = (avaria_count / len(vibe_data)) * 100
     return percent

#Тестирование программы
test_measurements = [1.5, 3.2, 8.0, 5.5, 7.5, 2.0, 9.1]
print(" Результаты диагностики")
result = vibration_diagnostic(test_measurements)
print(f"\nПроцент аварийных замеров: {result:.1f}%")
