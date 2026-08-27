# 🤝 Contributing to StudentPy

Thank you for your interest in contributing to **StudentPy**! 🐍

StudentPy is an open-source Python learning library designed for students in **Classes 9–12**. Contributions from students, teachers, developers, and Python enthusiasts are welcome.

Whether you're fixing a small mistake or adding a new program, your contribution can help another student learn.

---

## 🎯 What Can You Contribute?

You can contribute by:

- 🐍 Adding a useful Python program
- 🧠 Adding practice problems
- 🚀 Creating beginner-friendly mini-projects
- 🐛 Fixing bugs
- ✨ Improving existing code
- 📚 Improving explanations or documentation
- 📝 Adding comments to make code easier to understand
- 🔧 Improving the repository structure
- 💡 Suggesting new topics or features

---

## 🗂️ Follow the Repository Structure

Please place your contribution in the appropriate directory.

```text
StudentPy/
│
├── Class-09/
├── Class-10/
├── Class-11/
├── Class-12/
├── Practice/
└── Mini-Projects/
```

For example:

```text
Class-09/
└── Basics/
    └── hello_world.py
```

---

## 🐍 Python Code Guidelines

When submitting Python code:

### 1. Keep it beginner-friendly

Write code that students can understand.

Prefer:

```python
number = int(input("Enter a number: "))
```

over unnecessarily complicated implementations.

### 2. Use meaningful names

Good:

```python
student_name = "Om"
```

Avoid:

```python
x = "Om"
```

when `x` does not clearly describe the value.

### 3. Add comments when useful

Comments should explain **why** something is being done, not simply repeat the code.

```python
# Check whether the number is divisible by 2
if number % 2 == 0:
    print("Even")
```

### 4. Keep programs focused

A single educational program should generally demonstrate one main concept or a small group of related concepts.

### 5. Test your code

Before submitting a contribution, run the program and make sure it works as expected.

---

## 📄 Program Format

Where practical, structure educational programs with:

```text
Program Name
Description
Concepts Used
Code
Example Input
Example Output
Challenge / Try It Yourself
```

Example:

```text
Program: Even or Odd

Concepts:
- Input
- Variables
- Modulus operator
- if-else

Try It Yourself:
Modify the program to also identify whether the number is positive,
negative, or zero.
```

---

## 🔀 How to Contribute

### Step 1 — Fork the Repository

Create your own fork of the StudentPy repository.

### Step 2 — Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/StudentPy.git
```

### Step 3 — Create a Branch

Use a descriptive branch name.

```bash
git checkout -b add-even-odd-program
```

Examples:

```text
add-string-program
fix-loop-example
add-class-11-practical
improve-readme
add-quiz-project
```

### Step 4 — Make Your Changes

Add or improve the relevant files.

Keep your changes focused on one contribution whenever possible.

### Step 5 — Test Your Changes

Run your Python program:

```bash
python filename.py
```

Make sure:

- The program runs correctly.
- There are no obvious errors.
- Input and output behave as expected.
- The code is understandable.
- The program is appropriate for the intended student level.

### Step 6 — Commit Your Changes

Use a clear commit message.

```bash
git add .
git commit -m "Add even odd program"
```

Good commit messages:

```text
Add class 9 loop examples
Fix calculator input handling
Add class 11 file handling example
Improve Python basics documentation
```

Avoid vague messages such as:

```text
update
changes
stuff
final
test
```

### Step 7 — Push Your Branch

```bash
git push origin add-even-odd-program
```

### Step 8 — Open a Pull Request

Create a Pull Request on GitHub.

In the Pull Request description, explain:

- What you changed
- Why you made the change
- Which class/topic it belongs to
- How you tested it

---

## ✅ Pull Request Checklist

Before submitting your Pull Request:

- [ ] My contribution belongs in the correct directory.
- [ ] I tested the code.
- [ ] The code is readable and beginner-friendly.
- [ ] I used meaningful variable and function names.
- [ ] I added explanations where useful.
- [ ] I did not include malicious or unsafe code.
- [ ] I did not intentionally copy copyrighted material.
- [ ] My Pull Request has a clear title.
- [ ] I explained what I changed.

---

## 🚫 What We Don't Accept

StudentPy does not accept contributions containing:

- Malware or malicious code
- Credential-stealing code
- Harmful scripts
- Unnecessary obfuscated code
- Plagiarized or improperly copied material
- Content unrelated to the project's educational purpose
- Programs designed to facilitate illegal activity
- Deliberately broken examples

---

## 💡 New to GitHub?

That's completely fine.

You don't need to be an expert developer to contribute.

You can start with something simple:

1. Find a spelling mistake.
2. Improve an explanation.
3. Add a beginner program.
4. Fix a small bug.
5. Add a practice question.

Every contribution counts. 🌱

---

## 🧑‍🎓 Student Contributions

StudentPy especially welcomes contributions from students.

You can use this project to learn:

- Git
- GitHub
- Python
- Pull Requests
- Open-source collaboration
- Code review
- Documentation

Your first contribution does not need to be perfect. The goal is to **learn, contribute, and improve**.

---

## 🔍 Code Review

Contributions may be reviewed before being merged.

Maintainers may request changes related to:

- Correctness
- Readability
- Educational value
- Organization
- Documentation
- Code quality

Please don't take requested changes personally. Code review is part of open-source development.

---

## 📜 License

By contributing to StudentPy, you agree that your contribution may be distributed under the project's **GNU General Public License v3.0 (GPL-3.0)**.

See the [`LICENSE`](LICENSE) file for details.

---

## 🤝 Thank You!

Thank you for helping build **StudentPy**.

Your contribution could become the example that helps another student understand Python for the first time.

> **Learn → Contribute → Improve → Share. 🐍**
