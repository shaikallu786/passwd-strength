import re


def assess_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Assess strength
    score = sum([
        length_criteria,
        bool(uppercase_criteria),
        bool(lowercase_criteria),
        bool(digit_criteria),
        bool(special_char_criteria)
    ])

    # Determine strength level
    if score == 5:
        strength = "Strong"
        feedback = "Your password is strong!"
    elif score >= 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding more complexity for a stronger password."
    else:
        strength = "Weak"
        feedback = "Your password is weak. Consider making it longer and including uppercase letters, numbers, and special characters."

    # Provide detailed feedback
    feedback_details = []
    if not length_criteria:
        feedback_details.append("Make your password at least 8 characters long.")
    if not uppercase_criteria:
        feedback_details.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback_details.append("Include at least one lowercase letter.")
    if not digit_criteria:
        feedback_details.append("Include at least one number.")
    if not special_char_criteria:
        feedback_details.append("Include at least one special character (e.g., !, @, #, etc.).")

    return {
        "strength": strength,
        "feedback": feedback,
        "feedback_details": feedback_details
    }

# Example usage
password = "Abcde@1234"
result = assess_password_strength(password)

print(f"Password Strength: {result['strength']}")
print(result['feedback'])
if result['feedback_details']:
    print("Suggestions:")
    for detail in result['feedback_details']:
        print(f" - {detail}")
