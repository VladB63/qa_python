from main import BooksCollector

import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    # проверка метода добавления книги add_new_book
    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_books(self, book):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book(book)
        # проверяем что книга действительно добавилась
        assert book in collector.books_genre
        # проверяем что жанр у книги пустой
        assert collector.books_genre[book] == ''

    # проверка метода добавления нескольких книг add_new_book, данные не затираются
    def test_add_new_book_add_2_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем что кол-во элементов теперь 2
        assert len(collector.books_genre) == 2



    # проверка метода установки книге жанра по имени set_book_genre
    @pytest.mark.parametrize('book, genre', [
        ('Человек амфибия','Фантастика'),
        ('12 стульев', 'Комедии'),
        ('Трое в лодке, не считая собаки', 'Комедии')])
    def test_set_book_genre_set_genre(self, book, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book(book)
        # добавленной книге присваиваем жанр
        collector.set_book_genre(book, genre)
        # проверяем условие метода - действительно ли есть такая книга в словаре books_genre
        # и входит ли в список genre присвоенный жанр
        assert collector.books_genre[book] == genre



    # проверка метода получения жанра по имени книги get_book_genre
    @pytest.mark.parametrize('book, genre', [
        ('Человек амфибия', 'Фантастика'),
        ('12 стульев', 'Комедии'),
        ('Трое в лодке, не считая собаки', 'Комедии')])
    def test_get_book_genre_by_name(self, book, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book(book)
        # добавленной книге присваиваем жанр
        collector.books_genre[book] = genre
        # запрашиваем жанр по имени книги
        collector.get_book_genre(book)
        # проверяем соответствие жанра заданному книге
        assert collector.get_book_genre(book) == genre



    # проверка метода вывода списка книг по заданному жанру get_books_with_specific_genre
    def test_get_books_with_specific_genre_by_genre_from_the_list(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Человек амфибия')
        collector.add_new_book('12 стульев')
        collector.add_new_book('Трое в лодке, не считая собаки')
        # добавленным книгам присваиваем жанр
        collector.set_book_genre('Человек амфибия', 'Фантастика')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.set_book_genre('Трое в лодке, не считая собаки', 'Комедии')
        # задаем отбор
        collector.get_books_with_specific_genre('Комедии')
        # проверяем выдачу по заданному жанру. в assert я сравниваю список с запросом
        # в той же очередности, что и создавал, я это понимаю
        assert ['12 стульев', 'Трое в лодке, не считая собаки'] == collector.get_books_with_specific_genre('Комедии')



    # проверка метода получения словаря get_books_genre
    # что возвращаются действительно данные с типом словарь
    def test_get_books_genre_by_data_type(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # заполняем словарь book_genre данными
        collector.add_new_book('Человек амфибия')
        collector.add_new_book('12 стульев')
        collector.add_new_book('Трое в лодке, не считая собаки')
        # присвоим жанр для удобства
        collector.set_book_genre('Человек амфибия', 'Фантастика')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.set_book_genre('Трое в лодке, не считая собаки', 'Комедии')
        collector.get_books_genre()
        # проверка типа возвращенных данных
        assert type(collector.get_books_genre()) is dict



    # проверка метода возврата книг для детей get_books_for_children
    def test_get_books_for_children_by_age_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Человек амфибия')
        collector.add_new_book('12 стульев')
        collector.add_new_book('Мизери')
        collector.add_new_book('Сияние')
        collector.add_new_book('Среди восковых фигур')
        # добавленным книгам присваиваем жанр
        collector.set_book_genre('Человек амфибия', 'Фантастика')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.set_book_genre('Мизери', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Среди восковых фигур', 'Детективы')
        collector.get_books_for_children()
        # проверка результата - соответствует ли выдача тому что было добавлено
        assert ['Человек амфибия', '12 стульев'] == collector.get_books_for_children()



    # проверка метода добавления книги в избранное add_book_in_favorites
    def test_add_book_in_favorites_book_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Человек амфибия')
        collector.add_new_book('12 стульев')
        # добавляем книги в избранное
        collector.add_book_in_favorites('Человек амфибия')
        collector.add_book_in_favorites('12 стульев')
        # проверка результата - соответствует ли выдача тому что было добавлено
        assert ['Человек амфибия', '12 стульев'] == collector.favorites



    # проверка метода удаления книги из избранного delete_book_from_favorites
    def test_delete_book_from_favorites_book_del(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Человек амфибия')
        collector.add_new_book('12 стульев')
        # добавляем книги в избранное
        collector.add_book_in_favorites('Человек амфибия')
        collector.add_book_in_favorites('12 стульев')
        # вызываем метод удаления книги из избранного
        collector.delete_book_from_favorites('Человек амфибия')
        # проверка результата удаления
        assert 'Человек амфибия' not in collector.favorites



    # проверка метода получения списка избранных книг get_list_of_favorites_books
    def test_get_list_of_favorites_books_success(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Человек амфибия')
        collector.add_new_book('12 стульев')
        # добавляем книги в избранное
        collector.add_book_in_favorites('Человек амфибия')
        collector.add_book_in_favorites('12 стульев')
        # вызываем метод удаления книги из избранного
        collector.get_list_of_favorites_books()
        # проверка результата запроса выдачи
        assert ['Человек амфибия', '12 стульев'] == collector.favorites

