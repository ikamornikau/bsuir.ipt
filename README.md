# Лабораторная работа 2

### Условие

1. Создать сериализатор
2. Создать консольную утилиту на основе сериализатора из п.1

- Код программы должен содержать фабричный метод `create_serializer()`, который будет порождать различные типы сериализаторов: `JSON`, `YAML`, `TOML`, `PICKLE`

- Каждый из сериализаторов должен реализовывать следующие методы:
  - dump(obj, fp) — сериализует Python объект в файл
  - dumps(obj) — сериализует Python объект в строку
  - load(fp) — десериализует Python объект из файла
  - loads(s) — десериализует Python объект из строки

- Режимы работы:
  - как библиотека, для переиспользования основной логики или
вспомогательных функций
  - как консольная утилита

- Задание конфигурации:
  - Возможность передачи всех конфигурационных параметров по отдельности через аргументы командной строки
  - Опциональный конфигурационный файл для конкретного запуска через аргументы командной строки