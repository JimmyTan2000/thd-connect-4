# Software Engineering Project - KI4, TH Deggendorf

## Description

This is the source code repository of the KI (Küstliche Intelligenz) project for the course "Software Engineering", 4. Semester, TH Deggendorf.
The goal of this project is to create a simple ["Connect 4"](https://en.wikipedia.org/wiki/Connect_Four) game console application running inside a docker container managed by docker compose.
The application is going to be started with docker-compose running the python app in an interactive manner.

## Requirements

- To run this project [docker and docker-compose](https://www.docker.com/) needs to be installed
- [GNU Make](https://www.gnu.org/software/make/) is optional but highly advised

## Run software

1. If [GNU Make](https://www.gnu.org/software/make/) is installed just invoke `make` from the command line and the project will be automatically tested, build and run in interactive mode. Make sure your current working directory contains the **Makefile** (found at project root).
1. To manually build and run docker-compose issue following commands

```
docker-compose build
docker-compose run --rm connect-four
```

## Development

For development additional commands are availabe in the _Makefile_. **Note that after each command the container that ran will be deleted!**

1. `make` or `make prod` : build, test and run the production container
1. `make prod-tty` : drop into a bash shell for the production container
1. `make build-prod` : build and test the production container

The specific commands can be extracted from the _Makefile_.

## Testing

For unit testing the application the [python unittest framework](https://docs.python.org/3/library/unittest.html) is being used. To run the tests the following commands need to be issued from the project root directory. There are 3 different ways to run these:

1. If [Visual Studio Code](https://code.visualstudio.com/) is being used as the editor of choice navigate to the **Testing** tab and click the "Run Tests" (⯮) button.
1. If [GNU Make](https://www.gnu.org/software/make/) is installed run the command `make unittest`
1. To run the tests directly with [python](https://www.python.org/) issue the command `python -m unittest`

## Members

- Daniel Stoffel
- Wen Bin Bu
- Jimmy Tan
- Zi Xun Tan
- Mahmoud Mansour
