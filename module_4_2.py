def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()     #вложенная функция выполняется
inner_function()    #вложенная функция вне простанства имен функции test_function() не видна