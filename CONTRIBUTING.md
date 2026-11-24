# Contributing to Kilele Python Learning Pack

Thank you for your interest in contributing to the **Kilele Python Learning Pack**! This project is maintained by **Kilele Code Studio** as an open educational curriculum designed to introduce young learners and introductory programmers to the joy and discipline of software development.

We welcome contributions from educators, software engineers, students, and curriculum designers.

---

## 💡 Pedagogical Philosophy

When contributing lesson content, exercises, or code samples, keep in mind our core educational principles:

1. **Clarity Over Cleverness**: Code must be straightforward and readable. Avoid esoteric one-liners or complex language tricks (e.g., avoid deeply nested list comprehensions or cryptic lambda functions in introductory modules).
2. **Age-Appropriate Language**: Explanations should be intuitive and engaging for students in Grades 7–10 without watering down genuine computer science terminology.
3. **Active Learning (The 7-Step Cycle)**:
   - Introduce concept with real-world analogies.
   - Explain rules and mechanics.
   - Provide working code demonstrations with clear comments.
   - Offer guided practice tasks.
   - Provide independent exercises.
   - Connect to an applied project.
   - Prompt reflection and debugging.
4. **Resilience & Growth Mindset**: Frame errors as valuable learning checkpoints. Emphasize how to interpret Python tracebacks calmly.

---

## 🛠 Code Standards

- **Python Version**: Python 3.8+ compatibility is required.
- **Dependencies**: Introductory modules and mini-projects must rely solely on the **Python standard library** (no external `pip` packages) so students can run code immediately on any computer.
- **PEP 8 Compliance**: Follow standard Python conventions:
  - `snake_case` for function and variable names.
  - `UPPER_SNAKE_CASE` for constants.
  - `PascalCase` for classes.
  - 4 spaces per indentation level (no tabs).
  - Explicit and meaningful identifier names (e.g. `student_score`, not `sc` or `x`).
- **Comments**: Every significant logic block in demonstration scripts should include friendly comments explaining *why* an operation is performed.

---

## 📱 Accessibility & Device Compatibility

Some learners complete this curriculum without a laptop, using a browser or an Android phone (see [`00-orientation/no-laptop-setups.md`](./00-orientation/no-laptop-setups.md)). When adding code or exercises:

- **Stay in the standard library** (already required above) so no extra installation is needed.
- **Use relative filenames** such as `students.txt`, never machine-specific absolute paths or OS-only commands.
- **Prefer self-contained scripts** where practical. If an exercise needs several files or a custom import, say so in the README so phone/browser learners can pick a compatible tool.
- **Keep `input()` simple** — one question at a time with a clear prompt works best in browser consoles and phone apps.
- **Mention the no-laptop route** in new module READMEs when an exercise depends on files, folders, or the terminal.

---

## 📝 Documentation Standards

Every module and project directory requires a `README.md`. Individual lessons and project READMEs should include:
- **Title and Objectives**: What will the learner know or be able to build?
- **Concept Definition & Purpose**: Why does this concept exist?
- **Syntax and Working Examples**: Clear, runnable code blocks.
- **Common Pitfalls & Mistakes**: Real errors learners frequently encounter and how to resolve them.
- **Practice Exercises**: Step-by-step challenges.

---

## 🔄 How to Submit a Contribution

1. **Fork the Repository**: Create your personal fork on GitHub.
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/module-improvement-or-new-exercise
   ```
3. **Implement Your Changes**: Ensure all code samples run without syntax errors and conform to the standards above.
4. **Test Your Code**:
   ```bash
   python3 <path_to_your_script>.py
   ```
5. **Commit with Clear Messages**:
   ```bash
   git commit -m "docs(02-core-concepts): add common pitfalls section to while-loops.py"
   ```
6. **Submit a Pull Request**: Explain what you added or improved, why it benefits learners, and which section of the curriculum it aligns with.

---

## 📬 Questions or Feedback?

Reach out through our GitHub Issues page or contact the **Kilele Code Studio** education team. Thank you for helping shape the next generation of creators and problem-solvers!
