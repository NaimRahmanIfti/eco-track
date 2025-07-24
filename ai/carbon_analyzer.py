def analyze_carbon(data):
    score = 0
    tips = []

    if data["transport"] == "car":
        score += 30
        tips.append("Try carpooling or public transport.")
    elif data["transport"] == "bus":
        score += 20
    elif data["transport"] == "bike":
        score += 5
    else:
        score += 0

    if data["energy"] == "high":
        score += 30
        tips.append("Reduce air conditioning or heater usage.")
    elif data["energy"] == "moderate":
        score += 15
    else:
        score += 5

    if data["diet"] == "meat":
        score += 30
        tips.append("Try reducing red meat consumption.")
    elif data["diet"] == "mixed":
        score += 20
    elif data["diet"] == "veg":
        score += 10
    else:
        score += 5

    return score, tips[0] if tips else "Great job being eco-friendly!"
