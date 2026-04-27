def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    issues = []

    if length < 8:
        issues.append("Password must be at least 8 characters long")
    if not has_upper:
        issues.append("Add at least one uppercase letter")
    if not has_lower:
        issues.append("Add at least one lowercase letter")
    if not has_digit:
        issues.append("Add at least one number")
    if not has_special:
        issues.append("Add at least one special character")

    if len(issues) == 0:
        return "Strong password"
    else:
        return "Weak password:\n- " + "\n- ".join(issues)


def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    print(check_password_strength(password))


if __name__ == "__main__":
    main()
