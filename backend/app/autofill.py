import re

NEG = r"(no|not|never|don't|do not|didn't|without|none)"

def parse_data(text: str) -> dict:
    text = text.lower()
    data = {}

    m = re.search(r"age\s*(\d+)", text)
    if m:
        data["age"] = m.group(1)

    m = re.search(
        r"(?:bp|blood pressure)\s*(\d+)\s*(?:by|over|/)\s*(\d+)",
        text
    )
    if m:
        data["systolicBP"] = m.group(1)
        data["diastolicBP"] = m.group(2)

    m = re.search(r"(?:blood sugar|glucose|bs)\s*(\d+)", text)
    if m:
        data["bloodSugar"] = m.group(1)

    m = re.search(r"(?:temperature|temp)\s*(\d+\.?\d*)", text)
    if m:
        data["Bodytemp"] = m.group(1)

    m = re.search(r"bmi\s*(\d+\.?\d*)", text)
    if m:
        data["bmi"] = m.group(1)

    m = re.search(r"(?:heart rate|pulse)\s*(\d+)", text)
    if m:
        data["heartrate"] = m.group(1)

    if re.search(fr"{NEG}.*(mental health|depression|anxiety)", text):
        data["mentalHealthConcerns"] =0
    elif re.search(r"(mental health|depression|anxiety)", text):
        data["mentalHealthConcerns"] = 1

    if re.search(fr"{NEG}.*pre[- ]?existing diabetes", text):
        data["preExistingDiabetes"] = 0
    elif re.search(r"pre[- ]?existing diabetes", text):
        data["preExistingDiabetes"] = 1

    if re.search(fr"{NEG}.*gestational diabetes", text):
        data["gestationalDiabetes"] = 0
    elif re.search(r"gestational diabetes", text):
        data["gestationalDiabetes"] = 1

    if re.search(fr"{NEG}.*complication", text):
        data["previousComplications"] = 0
    elif re.search(r"previous.*complication", text):
        data["previousComplications"] = 1

    return data
