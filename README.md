# django_course

Дипломный проект Django
Создать простую торговую площадку. Сайт, имеющий возможность выставлять что-то на продажу
Каждый юзер может выставлять товары на продажу и покупать их.
У юзера есть счет, баланс которого меняется, в зависимости о того, покупает или продает юзер
товар. и покупать для зарегистрированных юзеров.
После регистрации каждый новый юзер автоматически получает 100 кредитов на баланс.
У каждого юзера есть корзина – он может добавить туда товар, и в любой момент зайти в свою
корзину чтоб увидеть ее состояние.
Кроме того на каждой странице юзер видит сумму, на которую он набрал товаров в корзину
Заказ выглядит так:
- Юзер набирает товар в корзину, используя кнопку «добавить в корзину».
- В корзине есть кнопка «Оплатить», нажав на которую происходит списание со счета покупателя,
которые зачисляются на баланс владельца товара.
- Затем юзер получает сообщение об успешной оплате заказа (самый просто вариант –
реализация через перенаправление на отдельную страницу, так же можно реализовать отправку
на почту)
Оплата происходит путем списания денег со счета одного юзера и переводом их на счет юзера,
владеющего товаром.
На главной странице отображены все выставленные пользователями товары и меню выбора
категорий.
Так же есть страницы категории.
Каждый товар имеет свою страницу с информацией о нем и кнопкой «Добавить в корзину».

Юзер имеет атрибуты:
-почта
-имя
-аватарка
-статус (продавец или покупатель).
-счет.

Товар имеет атрибуты:
-юзера-владельца
-имя
-слаг-описание
-цена
-категория
-изображение

Категория имеет атрибуты:
Добавляется только суперюзером (админом).
Имеет:
- имя
- слаг
