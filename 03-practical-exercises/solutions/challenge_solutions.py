"""
=============================================================================
Kilele Python Learning Pack — Solutions
File: challenge_solutions.py
Description: Reference solutions for Level 3 Programming Challenges (1 to 5)
=============================================================================
"""

# ==========================================
# Challenge 1: Caesar Cipher
# ==========================================
def caesar_cipher_encrypt(message, shift=3):
    result = []
    for char in message:
        if char.isupper():
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)
        elif char.islower():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)

def caesar_cipher_decrypt(ciphertext, shift=3):
    return caesar_cipher_encrypt(ciphertext, -shift)

def demo_challenge_1():
    print("\n--- Challenge 1: Caesar Cipher Demonstration ---")
    secret = "Meet at Kilele Code Studio at 10 AM!"
    encrypted = caesar_cipher_encrypt(secret, shift=4)
    decrypted = caesar_cipher_decrypt(encrypted, shift=4)
    print("Original: ", secret)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)


# ==========================================
# Challenge 2: Binary Search Guessing AI
# ==========================================
def binary_search_guessing_simulation(target_secret=42, low=1, high=100):
    print(f"\n--- Challenge 2: Binary Search AI (Target Secret: {target_secret}) ---")
    guess_count = 0
    while low <= high:
        guess_count += 1
        guess = (low + high) // 2
        print(f"Guess #{guess_count}: Computer guesses {guess} (Bounds: [{low}, {high}])")

        if guess == target_secret:
            print(f"🎉 Correct! Computer guessed {target_secret} in {guess_count} guesses!")
            return guess_count
        elif guess < target_secret:
            print("  Feedback: 'Too Low' ──▶ Adjusting lower bound.")
            low = guess + 1
        else:
            print("  Feedback: 'Too High' ──▶ Adjusting upper bound.")
            high = guess - 1
    return guess_count


# ==========================================
# Challenge 3: School Tuck Shop POS System
# ==========================================
def demo_tuck_shop_pos():
    print("\n--- Challenge 3: School Tuck Shop POS ---")
    inventory = {
        "A1": {"name": "Granola Bar", "price": 1.50, "stock": 5},
        "B2": {"name": "Fruit Juice", "price": 2.00, "stock": 4},
        "C3": {"name": "Crisp Apple", "price": 0.75, "stock": 10}
    }

    cart = [("A1", 2), ("B2", 1), ("C3", 3)]
    subtotal = 0.0

    print("Receipt:")
    print("-" * 45)
    print(f"{'Item':<15} {'Qty':<5} {'Unit Price':<12} {'Line Total'}")
    print("-" * 45)

    for code, qty in cart:
        item = inventory[code]
        if item["stock"] >= qty:
            item["stock"] -= qty
            line_cost = qty * item["price"]
            subtotal += line_cost
            print(f"{item['name']:<15} {qty:<5} ${item['price']:<11.2f} ${line_cost:.2f}")
        else:
            print(f"OUT OF STOCK: {item['name']}")

    tax = subtotal * 0.08
    grand_total = subtotal + tax

    print("-" * 45)
    print(f"Subtotal:    ${subtotal:.2f}")
    print(f"Tax (8%):    ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")


# ==========================================
# Challenge 4: Morse Code Transmitter
# ==========================================
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}
REVERSE_MORSE = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    words = text.upper().split()
    morse_words = []
    for word in words:
        morse_chars = [MORSE_CODE_DICT.get(c, "") for c in word if c in MORSE_CODE_DICT]
        morse_words.append(" ".join(morse_chars))
    return " / ".join(morse_words)

def morse_to_text(morse_str):
    morse_words = morse_str.split(" / ")
    decoded_words = []
    for m_word in morse_words:
        chars = [REVERSE_MORSE.get(code, "?") for code in m_word.split()]
        decoded_words.append("".join(chars))
    return " ".join(decoded_words)

def demo_challenge_4():
    print("\n--- Challenge 4: Morse Code Translator ---")
    phrase = "KILELE 2026"
    encoded = text_to_morse(phrase)
    decoded = morse_to_text(encoded)
    print("English Text: ", phrase)
    print("Morse Signal: ", encoded)
    print("Decoded Back: ", decoded)


# ==========================================
# Challenge 5: Student Attendance Analyzer
# ==========================================
def analyze_attendance():
    print("\n--- Challenge 5: Student Attendance Analyzer ---")
    attendance_log = {
        "Amina":  ["P", "P", "P", "P", "P"],
        "Kofi":   ["P", "A", "P", "P", "P"],
        "Zawadi": ["P", "P", "P", "P", "P"],
        "Juma":   ["A", "P", "P", "A", "P"]
    }

    days_count = 5
    perfect_streak_students = []

    print("Student Summary:")
    for student, record in attendance_log.items():
        present_days = record.count("P")
        percent = (present_days / days_count) * 100
        is_perfect = percent == 100.0
        if is_perfect:
            perfect_streak_students.append(student)
        badge = "🏆 Perfect Streak!" if is_perfect else ""
        print(f"  {student:<8}: {percent:5.1f}% Present {badge}")

    print("\nPerfect Attendance Awardees:", ", ".join(perfect_streak_students))


if __name__ == "__main__":
    print("==================================================")
    print("      LEVEL 3 CHALLENGE SOLUTIONS DEMONSTRATION   ")
    print("==================================================")
    demo_challenge_1()
    binary_search_guessing_simulation(73)
    demo_tuck_shop_pos()
    demo_challenge_4()
    analyze_attendance()
