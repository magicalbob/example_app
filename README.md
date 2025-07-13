# 🧮 example_app

A simple command-line Python utility that prints all **prime numbers** less than a given maximum.

This is a minimal educational example, useful for:
- Practicing Python scripting
- Understanding prime number algorithms
- Demonstrating argument parsing with `argparse`
- Showcasing modern Python project structure with `pyproject.toml`
- Illustrating unit testing with `pytest`

---

## 📦 Features

- Computes prime numbers below a user-specified maximum
- Fast, readable implementation using trial division
- Clean CLI with helpful error messages
- Project metadata managed by `pyproject.toml`
- Comprehensive unit test suite ensuring correctness

---

## 🚀 Installation

### From PyPI (Coming Soon)

Once published, you will be able to install `example_app` directly using pip:

```bash
pip install example_app

```

### From Source

Clone the repository:

Bash

```
git clone [https://github.com/magicalbob/example_app.git](https://github.com/magicalbob/example_app.git)
cd example_app

```

Then, you can run the application directly:

Bash

```
python src/example_app/example_app.py 50

```

Alternatively, you can install it in editable mode for development:

Bash

```
pip install -e .

```

This will make the `example_app` command available in your environment.

----------

## 🛠 Usage

To run the application:

Bash

```
python src/example_app/example_app.py MAXIMUM

```

Or, if installed in editable mode:

Bash

```
example_app MAXIMUM

```

Where `MAXIMUM` is a positive integer. The app will print all prime numbers **less than** this value.

### Example:

Bash

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

----------

## ⚙️ Project Structure

The project adheres to a standard Python packaging layout:

```
example_app/
├── src/
│   └── example_app/
│       └── example_app.py    # Main application logic
├── tests/
│   └── test_example_app.py   # Unit tests
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
    
-   Development dependencies (e.g., `pytest` for testing, `build` for packaging).
    

----------

## 🧪 Testing

This project includes a comprehensive suite of unit tests powered by `pytest`.

### Running Tests

To run the tests, ensure you have the development dependencies installed:

Bash

```
pip install -e ".[dev]"

```

Then, navigate to the project root and run `pytest`:

Bash

```
pytest

```

### Test Coverage

The tests cover:

-   **`is_prime` function logic**: Various known prime and non-prime numbers are tested to ensure the core prime checking algorithm is correct.
    
-   **`list_primes_below` function output**: Verifies that the function correctly prints primes up to a given maximum by capturing standard output.
    
-   **Command-line interface (CLI) behavior**: Uses `subprocess` to simulate CLI invocations, checking:
    
    -   Correct output for valid inputs.
        
    -   Empty output for edge cases (e.g., `MAXIMUM` of 1).
        
    -   Proper error handling and non-zero exit codes for invalid or missing arguments.
        

----------

## 🧑‍💻 Contributing

This project is kept intentionally simple, but pull requests and ideas are welcome!

1.  Fork the repo
    
2.  Create your feature branch (`git checkout -b feature/my-feature`)
    
3.  Commit your changes (`git commit -am 'Add new feature'`)
    
4.  Push to the branch (`git push origin feature/my-feature`)
    
5.  Open a pull request
    

----------

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

You may copy, distribute, and modify the software as long as you track changes/dates in source files. Derivative works must also be licensed under GPLv3.

See the full license in [LICENSE](https://www.google.com/search?q=LICENSE) or at [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html)

----------

## 👤 Author

Ian Ellis

[GitHub](https://github.com/magicalbob)

Feel free to fork, improve, and reuse.
