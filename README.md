# Connect 4 minimax algorithm

[Week 1 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week1_report.md)

[Week 2 report](https://github.com/msslotboom/tiralabra/blob/main/documentation/week2_report.md)

[Project specification](https://github.com/msslotboom/tiralabra/blob/main/documentation/project_specification.md)


## How to use the program
Clone the project, then execute the following commands to install it:
```
cd project
poetry install --no-root
```
Now you can execute the program using the following command:
```
poetry run invoke start
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
