python-commerceml
=================

Обмен между 1с и сайтом

Установка
-------------

``pip install python-commerceml``

* django

    добавить приложение ``commerceml.contrib.django.cml`` в INSTALLED_APPS

    добавить пути в общий urls

        (r'^1c/', include('commerceml.contrib.django.urls')),

Настройки django
-----------------

`CML_FILE_LIMIT`
`CML_USE_ZIP` - Пока не работает
`CML_IMPORT_FOLDER` - опционально, куда загуржать XML с товарами и заказами.

`CML_MODELS_APP` - модуль с моделями данных или указывать каждую модель отдельно:
`CML_PRODUCT`
`CML_PRODUCT_PROPERTY`
`CML_CATEGORY`
`CML_MANUFACTURER`
`CML_IMAGE`
`CML_ORDER`
`CML_ORDER_ITEM`




TODO
-----------------

* Написать документацию
* Написать тесты
* django. USE_ZIP == True
* django. FILE_LIMIT > 0
* django. импорт и экспорт заказов
* django. экспорт каталога
* django. basic auth
