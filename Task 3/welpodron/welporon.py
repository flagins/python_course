'''

Пример выполненого задания, рекомендуется к ознакомлению

'''

# - однострочный комментарий 

'''

Пример многострочного комментария

'''

"""

Аналогичен предыдущему примеру многострочного комментария

"""

number_example = 1
print(number_example, type(number_example)) # 1 <class 'int'>

string_example = 'some text' # Аналогично string_example = "some text" (можно использовать любые из кавычек '' или "")
print(string_example, type(string_example)) # some text <class 'str'>

array_or_list_example = ["hello, i'm string inside list", 'this is me, second string inside list', number_example]

""" 

Обратите внимание на строку "hello, i'm string inside list", если бы мы написали:
'hello, i'm string inside list' (попытка написать кавычки внутри кавычек) python вызвал бы ошибку, из-за спецсимвола ' 
те он бы подумал, что вы закрыли строку уже здесь 'hello, i', при этом: m string inside list'
вызвало бы исключение (ошибку) тк python не понял бы что такое m string inside list 
подробнее о том как включать строку в строку, будет рассмотрено в следующих занятиях

"""

print(array_or_list_example, type(array_or_list_example)) # ["hello, i'm string inside list", 'this is me, second string inside list', 1] <class 'list'>

dictionary_example = { 
    'key1' : number_example,
    'key2' : string_example,
    'key3' : array_or_list_example,
    number_example : number_example,
    number_example + 1 : 'magic is here',
    3 : {}
} 

'''

Аналогично: dictionary = {'key1' : integer, 'key2' : string, 'key3' : array_or_list и так далее} 

(к слову тоже самое мы могли бы и сделать со списоком(листом, массивом)) те записать так:

    array_or_list_example = [
        "hello, i'm string inside list",
        'this is me, second string inside list',
        number_example
    ]


те можно писать в одну строку, а можно раскрыть скобки, главное чтобы ключи и их значения
находились внутри скобок 

Обратите внимание как интересно могут работать словари: 

    number_example : number_example,
    number_example + 1 : 'magic is here',
    3 : {}

Достаточно распространённая практика использовать другие переменные, созданные раньше, как ключи в словаре

'''

print(dictionary_example, type(dictionary_example)) # {'key1': 1, 'key2': 'some text', 'key3': ["hello, i'm string inside list", 'this is me, second string inside list', 1], 1: 1, 2: 'magic is here', 3: {}} <class 'dict'>

number_example += 1 #Аналогично: number_example = number_example + 1 

'''

(отсутствует Неявная операция инкремента как в C++), те: 
    C++: 
        number_example++ //Аналогично number_example += 1
    Python:
        number_example++ #Приводит к ошибке, используйте number_example += 1 

'''

print(number_example) # 2

print(array_or_list_example) # Обратите внимание что после изменения значения number_example лист и словарь не изменились
print(dictionary_example) 

string_example += str(number_example) #Аналогично: string_example = string_example + str(number_example)
print(string_example) # string2