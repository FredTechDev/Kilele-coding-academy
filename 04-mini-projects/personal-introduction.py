"""
=============================================================================
Kilele Python Learning Pack — Mini-Project 1
Project: Personal Introduction & Coder Profile Generator
File: personal-introduction.py
Concepts Applied: Console output, variables, string manipulation, f-strings
=============================================================================
"""

import sys

def get_input(prompt, demo_default):
    if "--demo" in sys.argv:
        print(f"{prompt}[Auto-demo]: {demo_default}")
        return demo_default
    try:
        val = input(prompt).strip()
        return val if val else demo_default
    except (EOFError, KeyboardInterrupt):
        return demo_default

def generate_coder_profile():
    print("=" * 60)
    print("      KILELE CODE STUDIO · DIGITAL CODER BIO CREATOR      ")
    print("=" * 60)
    print("Answer a few quick questions to generate your official developer badge!\n")

    full_name = get_input("1. What is your full name? ", "Amani Mwangi").title()
    age = get_input("2. How old are you? ", "14")
    city = get_input("3. What city are you coding from? ", "Nairobi").title()
    grade = get_input("4. What school grade are you in? ", "Grade 9")
    favorite_track = get_input("5. What is your tech interest (e.g. AI, Games, Web)? ", "Game Development").title()
    dream_project = get_input("6. What is your dream project to build? ", "An African Mythology Adventure RPG")

    # Generate ASCII Developer ID Badge
    print("\n" + "#" * 60)
    print(f"#{'OFFICIAL KILELE DEVELOPER PASSPORT':^58}#")
    print("#" * 60)
    print(f"#  Full Name:      {full_name:<42}#")
    print(f"#  Age & Cohort:   {age + ' years old | ' + grade:<42}#")
    print(f"#  Base City:      {city:<42}#")
    print(f"#  Specialization: {favorite_track:<42}#")
    print(f"#  Status:         Active Junior Software Engineer           #")
    print("#" + "-" * 58 + "#")
    print(f"#  MISSION STATEMENT:                                        #")
    wrapped_mission = f"Building: {dream_project}"
    print(f"#  {wrapped_mission:<56}#")
    print("#" * 60)

    # Narrative Introduction
    print("\n📝 Biography Summary:")
    print(
        f"Meet {full_name}, a {age}-year-old {grade} student coding from {city}. "
        f"With a passion for {favorite_track}, {full_name} is on a mission to create "
        f"'{dream_project}' using Python and computational thinking. "
        f"Welcome to the builder generation! 🚀\n"
    )

if __name__ == "__main__":
    generate_coder_profile()
