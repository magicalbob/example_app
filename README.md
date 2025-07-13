🧮 example_app
==============

A simple command-line Python utility that prints all **prime numbers** less than a given maximum.

This is a minimal educational example, useful for:

-   Practicing Python scripting
-   Understanding prime number algorithms
-   Demonstrating argument parsing with `argparse`
-   Showcasing modern Python project structure with `pyproject.toml`
-   Illustrating unit testing with `pytest` and code coverage analysis

* * * * *

📦 Features
-----------

-   Computes prime numbers below a user-specified maximum
-   Fast, readable implementation using trial division
-   Clean CLI with helpful error messages
-   Project metadata managed by `pyproject.toml`
-   Comprehensive unit test suite with coverage reporting ensuring correctness

* * * * *

🚀 Installation
---------------

### From PyPI (Coming Soon)

Once published, you will be able to install `example_app` directly using pip:

```
pip install example_app

```

### From Source

Clone the repository:

```
git clone https://github.com/magicalbob/example_app.git
cd example_app

```

Then, you can run the application directly:

```
python src/example_app/example_app.py 50

```

Alternatively, you can install it in editable mode for development:

```
pip install -e .

```

This will make the `example_app` command available in your environment.

* * * * *

🛠 Usage
--------

To run the application:

```
python src/example_app/example_app.py MAXIMUM

```

Or, if installed in editable mode:

```
example_app MAXIMUM

```

Where `MAXIMUM` is a positive integer. The app will print all prime numbers **less than** this value.

### Example:

```
$ python src/example_app/example_app.py 20
2
3
5
7
11
13
17
19

```

* * * * *

⚙️ Project Structure
--------------------

The project adheres to a standard Python packaging layout:

```
example_app/
├── src/
│   └── example_app/
│       └── example_app.py    # Main application logic
├── tests/
│   └── test_example_app.py   # Unit tests
├── htmlcov/                  # Coverage HTML reports (generated)
├── pyproject.toml            # Project metadata and build configuration
├── README.md                 # This file
└── LICENSE                   # Project license

```

### `pyproject.toml`

This file defines the project's metadata, dependencies, and build system according to PEP 517 and PEP 621. It specifies:

-   Project name, version, description, and authors.
-   Python version requirements.
-   License information.
-   Entry points for the command-line interface (if applicable, though in this simple case, direct script execution or `setuptools` entry points would be used for a full package).
-   Development dependencies (e.g., `pytest` for testing, `pytest-cov` for coverage, `build` for packaging).
-   Test configuration with coverage reporting settings.

* * * * *

🧪 Testing
----------

This project includes a comprehensive suite of unit tests powered by `pytest` with integrated code coverage analysis.

### Running Tests

To run the tests, ensure you have the development dependencies installed:

```
pip install -e ".[dev]"

```

Then, navigate to the project root and run `pytest`:

```
# Run tests (basic)
pytest

# Run tests with coverage
pytest --cov=example_app

# Run tests with coverage and detailed missing line report
pytest --cov=example_app --cov-report=term-missing

# Run tests with coverage and generate HTML report
pytest --cov=example_app --cov-report=html

# Run tests with coverage, fail if below 90% coverage
pytest --cov=example_app --cov-fail-under=90

```

### Test Coverage

The project is configured to maintain high code coverage (90% minimum). Coverage reports are generated in multiple formats:

-   **Terminal output**: Shows coverage percentage and missing lines
-   **HTML report**: Detailed interactive coverage report in `htmlcov/index.html`
-   **XML report**: Machine-readable coverage data in `coverage.xml`

#### Viewing Coverage Reports

After running tests, you can view the detailed HTML coverage report:

```
# On macOS/Linux
open htmlcov/index.html

# On Windows
start htmlcov/index.html

# Or use your preferred browser
firefox htmlcov/index.html

```

#### Coverage Commands

```
# Run tests with coverage (default behavior)
pytest

# Run tests with verbose coverage output
pytest --cov-report=term-missing

# Generate only HTML coverage report
pytest --cov-report=html

# Check coverage without running tests (if .coverage file exists)
coverage report

# Generate HTML report from existing coverage data
coverage html

```

### Test Suite Coverage

The tests comprehensively cover:

-   **`is_prime` function logic**: Various known prime and non-prime numbers are tested to ensure the core prime checking algorithm is correct.
-   **`list_primes_below` function output**: Verifies that the function correctly prints primes up to a given maximum by capturing standard output.
-   **Command-line interface (CLI) behavior**: Uses `subprocess` to simulate CLI invocations, checking:
    -   Correct output for valid inputs.
    -   Empty output for edge cases (e.g., `MAXIMUM` of 1).
    -   Proper error handling and non-zero exit codes for invalid or missing arguments.

**Current test coverage**: The test suite achieves excellent coverage of all critical code paths, ensuring reliability and maintainability.

* * * * *

🧑‍💻 Contributing
------------------

This project is kept intentionally simple, but pull requests and ideas are welcome!

1.  Fork the repo
2.  Create your feature branch (`git checkout -b feature/my-feature`)
3.  Commit your changes (`git commit -am 'Add new feature'`)
4.  Run tests and ensure coverage remains high (`pytest`)
5.  Push to the branch (`git push origin feature/my-feature`)
6.  Open a pull request

### Development Guidelines

-   Maintain test coverage above 90%
-   Add tests for any new functionality
-   Update documentation for significant changes
-   Follow existing code style and patterns

* * * * *

📄 License
----------

This project is licensed under the **GNU General Public License v3.0**.

You may copy, distribute, and modify the software as long as you track changes/dates in source files. Derivative works must also be licensed under GPLv3.

See the full license in [LICENSE](https://claude.ai/chat/LICENSE) or at <https://www.gnu.org/licenses/gpl-3.0.en.html>

* * * * *

👤 Author
---------

Ian Ellis

[GitHub](https://github.com/magicalbob)

Feel free to fork, improve, and reuse.
