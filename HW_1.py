
# Создать переменную типа String
var_string = "Hello World"
# Создать переменную типа Integer
var_int = 29
# Создать переменную типа float
var_float = 3.56
# Создать переменную типа Bytes
var_bytes = b"Hello"
# Создать переменную типа List
var_list = [10, 20, 30]
# Создать переменную типа Tuple
var_tulpe = (10, 20, 30)
# Создать переменную типа Set
var_set = {10, 20, 30, 40}
# Создать переменную типа Frozen set
var_frozenset = frozenset(var_set)
# Создать переменную типа Dict
var_dict = {'10': 10, '20': 20, '30':30}

# Вывести у консоль все выше перечисленные переменные с добавлением типа данных
print(var_string, type(var_string))
print(var_int, type(var_int))
print(var_float, type(var_float))
print(var_bytes, type(var_bytes))
print(var_list, type(var_list))
print(var_tulpe, type(var_tulpe))
print(var_set, type(var_set))
print(var_frozenset, type(var_frozenset))
print(var_dict, type(var_dict))

# Cоздать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль
first_word = "Happy"
second_word = "day"
const_word = first_word + second_word
print (const_word)

# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print (var_string,',', var_int)

# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print (var_string,'+', var_int)