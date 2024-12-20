### Таблиця 1: Для інженера-будівельника
|Назва пункту                     |Опис                                                    |
|---------------------------------|--------------------------------------------------------|
|Ідентифікатор та назва           |Моніторинг стану обладнання                             |
|Основна та додаткова дійові особи|Основна: Інженер-будівельник<br>Додаткова: Менеджер проєкту|  
|Опис|Інженер використовує веб-додаток для моніторингу стану обладнання та отримання попереджень про потенційні несправності.|
|Тригер|Регулярна перевірка або отримання сповіщення від системи про несправність.|
|Попередні умови|Датчики IoT встановлені на обладнанні.<br>Інженер має доступ до системи моніторингу.|
|Нормальний напрямок подій|1.Інженер входить у систему.<br>2.Відкриває панель моніторингу.<br>3.Аналізує дані про стан обладнання (температура, вібрації, інші показники).<br>4.Отримує рекомендації від AI щодо необхідних дій.<br>5.Вживає заходів, щоб уникнути аварій.|
|Альтернативний напрямок подій|Якщо дані не оновлюються, інженер перевіряє роботу IoT-пристроїв.|
|Винятки|Система не отримує дані через збій в IoT-пристрої.|
|Бізнес правила|1.Попередження про критичні несправності мають надсилатися в реальному часі.<br>2.Лог кожного попередження зберігається для подальшого аналізу.|
-----
### (Альтернативний варіант): Для інженера-будівельника
|Назва пункту                     |Опис                                                    |
|---------------------------------|--------------------------------------------------------|
|Ідентифікатор та назва           |Виявлення несправностей через аварійне повідомлення                             |
|Основна та додаткова дійові особи|Основна: Інженер-будівельник<br>Додаткова: Менеджер проєкту|  
|Опис|Система автоматично генерує сповіщення про аварійну ситуацію, інженер оперативно реагує.|
|Тригер|Датчик IoT зафіксував критичне значення параметра (наприклад, надмірну вібрацію).|
|Попередні умови|IoT-пристрої справно працюють.<br>Увімкнено систему оповіщень у веб-додатку.|
|Нормальний напрямок подій|1.Інженер отримує сповіщення про несправність.<br>2.Відкриває додаток і переглядає критичні параметри.<br>3.Викликає обслуговуючу команду для ремонту або вимикає обладнання.|
|Альтернативний напрямок подій|Якщо інженер не реагує, сповіщення надсилається менеджеру проєкту.|
|Винятки|Сповіщення не було доставлено через технічний збій.|
|Бізнес правила|1.Сповіщення повинно надсилатися основному користувачеві (інженеру) та дублюватися на резервного користувача (менеджера) через 5 хвилин, якщо не отримано підтвердження про прочитання.<br>2.Система повинна мати журнал дій, де фіксується кожне аварійне сповіщення та час його обробки.|
----
### Таблиця 2: Для менеджера проекту
|Назва пункту                     |Опис                                                    |
|---------------------------------|--------------------------------------------------------|
|Ідентифікатор та назва           |Аналіз даних про безпеку будівельного майданчика                             |
|Основна та додаткова дійові особи|Основна: Менеджер проєкту<br>Додаткова: Адміністрація|  
|Опис|Менеджер переглядає зведену інформацію про безпеку на будівельному майданчику та використовує аналітичні інструменти для запобігання аваріям.|
|Тригер|Кінцевий термін щоденного звіту або аварійне сповіщення.|
|Попередні умови|Дані зібрані IoT-пристроями та оброблені системою.<br>Менеджер має доступ до аналітичних модулів.|
|Нормальний напрямок подій|1.Менеджер входить у систему.<br>2.Обирає вкладку "Аналітика безпеки".<br>3.Переглядає графіки, статистику та рекомендації від AI.<br>4.Формує план дій на основі отриманих даних.|
|Альтернативний напрямок подій|Якщо аналітичні дані відсутні, менеджер повідомляє адміністрацію про технічну проблему|
|Винятки|Помилкові дані через збій у системі збору IoT.|
|Бізнес правила|1.Щоденні звіти мають формуватися автоматично.<br>2.Дані зберігаються протягом 5 років для аудиту.|
----
### (Альтернативний варіант): Для менеджера проекту
|Назва пункту                     |Опис                                                    |
|---------------------------------|--------------------------------------------------------|
|Ідентифікатор та назва           |Формування звіту про несправність за запитом                             |
|Основна та додаткова дійові особи|Основна:  Менеджер проєкту<br>Додаткова: Адміністрація|  
|Опис|Менеджер формує звіт про небезпеки за конкретним критерієм (наприклад, період або тип несправності).|
|Тригер|Запит адміністрації про звіт у нестандартному форматі.|
|Попередні умови|Система зберігає історію даних.<br>Доступ до модулю ручного формування звітів.|
|Нормальний напрямок подій|1.Менеджер входить у систему.<br>2.Переходить до модуля "Ручне формування звіту".<br>3.Задає параметри (певний період, місце чи обладнання).<br>4.Генерує та надає звіт адміністрації.|
|Альтернативний напрямок подій|Якщо дані за запитом відсутні, менеджер формує звіт вручну, використовуючи локальні архіви.|
|Винятки|Збій у модулі звітності або пошкодження даних.|
|Бізнес правила|1.Усі звіти повинні зберігатися у базі даних протягом мінімум 1 року для забезпечення відповідності регуляторним нормам.<br>2.Запити на звіти повинні автоматично перевірятися на наявність критичних даних і, за необхідності, генерувати сповіщення для відповідальних осіб.|
----
### Таблиця 3: Для адміністрації
|Назва пункту                     |Опис                                                    |
|---------------------------------|--------------------------------------------------------|
|Ідентифікатор та назва           |Отримання стратегічного звіту для компанії                             |
|Основна та додаткова дійові особи|Основна: Адміністрація<br>Додаткова: Менеджер проєкту|  
|Опис|Адміністрація переглядає стратегічні звіти, які генерує система, для аналізу ефективності та безпеки на будівельних майданчиках.|
|Тригер|Кінцевий термін щомісячного або квартального звіту.|
|Попередні умови|Всі IoT-пристрої та аналітичні модулі працюють коректно.<br>Адміністрація має права доступу до звітів.|
|Нормальний напрямок подій|1.Адміністрація входить у систему.<br>2.Обирає вкладку "Стратегічні звіти".<br>3.Переглядає інтерактивний звіт про всі будівельні майданчики.<br>4.Використовує звіт для прийняття управлінських рішень.|
|Альтернативний напрямок подій|Якщо звіт не формується, адміністрація звертається до менеджера проєкту для перевірки даних.|
|Винятки|Неповні дані через проблеми на стороні IoT-пристроїв.|
|Бізнес правила|1.Звіти повинні включати показники ефективності роботи та рівень безпеки.<br>2.Стратегічний звіт формується з можливістю експорту у формат PDF.|
----
### (Альтернативний варіант): Для адміністрації
|Назва пункту                     |Опис                                                    |
|---------------------------------|--------------------------------------------------------|
|Ідентифікатор та назва           |Отримання звіту через мобільний додаток                            |
|Основна та додаткова дійові особи|Основна: Адміністрація<br>Додаткова: Менеджер проєкту|  
|Опис|Адміністрація використовує мобільний додаток для перегляду звіту без доступу до основної системи.|
|Тригер|Терміновий запит адміністрації на отримання звіту під час відсутності на робочому місці.|
|Попередні умови|Мобільний додаток інтегровано з веб-додатком.<br>Адміністрація має авторизований доступ.|
|Нормальний напрямок подій|1.Адміністрація відкриває мобільний додаток.<br>2.Вибирає потрібний звіт із меню.<br>3.Переглядає інформацію у зручному форматі.|
|Альтернативний напрямок подій|Якщо мобільний додаток не має необхідного звіту, адміністрація запитує звіт через менеджера.|
|Винятки|Відсутній інтернет-зв’язок для доступу до системи.|
|Бізнес правила|1.Усі дані в мобільному додатку повинні бути синхронізовані з основною системою не рідше, ніж раз на 15 хвилин.<br>2.Якщо доступ до потрібного звіту неможливий, мобільний додаток повинен автоматично надсилати запит на сервер і сповіщати адміністрацію про орієнтовний час підготовки звіту.|
---
