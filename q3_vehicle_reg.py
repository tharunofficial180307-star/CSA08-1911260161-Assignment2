"""Q3: Toll Plaza Vehicle Registration Number Validator and Formatter."""
import re

def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
    # TODO 1 Completed
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    # TODO 2 Completed
    if len(reg) not in (9, 10):
        return False
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]
    return state.isalpha() and district.isdigit() and series.isalpha() and number.isdigit()

def format_receipt(reg):
    if not is_valid(reg):
        return "INVALID"
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

def is_valid_regex(reg):
    return bool(re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg))

if __name__ == "__main__":
    samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB", "dl-04-caf-9999", "MH 12 PQ 4321"]
    for raw in samples:
        reg = normalise(raw)
        valid = is_valid(reg)
        assert valid == is_valid_regex(reg)
        print(f"{raw:15} -> {reg:11} {'valid' if valid else 'INVALID':7} | Receipt: {format_receipt(reg)}")
