# Решение по анализу видеопотока транспорта от DataForce

DataForce представляет решение для анализа транспортного видеопотока. Алгоритм точно определяет категории транспорта, вычисляет средние скорости и легко интегрируется в системы комплексного анализа загрязнения воздуха. 

![alt text](https://github.com/Arctic-Data-Force/minpriroda/blob/e211271201f224cc44792bde1db03ee0aab8c5db/IMG_4507-2.gif)

## 🌐 Обзор решения

1. **Категоризация транспорта**: Видеозапись анализируется на предмет выделения транспортных средств различных категорий.

2. **Отслеживание объектов с реидентификацией**: Помимо обнаружения автотранспорта, объекты отслеживаются с использованием механизма реидентификации.

3. **Расчет скорости**: Общее количество проезжающих автотранспортных средств и средняя скорость для каждой категории.

4. **Структурированная информация**: Генерируется структурированная информация о движении транспорта и сохраняется в требуемом формате (csv).

## ⚙️ Технические характеристики

- **Python**: основной язык программирования для реализации решения.
- **RTDETR**: используется для точного обнаружения объектов.
- **ByteTrack с реидентификацией**: интегрирован для надежного отслеживания объектов с реидентификацией.
- **Roboflow Supervision**: применяется для эффективной аннотации и предварительной обработки данных.

## 🚀 Начало работы

Для начала использования решения по анализу видеопотока транспорта от DataForce, выполните следующие шаги:

1. **Склонируйте репозиторий:**
    ```bash
    git clone https://github.com/DataForce/minpriroda.git
    ```

2. **Загрузите модель .pt**

3. **Запустите pipeline с загруженной моделью:**

Важно: пути в ячейках нужно изменять индивидуально для каждого!

## ➕ Дополнительные источники данных


Для обеспечения высокой точности и разнообразия в обучении модели, были использованы следующие открытые источники данных:

- [Tram Dataset 1](https://universe.roboflow.com/cards-pgwnk/tram-5nu8e/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- [Tram Dataset 2](https://universe.roboflow.com/gdk-bd-muctr/tram-kshkj/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- [Trolleybus Dataset](https://universe.roboflow.com/cards-pgwnk/trolleybus/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- [Street View Dataset](https://universe.roboflow.com/fsmvu/street-view-gdogo/dataset/1)
- [Good Conditions Traffic](https://universe.roboflow.com/university-of-passau-germany/goodconditionstraffic/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- [Custom Dataset 1](https://universe.roboflow.com/bsuir-wmujb/asdfg-rmzhn)
- [Custom Dataset 2](https://universe.roboflow.com/my-projects-ons8w/object-tracking-and-detection-mkhw4/dataset/1)
- [Smart City Cars Detection](https://universe.roboflow.com/simone-bernabe/smart-city-cars-detection/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)


## 👥 Участники

- Васендина Ирина
- Голышев Алексей
- Громов Никита
- Калинин Илья
- Покрышкин Даниил
