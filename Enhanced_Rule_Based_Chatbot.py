# Locations
DESTINATIONS = [
	{
		"name": "Goa, India",
		"style": "Beach and relaxation",
		"interests": ["food", "relaxation", "wildlife"],
		"budget": "Medium",
		"reason": "beaches, local food, and a relaxed pace",
		"plans": [
			"Explore a beach and try a local cafe",
			"Visit a market or a historic neighborhood",
			"Take a nature break and enjoy a relaxed evening",
		],
		"packing": ["Sun protection", "Swimwear", "A light rain jacket"],
	},
	{
		"name": "Manali, India",
		"style": "Nature and adventure",
		"interests": ["hiking", "wildlife", "relaxation"],
		"budget": "Low",
		"reason": "mountain scenery, outdoor activities, and fresh air",
		"plans": [
			"Walk around town and find a scenic viewpoint",
			"Choose a local nature walk suited to your fitness level",
			"Spend time by the river or visit a nearby village",
		],
		"packing": ["Comfortable walking shoes", "Warm layers", "A refillable water bottle"],
	},
	{
		"name": "Jaipur, India",
		"style": "Culture and history",
		"interests": ["history", "food", "shopping"],
		"budget": "Low",
		"reason": "historic architecture, colorful markets, and regional food",
		"plans": [
			"Visit a historic landmark",
			"Explore a market and sample regional food",
			"Choose a museum or another heritage site",
		],
		"packing": ["Comfortable walking shoes", "Sun protection", "A small day bag"],
	},
	{
		"name": "Singapore",
		"style": "City and food",
		"interests": ["food", "shopping", "history"],
		"budget": "High",
		"reason": "a lively city, gardens, and many different food choices",
		"plans": [
			"Explore a neighborhood and try a local food center",
			"Visit a garden or city attraction",
			"Spend time in a museum or shopping district",
		],
		"packing": ["Light, breathable clothes", "Comfortable walking shoes", "A compact umbrella"],
	},
	{
		"name": "Kyoto, Japan",
		"style": "Culture and nature",
		"interests": ["history", "hiking", "food"],
		"budget": "High",
		"reason": "historic sites, gardens, and memorable local meals",
		"plans": [
			"Visit a temple or garden, checking opening times first",
			"Walk through a historic district respectfully",
			"Try a local dish and visit a quieter green space",
		],
		"packing": ["Comfortable walking shoes", "A small day bag", "Weather-appropriate layers"],
	},
]


# Function [Choice]
def ask_choice(question, options):
	"""Ask until the traveler selects one of the numbered options."""
	print(f"\n{question}")
	for number, option in enumerate(options, start=1):
		print(f"  {number}. {option}")

	while True:
		answer = input("Your choice: ").strip()
		if answer.isdigit() and 1 <= int(answer) <= len(options):
			return options[int(answer) - 1]
		print(f"Please enter a number from 1 to {len(options)}.")

# Function [Days]
def ask_days():
	"""Get a trip length between one and thirty days."""
	while True:
		answer = input("How many days is your trip? (1-30): ").strip()
		if answer.isdigit() and 1 <= int(answer) <= 30:
			return int(answer)
		print("Please enter a whole number from 1 to 30.")

# Function [Recommend Destinations]
def recommend_destinations(travel_style, interest, budget):
	"""Rank destinations using simple rules based on the traveler's answers."""
	def score(destination):
		points = 0
		if destination["style"] == travel_style:
			points += 3
		if interest in destination["interests"]:
			points += 2
		if destination["budget"] == budget:
			points += 1
		return points

	return sorted(DESTINATIONS, key=score, reverse=True)

# Function [Plan]
def show_trip_plan(destination, days, travel_group, transport):
	print(f"\nYour idea for {destination['name']}")
	print(f"Why it matches: {destination['reason']}.")
	print(f"Budget style: {destination['budget']} (a broad guide, not a price quote).")
	print("\nSample itinerary:")
	for day in range(days):
		plan = destination["plans"][day % len(destination["plans"])]
		print(f"  Day {day + 1}: {plan}")

	print("\nTravel tips:")
	if transport == "Train":
		print("  Check station locations and book popular routes early.")
	elif transport == "Bus":
		print("  Compare departure points and keep water and a light snack handy.")
	elif transport == "Car":
		print("  Check parking and road conditions, and plan rest stops.")
	else:
		print("  Compare nearby airports and allow time for airport transfers.")

	print(f"  Traveling with {travel_group.lower()}? Agree on a meeting point for busy places.")
	print("  Check current opening hours, weather, local guidance, and travel requirements.")

	packing_list = [
		"Photo ID and booking details",
		"Phone, charger, and any needed medicines",
		"Passport or visa, if required for your trip",
	]
	packing_list.extend(destination["packing"])
	if days >= 5:
		packing_list.append("Extra clothing or a plan for laundry")
	if travel_group == "Family":
		packing_list.append("Any snacks or comfort items children may need")
	elif travel_group == "Solo":
		packing_list.append("A trusted contact's details and your check-in plan")
	elif travel_group == "Friends":
		packing_list.append("A shared list of bookings and group contact details")

	print("\nPacking checklist:")
	for item in packing_list:
		print(f"  [ ] {item}")


def plan_trip():
	print("\nLet's plan a trip!")
	name = input("What should I call you? ").strip() or "traveler"
	travel_style = ask_choice(
		"What kind of trip sounds best?",
		["Beach and relaxation", "Nature and adventure", "Culture and history", "City and food", "Culture and nature"],
	)
	interest = ask_choice(
		"What would you most like to do?",
		["food", "hiking", "history", "shopping", "wildlife", "relaxation"],
	)
	days = ask_days()
	budget = ask_choice("How would you describe your budget?", ["Low", "Medium", "High"])
	travel_group = ask_choice(
		"Who are you traveling with?",
		["Solo", "Family", "Friends", "Partner"],
	)
	transport = ask_choice(
		"How do you prefer to get around?",
		["Train", "Bus", "Car", "Plane"],
	)

	recommendations = recommend_destinations(travel_style, interest, budget)
	print(f"\nThanks, {name}! Here are your destination matches:")
	for number, destination in enumerate(recommendations[:3], start=1):
		print(f"  {number}. {destination['name']} - {destination['reason']}.")

	show_trip_plan(recommendations[0], days, travel_group, transport)

# Chat
def main():
	print("Travel Buddy: a rule-based trip planner")
	print("I'll ask a few questions and suggest travel ideas.\n")
	while True:
		plan_trip()
		again = input("\nWould you like to plan another trip? (yes/no): ").strip().lower()
		if again not in {"yes", "y"}:
			print("Thanks for planning with Travel Buddy. Have a great trip!")
			break

# Main
if __name__ == "__main__":
	main()
