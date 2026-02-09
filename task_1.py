# Строка содержит пять временных значений. Они записаны через запятую:
#'1h 45m,360s,25m,30m 120s,2h 60s'.
# Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы split(), replace() и оператор in.
# Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. Значения расшифровываются так:
#   часы — любое положительное целое число и символ h;
#   минуты — любое положительное целое число и символ m;
#   секунды — положительное целое число кратное 60 и символ s.


time = "1h 45m,360s,25m,30m 120s,2h 60s"
time1 = time.replace(",", " ")
time2 = time1.split()
total_minutes = 0
for vremya in time2:
    #  часы
    if "h" in vremya:
        hours = int(vremya.replace("h", ""))
        total_minutes += hours * 60
    #  минуты
    elif "m" in vremya:
        minutes = int(vremya.replace("m", ""))
        total_minutes += minutes
    #  секунды
    elif "s" in vremya:
        seconds = int(vremya.replace("s", ""))
        total_minutes += seconds // 60
print(total_minutes, "минут")
