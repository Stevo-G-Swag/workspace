# Agents

Agents is an AI-driven task management and execution system. It leverages agents with specific roles and goals to perform tasks, which can be analyzed, planned, executed, or delegated. The system is designed to simulate a workflow involving multiple agents working together to achieve a common goal. The project includes a context-aware workflow that executes a series of chains based on a given context. It also integrates with an external Language Model (LLM) service to generate text based on provided prompts.

## Overview

The application is structured around several core modules: agents, chains, examples, and LLM interface. The agents module handles agent management, including role assignment, task performance, and delegation. The chains module manages the definition and execution of task chains and context-aware workflows. The examples module provides sample usage scenarios. The LLM interface module handles interactions with the external Language Model service. The main entry point is in `main.py`, which initializes agents, assigns tasks, executes chains, and manages workflows. Flask is used as the web framework, and the project is configured to run on Replit with environment management handled by Nix. Dependencies are managed by Poetry.

### Project Structure

- **agents**: Contains classes for `Agent`, `Crew`, and `Task`.
- **chains**: Contains classes for `Chain` and `ContextAwareWorkflow`.
- **examples**: Provides example usage of the system.
- **llm_interface.py**: Contains the implementation for interacting with the external LLM service.
- **main.py**: Serves as the entry point for the application.
- **templates**: Contains HTML templates for the web interface.
- **static**: Contains CSS files for styling the web interface.

## Features

1. **Agent Management**:
    - **Role Assignment**: Assign specific roles and goals to agents, including backstories and tools.
    - **Task Performance**: Agents can analyze, plan, execute, or delegate tasks.
    - **Delegation**: Agents can delegate tasks to other agents if allowed.

2. **Task Management**:
    - **Task Definition**: Define tasks with descriptions, expected outputs, and responsible agents.
    - **Task Execution**: Execute tasks by the assigned agent and return the result.

3. **Crew Management**:
    - **Crew Initialization**: Initialize a crew with a list of agents.
    - **Task Assignment**: Assign tasks to the crew, which delegates them to appropriate agents.

4. **Chain Execution**:
    - **Chain Definition**: Define sequences of tasks (links) to be executed in order.
    - **Chain Execution**: Execute chains sequentially.

5. **Context-Aware Workflow**:
    - **Workflow Definition**: Define workflows based on a given context and a series of chains.
    - **Workflow Execution**: Execute chains in the provided context, ensuring tasks are performed in the correct order.

6. **LLM Integration**:
    - **LLM Interface**: Integrate with an external Language Model (LLM) service to generate text based on prompts.
    - **API Interaction**: Handle API calls to the LLM service, sending prompts and receiving generated text.

## Getting started

### Requirements

- **Python**: Programming language required to run the application.
- **Nix**: Package manager for environment management and reproducibility.
- **Flask**: Web framework for building the application.
- **requests**: Library for making HTTP requests to the LLM service.
- **Poetry**: Dependency management and packaging tool for Python.
- **OpenAI**: Library for interacting with the OpenAI API.

### Quickstart

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd agents
    ```

2. **Set up the environment**:
    Ensure you have Nix installed. Then, run:
    ```sh
    nix-shell
    ```

3. **Install dependencies**:
    To resolve the issue with dependency installation, follow these steps:
    - Update the lock file to ensure it matches the `pyproject.toml` file by running:
      ```sh
      poetry lock --no-update
      ```
    - Install the dependencies using the updated lock file:
      ```sh
      poetry install
      ```

4. **Set up the OpenAI API key**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. **Run the application**:
    ```sh
    poetry run python main.py
    ```

6. **Access the application**:
    Open your web browser and navigate to `http://localhost:8000`.

### License

The project is proprietary (not open source). Copyright (c) 2024.