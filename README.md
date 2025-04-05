# Linked List App

## Description

This application implements a linked list data structure with various operations such as insertion, deletion, search,
and cloning. The list supports bidirectional traversal, allowing efficient manipulation of elements.

## Variant Calculation and Description

The variant number is calculated as follows:

```
9167 % 4 = 3
```

- first implementation - built-in list
- second implementation - doubly linked list

## How to Build and Run Tests

To set up the project and run the tests, follow these steps:

1. Clone the repository:
   ```sh
   git clone <https://github.com/vladosadchuk/mtsd-lab2>
   ```

2. Run project using:
   ```sh
   python main.py
   ```

3. Run unit tests using:
   ```sh
   python -m unittest
   ```

## CI Failure Commit Link

The commit where the tests failed on CI can be
found [69e22a0](https://github.com/vladosadchuk/mtsd-lab2/commit/69e22a0e14560ba0562c08fad7edb26ca5d53ccd).

## Conclusions

Юніт-тестування виявилося надзвичайно корисним інструментом у процесі розробки. Воно допомогло виявити та виправити
помилки на ранніх етапах, забезпечуючи коректну роботу окремих компонентів ще до їх інтеграції в загальну систему.
Автоматизоване тестування в CI/CD дозволило швидко отримувати зворотний зв’язок щодо змін у коді, зменшуючи ризик
виникнення регресій. Хоча написання тестів вимагає додаткових зусиль, їх довгострокові переваги, такі як підвищення
надійності, підтримуваності коду та спрощення процесу налагодження, роблять їх цілком виправданими.

