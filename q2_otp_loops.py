"""Q2: Bank Kiosk OTP Verification – while, for-else, security question, and recursion."""

def verify_otp_while(entries, correct_otp="482910", security_ok=False):
    attempts = 0
    max_attempts = 3
    idx = 0
    while attempts < max_attempts and idx < len(entries):
        entry = entries[idx].strip()
        idx += 1
        if entry == "":
            continue  # Blank entry does not consume an attempt
        attempts += 1
        if entry == correct_otp:
            return "ACCESS GRANTED"
        if attempts == max_attempts and security_ok:
            max_attempts += 2
            security_ok = False
    else:
        pass  # Placeholder hook for audit telemetry
    return "ACCOUNT LOCKED FOR 30 MINUTES"

def verify_otp_for_else(entries, correct_otp="482910"):
    non_blank = [e.strip() for e in entries if e.strip()]
    for attempt in range(3):
        if attempt >= len(non_blank):
            break
        if non_blank[attempt] == correct_otp:
            return "ACCESS GRANTED"
    else:
        return "ACCOUNT LOCKED FOR 30 MINUTES"
    return "AWAITING INPUT"

def verify_otp_recursive(entries, correct_otp="482910", attempts_left=3):
    if attempts_left == 0:
        return "ACCOUNT LOCKED FOR 30 MINUTES"
    if not entries:
        return "AWAITING INPUT"
    head = entries[0].strip()
    if head == "":
        return verify_otp_recursive(entries[1:], correct_otp, attempts_left)
    if head == correct_otp:
        return "ACCESS GRANTED"
    return verify_otp_recursive(entries[1:], correct_otp, attempts_left - 1)

if __name__ == "__main__":
    print("3 wrong + blanks:", verify_otp_while(["", "111111", "  ", "222222", "333333"]))
    print("Extra attempts  :", verify_otp_while(["111", "222", "333", "482910"], security_ok=True))
    print("For-else locked :", verify_otp_for_else(["111", "222", "333"]))
    print("Recursive ok    :", verify_otp_recursive(["", "111", "482910"]))
