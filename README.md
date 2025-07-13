# 🧮 example_app

A simple command-line Python utility that prints all **prime numbers** less than a given maximum.

This is a minimal educational example, useful for:
- Practicing Python scripting
- Understanding prime number algorithms
- Demonstrating argument parsing with `argparse`

---

## 📦 Features

- Computes prime numbers below a user-specified maximum
- Fast, readable implementation using trial division
- Clean CLI with helpful error messages

---

## 🚀 Installation

Clone the repository and run the script with Python 3:

```bash
git clone https://github.com/yourusername/example_app.git
cd example_app/src/example_app
python example_app.py 50
````

No third-party libraries are required.

---

## 🛠 Usage

```bash
python example_app.py MAXIMUM
```

Where `MAXIMUM` is a positive integer. The app will print all prime numbers **less than** this value.

### Example:

```bash
$ python example_app.py 20
2
3
5
7
11
13
17
19
```

---

## 🧪 Testing

You can test the app manually by running it with various input values.

For example:

```bash
python example_app.py 1        # should print nothing
python example_app.py 10       # should print 2 3 5 7
python example_app.py 1000     # should print many primes
```

---

## 🧑‍💻 Contributing

This project is kept intentionally simple, but pull requests and ideas are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

You may copy, distribute, and modify the software as long as you track changes/dates in source files. Derivative works must also be licensed under GPLv3.

See the full license in [LICENSE](LICENSE) or at [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html)

---

## 👤 Author

**Your Name**
[GitHub](https://github.com/yourusername)
Feel free to fork, improve, and reuse.

---

````

---

### 📎 Notes:
- Replace `yourusername` with your actual GitHub username.
- Consider adding a `LICENSE` file with the full GPLv3 text if you haven’t already:
  ```bash
  curl -o LICENSE https://www.gnu.org/licenses/gpl-3.0.txt
````
