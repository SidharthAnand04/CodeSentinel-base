# CodeSentinel

CodeSentinel is a dynamic server application designed to monitor changes in a specified GitHub repository, feed those changes into a Language Learning Model (LLM), generate a bug log based on the commits, and then commit this log back to the repository. The application also includes a web dashboard built with Flask to display commit information, LLM responses, and an embedded view of the GitHub repository.

[Demonstration Repo](https://github.com/SidharthAnand04/CodeSentinel/tree/main)

## Features

- **Automatic Repository Monitoring**: Periodically checks the specified GitHub repository for new commits.
- **Commit Information Collection**: Gathers and displays details about each commit, including the author, date, and changed files.
- **LLM Integration**: Sends commit information to an LLM for analysis and generates a response.
- **Automated Logging**: Commits the LLM response as a new log back to the repository.
- **Web Dashboard**: A user-friendly dashboard to view commit information, LLM responses, and the GitHub repository.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- `pip` package manager.
- Git installed on your machine.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SidharthAnand04/CodeSentinel-base.git
   cd CodeSentinel-base
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Repository URL**:
   Update the `REPO_URL` in `app.py` to point to your target GitHub repository:
   ```python
   REPO_URL = 'https://github.com/SidharthAnand04/CodeSentinel.git'
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

Once the application is running, it will:

1. Clone the specified repository (if not already cloned).
2. Periodically check for new commits.
3. Collect and display commit information.
4. Generate a response from the LLM and commit it back to the repository.
5. Provide a web dashboard to view the commit information, LLM responses, and the embedded GitHub repository.

### Web Dashboard

Access the web dashboard by navigating to `http://127.0.0.1:5000` in your web browser. The dashboard includes:

- **Commit Information**: Detailed information about each commit.
- **LLM Response**: The response generated by the LLM based on the commit information.
- **GitHub Repository**: An embedded view of the GitHub repository.

### File Structure

```
CodeSentinel/
│
├── templates/
│   └── index.html         # HTML template for the dashboard
│
├── static/
│   └── styles.css         # CSS for styling the dashboard
│
├── app.py                 # Main application script
├── prompt.txt             # Prompt template for the LLM
└── commit_info.txt        # Temporary file for storing commit information
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out:

- **Sidharth Anand**: [LinkedIn](https://www.linkedin.com/in/anand-sidharth/)
