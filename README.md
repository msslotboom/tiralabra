# Connect 4 minimax algorithm

[Week 1 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week1_report.md)

[Week 2 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week2_report.md)

[Week 3 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week3_report.md)

[Week 4 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week4_report.md)

[Week 5 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week5_report.md)

[Week 6 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week6_report.md)

[Project specification](https://github.com/msslotboom/tiralabra/blob/main/documentation/project_specification.md)


## How to use the program
Clone the project, then execute the following commands to install it:
```
poetry install --no-root
```
Now you can execute the program using the following command:
```
poetry run invoke start
```
This starts the game. The user plays as player 1, and the program calculates the moves for player 2. You select a column to play by entering a number between 0 and 6.

Addittionally, you can run the program in debug mode, which prints additional information:
```
poetry run invoke start-debug
```
You can run the tests using the command:
```
poetry run invoke test
```
And you can get the test coverage report using the command:
```
poetry run invoke coverage-report
```
This generates a html coverage report. You can read it by opening the generated file /project/htmlcov/index.html in your favourite web-browser.

The lint report can be seen with the command:
```
poetry run invoke lint
```
Auto-formatting is done using the command:
```
poetry run invoke format
```
