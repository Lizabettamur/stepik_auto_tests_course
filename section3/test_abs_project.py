#def test_abs1():
#    assert abs(-42) == 42, "Should be absolute value of a number" 

#if __name__ == "__main__":
#    test_abs1()
#    print("All tests passed!")



#Если нам нужно добавить еще один тест, мы можем написать его как функцию в этом же файле. 
#В приведенном примере мы уже не увидим сообщение "Everything passed", 
#так как падение любого теста вызывает выход из программы:

#def test_abs1():
#    assert abs(-42) == 42, "Should be absolute value of a number"

#def test_abs2():
#    assert abs(-42) == -42, "Should be absolute value of a number"

#if __name__ == "__main__":
#    test_abs1()
#    test_abs2()
#    print("Everything passed")


#===============================================================================================================================================================

#теперь изменим наши предыдущие тесты, чтобы их можно было запустить с помощью unittest. Для этого нам понадобится выполнить следующие шаги:

#1. Импортировать unittest в файл: **import unittest**
#2. Создать класс, который должен наследоваться от класса TestCase: **class TestAbs(unittest.TestCase):**
#3. Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: **def test_abs1(self):**
#4. Изменить assert на **self.assertEqual()**
#5. Заменить строку запуска программы на **unittest.main()**

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()




    
    