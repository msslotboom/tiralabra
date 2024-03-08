## Testing
This is the test coverage of the project:
![Test Coverage](documentation/test-coverage.png "Test coverage of the project")

The most crucial testing happens in the tests written for the minimax file. The minimax function returns a move and the score of that move. Multiple scenarios are checked where a certain move should be played to prevent a loss and a certain move should be played to win immediately.
The heuristic file is tested on that it gives the correct heuristic and detects different types of sequences that should be detected and scored. The connect4 file is tested on that playing a move works and that wins are detected.

The tests can be run with the command:
```
poetry run invoke test
```
And the coverage report can be generated with the command:
```
poetry run invoke coverage-report
```
