"""Q1: State Electricity Subsidy Eligibility – Separate if vs if-elif-else vs Slab Lookup."""

def subsidy_buggy(units, has_ration_card, senior_above_80):
    decisions = []
    if units <= 100:
        decisions.append("Full Subsidy")
    if 101 <= units <= 200 and has_ration_card:
        decisions.append("Partial Subsidy")
    if units > 200 and senior_above_80:
        decisions.append("Senior Citizen Subsidy")
    if not decisions:
        decisions.append("No Subsidy")
    return decisions

def subsidy_fixed(units, has_ration_card, senior_above_80):
    if units <= 100:
        return "Full Subsidy"
    elif 101 <= units <= 200:
        return "Partial Subsidy" if has_ration_card else "No Subsidy"
    else:
        return "Senior Citizen Subsidy" if senior_above_80 else "No Subsidy"

def subsidy_slab_lookup(units, has_ration_card, senior_above_80):
    slabs = [
        (100, lambda r, s: "Full Subsidy"),
        (200, lambda r, s: "Partial Subsidy" if r else "No Subsidy"),
        (float("inf"), lambda r, s: "Senior Citizen Subsidy" if s else "No Subsidy"),
    ]
    for upper, rule in slabs:
        if units <= upper:
            return rule(has_ration_card, senior_above_80)

if __name__ == "__main__":
    households = [
        (80, False, False), (100, True, True), (101, True, False), (101, False, False),
        (200, True, False), (200, False, True), (201, True, False), (250, False, True),
    ]
    for u, rc, sr in households:
        print(f"Units={u:3d}, Ration={str(rc):5s}, Senior={str(sr):5s} -> {subsidy_fixed(u, rc, sr)}")
