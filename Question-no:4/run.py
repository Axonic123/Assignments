import json

# Load the JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)

# Initialize counters and storage
count_india = 0
count_usa = 0
countries = set()
names_starting_with_k = 0
towns = set()
city_counts = {}

# Process each entry in the JSON data
for person in data:
    try:
        # Navigate to the 'address' key in the nested structure
        if ('person_details' in person and 
            'details' in person['person_details'] and 
            'address' in person['person_details']['details']):
            
            address_details = person['person_details']['details']['address']
            country = person['person_details']['details'].get('country', 'Unknown')
            town = address_details.get('detailed', {}).get('town', 'Unknown')
            city = person['person_details']['details'].get('city', 'Unknown')  # Adjusted to match the structure
            first_name = person['person_details'].get('name', 'Unknown').split()[0]  # Assuming name is a full name

            # 1. Count the number of people living in India and USA
            if country == 'India':
                count_india += 1
            elif country == 'USA':
                count_usa += 1

            # 2. Count the number of different countries
            countries.add(country)

            # 3. Count the number of people whose first name starts with K
            if first_name.startswith('K'):
                names_starting_with_k += 1

            # 4. Collect all different towns
            towns.add(town)

            # 5. Count people living in each city (adjusted to how city is represented)
            city_counts[city] = city_counts.get(city, 0) + 1

        else:
            print(f"Missing or misnamed 'address' key in entry: {person}")

    except Exception as e:
        print(f"Error processing entry {person}: {e}")

# Output the results
print(f"Number of people living in India: {count_india}")
print(f"Number of people living in USA: {count_usa}")
print(f"Number of different countries: {len(countries)}")
print(f"Number of people whose first name starts with K: {names_starting_with_k}")

print("\nDifferent towns (sorted):")
for town in sorted(towns):
    print(town)

print("\nCount of people living in each city:")
for city, count in city_counts.items():
    print(f"{city}: {count}")
