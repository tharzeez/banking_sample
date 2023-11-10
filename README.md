# Banking app

## Overview
This application simulates a basic banking system. It is built following Clean Architecture principles



### Prerequisites
- Python 3.0 or higher

### To run the application
```
python main.py
```

### Structure
The application is organized as follows:
```
src/
├── adapter/                 # Contains the repositories for persistence
├── application/             # Contains the abstract classes for the repositories,
                               so that in future the underlying data models can be replaced 
├── config/                  # Centralized configuration and application context. 
├── domain/                  # Contains the entities of the project
├── use_cases/               # Application use cases encapsulating business rules.
└── main.py                  # Entry point for the application flow.
```