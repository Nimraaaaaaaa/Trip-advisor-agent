from Agents.Mock_data import mock_costs

def get_budget_estimate(destination, accommodation_level, duration_days):
    destination = destination.lower()
    if destination not in mock_costs:
        return f"❌ Destination '{destination}' not supported."

    city = mock_costs[destination]

    try:
        acc_cost = city['accommodation'][accommodation_level]
        meal_cost = city['meals']
        transport_cost = city['transport']
    except KeyError:
        return f"❌ Invalid accommodation level. Choose from low, medium, high."

    total_acc = acc_cost * duration_days
    total_meals = meal_cost * duration_days
    total_transport = transport_cost  # One-time

    total = total_acc + total_meals + total_transport

    return {
        "Destination": destination.title(),
        "Accommodation Level": accommodation_level,
        "Stay (x days)": duration_days,
        "Accommodation Total": total_acc,
        "Meals Total": total_meals,
        "Transport": total_transport,
        "Estimated Total Cost": total
    }
