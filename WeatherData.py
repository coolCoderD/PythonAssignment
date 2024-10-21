def aggregateWeatherData():
    try:
        num_records = int(input("Enter the number of weather records: "))
        if num_records <= 0:
            raise ValueError("The number of records should be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    records = []

    for _ in range(num_records):
        city = input("Enter city name: ").strip()
        if not city:
            print("City name cannot be empty. Please enter a valid city name.")
            continue

        temperature = None
        humidity = None

        temperature_input = input(f"Enter temperature for {city} (leave blank if not available): ").strip()
        if temperature_input:
            try:
                temperature = float(temperature_input)
            except ValueError:
                print("Invalid temperature input. Please enter a valid number for temperature.")
                continue

        humidity_input = input(f"Enter humidity for {city} (leave blank if not available): ").strip()
        if humidity_input:
            try:
                humidity = float(humidity_input)
            except ValueError:
                print("Invalid humidity input. Please enter a valid number for humidity.")
                continue

        record = {'city': city}
        if temperature is not None:
            record['temperature'] = temperature
        if humidity is not None:
            record['humidity'] = humidity

        records.append(record)

    if not records:
        print("No valid records were provided.")
        return

    cityData = {}
    for record in records:
        city = record.get('city')
        if city not in cityData:
            cityData[city] = {
                'temperature_sum': 0,
                'temperature_count': 0,
                'humidity_sum': 0,
                'humidity_count': 0
            }
        if 'temperature' in record:
            cityData[city]['temperature_sum'] += record['temperature']
            cityData[city]['temperature_count'] += 1
        if 'humidity' in record:
            cityData[city]['humidity_sum'] += record['humidity']
            cityData[city]['humidity_count'] += 1

    result = {}
    for city, data in cityData.items():
        avg_temperature = (
            data['temperature_sum'] / data['temperature_count']
            if data['temperature_count'] > 0 else None
        )
        avg_humidity = (
            data['humidity_sum'] / data['humidity_count']
            if data['humidity_count'] > 0 else None
        )
        
        result[city] = {
            'average_temperature': avg_temperature,
            'average_humidity': avg_humidity
        }
    
    return result

def printFormattedResult(result):
    if not result:
        print("No data to display.")
        return

    print("\nWeather Data Summary:")
    print("=" * 30)
    for city, data in result.items():
        print(f"City: {city}")
        avg_temp = data['average_temperature']
        avg_hum = data['average_humidity']
        temp_str = f"{avg_temp:.2f}°C" if avg_temp is not None else "No data"
        hum_str = f"{avg_hum:.2f}%" if avg_hum is not None else "No data"
        print(f"  Average Temperature: {temp_str}")
        print(f"  Average Humidity: {hum_str}")
        print("-" * 30)

result = aggregateWeatherData()
printFormattedResult(result)
