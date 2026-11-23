"""
=============================================================================
Kilele Python Learning Pack — Solutions
File: beginner_solutions.py
Description: Reference solutions for Level 1 Beginner Exercises (1 to 10)
=============================================================================
"""

def exercise_1_student_badge():
    print("\n--- Exercise 1: Student Badge ---")
    name = "Amani Mwangi"
    student_id = "KCS-2026-042"
    academy = "Kilele Code Studio"
    focus = "Python Programming"

    print("=" * 40)
    print("       KILELE CODE STUDIO STUDENT BADGE  ")
    print("=" * 40)
    print(f"Name:     {name}")
    print(f"ID:       {student_id}")
    print(f"Academy:  {academy}")
    print(f"Focus:    {focus}")
    print("=" * 40)


def exercise_2_age_calculator(years=14):
    print("\n--- Exercise 2: Age in Months & Days ---")
    months = years * 12
    days = years * 365
    hours = days * 24

    print(f"At {years} years old, you have lived approximately:")
    print(f"- {months:,} months")
    print(f"- {days:,} days")
    print(f"- {hours:,} hours!")


def exercise_3_temperature_converter(celsius=25.0):
    print("\n--- Exercise 3: Temperature Converter ---")
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.1f}°C is equal to {fahrenheit:.1f}°F.")


def exercise_4_bill_splitter(food_bill=80.00, tip_percent=15, people=4):
    print("\n--- Exercise 4: Restaurant Bill Splitter ---")
    tip_amount = food_bill * (tip_percent / 100)
    total_with_tip = food_bill + tip_amount
    each_person_pays = total_with_tip / people

    print(f"Total food bill: ${food_bill:.2f}")
    print(f"Tip percentage:  {tip_percent}%")
    print(f"Number of people: {people}")
    print(f"Tip amount:      ${tip_amount:.2f}")
    print(f"Total with tip:  ${total_with_tip:.2f}")
    print(f"Each person pays: ${each_person_pays:.2f}")


def exercise_5_even_or_odd(number=17):
    print("\n--- Exercise 5: Even or Odd ---")
    if number % 2 == 0:
        print(f"{number} is an EVEN number!")
    else:
        print(f"{number} is an ODD number!")


def exercise_6_password_validator(proposed_password="coder"):
    print("\n--- Exercise 6: Password Validator ---")
    if len(proposed_password) < 8:
        print(f"Password '{proposed_password}': Weak! Must be at least 8 characters long.")
    else:
        print(f"Password '{proposed_password}': Strong! Length accepted.")


def exercise_7_cinema_pricing(customer_age=14):
    print("\n--- Exercise 7: Cinema Ticket Pricing ---")
    if customer_age <= 5:
        category = "Toddler"
        price = 0.00
    elif customer_age <= 12:
        category = "Child"
        price = 5.00
    elif customer_age <= 17:
        category = "Teenager"
        price = 8.00
    else:
        category = "Adult"
        price = 12.00
    
    print(f"Age {customer_age} ({category}) ──▶ Ticket price: ${price:.2f}")


def exercise_8_rectangle_geometry(length=8.5, width=4.0):
    print("\n--- Exercise 8: Rectangle Geometry ---")
    perimeter = 2 * (length + width)
    area = length * width
    print(f"Length: {length}, Width: {width}")
    print(f"Perimeter: {perimeter:.1f} units")
    print(f"Area:      {area:.1f} square units")


def exercise_9_discount_inspector(purchase_total=35.00, has_card=True):
    print("\n--- Exercise 9: Discount Inspector ---")
    if purchase_total > 50.00 or has_card:
        print(f"Purchase: ${purchase_total:.2f}, Card: {has_card} ──▶ Discount APPLIED! (10% off)")
    else:
        print(f"Purchase: ${purchase_total:.2f}, Card: {has_card} ──▶ Standard Price (No discount)")


def exercise_10_inventory_counter():
    print("\n--- Exercise 10: Classroom Inventory ---")
    pencils = 120
    print(f"Initial supply:       {pencils} pencils")
    pencils -= 35  # Distributed to Grade 7
    print(f"After Grade 7 hand-out: {pencils} pencils")
    pencils += 50  # Donation received
    print(f"Final end-of-day tally: {pencils} pencils")


if __name__ == "__main__":
    print("==================================================")
    print("      LEVEL 1 BEGINNER SOLUTIONS DEMONSTRATION    ")
    print("==================================================")
    exercise_1_student_badge()
    exercise_2_age_calculator(14)
    exercise_3_temperature_converter(25.0)
    exercise_4_bill_splitter(80.00, 15, 4)
    exercise_5_even_or_odd(17)
    exercise_6_password_validator("coder")
    exercise_6_password_validator("KileleCoder2026")
    exercise_7_cinema_pricing(14)
    exercise_8_rectangle_geometry(8.5, 4.0)
    exercise_9_discount_inspector(35.00, True)
    exercise_10_inventory_counter()
