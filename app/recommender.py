def filter_relevant_reports(user_profile: dict, reports: list) -> list:
    relevant = []

    routes = [r.lower() for r in user_profile.get("common_routes", [])]
    zone = user_profile.get("zone", "").lower()
    city = user_profile.get("city", "").lower()

    for report in reports:
        location = report.get("location", "").lower()
        text = f"{location} {report.get('summary', '').lower()}"

        if city in location or zone in location:
            relevant.append(report)
            continue

        for route in routes:
            if route in text:
                relevant.append(report)
                break

    return relevant