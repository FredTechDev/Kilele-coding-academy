"""
=============================================================================
Kilele Python Learning Pack — Quality Assurance Test Suite
File: tests/test_curriculum_qa.py
Description: Automated test harness verifying syntax, execution, file tree,
             and documentation link integrity across the entire repository.
=============================================================================
"""

import unittest
import os
import sys
import py_compile
import subprocess
import glob
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class TestCurriculumQA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.py_files = []
        for root, _, files in os.walk(REPO_ROOT):
            if ".git" in root or "tests" in root:
                continue
            for f in files:
                if f.endswith(".py"):
                    cls.py_files.append(os.path.join(root, f))
        cls.py_files.sort()

    def test_01_all_python_files_compile(self):
        """Verify that every single Python file compiles with zero syntax errors."""
        print(f"\n[QA Test 1] Verifying compilation of {len(self.py_files)} Python files...")
        self.assertGreaterEqual(len(self.py_files), 33, "Should have at least 33 curriculum python files")
        for path in self.py_files:
            rel = os.path.relpath(path, REPO_ROOT)
            with self.subTest(file=rel):
                try:
                    py_compile.compile(path, doraise=True)
                except py_compile.PyCompileError as e:
                    self.fail(f"Compilation failed for {rel}: {e}")

    def test_02_all_python_scripts_execute(self):
        """Execute each Python file with --demo to ensure clean non-interactive runs."""
        print(f"\n[QA Test 2] Executing {len(self.py_files)} Python files with --demo...")
        for path in self.py_files:
            rel = os.path.relpath(path, REPO_ROOT)
            with self.subTest(file=rel):
                proc = subprocess.run(
                    [sys.executable, path, "--demo"],
                    cwd=os.path.dirname(path),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=15
                )
                self.assertEqual(
                    proc.returncode, 0,
                    f"Execution failed for {rel} (code {proc.returncode}):\n{proc.stderr}"
                )

    def test_03_repository_tree_structure(self):
        """Verify the expected numbered directory layout from MASTER_DOCUMENTATION.md."""
        print("\n[QA Test 3] Checking repository directory tree structure...")
        expected_dirs = [
            "00-orientation",
            "01-getting-started",
            "02-core-concepts",
            "03-practical-exercises",
            "03-practical-exercises/solutions",
            "04-mini-projects",
            "05-capstone-projects",
            "05-capstone-projects/horse-racing-game",
            "05-capstone-projects/school-management-system",
            "05-capstone-projects/student-results-system",
            "06-assessments",
            "07-teacher-resources"
        ]
        for d in expected_dirs:
            full_path = os.path.join(REPO_ROOT, d)
            self.assertTrue(os.path.isdir(full_path), f"Expected directory missing: {d}")

    def test_04_core_documentation_files_exist(self):
        """Verify that root documentation and folder READMEs exist."""
        print("\n[QA Test 4] Checking required documentation files...")
        required_docs = [
            "README.md",
            "CURRICULUM.md",
            "CONTRIBUTING.md",
            "LICENSE",
            "requirements.txt",
            ".gitignore",
            "MASTER_DOCUMENTATION.md",
            "00-orientation/README.md",
            "01-getting-started/README.md",
            "02-core-concepts/README.md",
            "03-practical-exercises/README.md",
            "04-mini-projects/README.md",
            "05-capstone-projects/README.md",
            "06-assessments/README.md",
            "07-teacher-resources/README.md"
        ]
        for f in required_docs:
            full_path = os.path.join(REPO_ROOT, f)
            self.assertTrue(os.path.isfile(full_path), f"Required documentation missing: {f}")

    def test_05_markdown_relative_links(self):
        """Verify that local relative file links in markdown files resolve to existing files."""
        print("\n[QA Test 5] Checking Markdown link integrity...")
        md_files = []
        for root, _, files in os.walk(REPO_ROOT):
            if ".git" in root: continue
            for f in files:
                if f.endswith(".md"):
                    md_files.append(os.path.join(root, f))

        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        broken_links = []

        for md_path in md_files:
            rel_source = os.path.relpath(md_path, REPO_ROOT)
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()

            for text, link in link_pattern.findall(content):
                if link.startswith("http://") or link.startswith("https://") or link.startswith("#") or link.startswith("mailto:"):
                    continue
                # Strip anchor tags like ./file.md#section
                clean_link = link.split("#")[0]
                if not clean_link:
                    continue

                target_path = os.path.normpath(os.path.join(os.path.dirname(md_path), clean_link))
                if not os.path.exists(target_path):
                    broken_links.append((rel_source, link, target_path))

        self.assertEqual(len(broken_links), 0, f"Found broken relative links: {broken_links}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
