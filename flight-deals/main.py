from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notifier = NotificationManager()

ORIGIN_CITY_CODE = "LON"

for row in sheet_data:
    dest_code = row["iataCode"]
    if not dest_code:
        continue

    flight = flight_search.search_flights(ORIGIN_CITY_CODE, dest_code)
    print(f"{row['city']} → {flight.price} GBP")

    # Compare price vs lowestPrice from sheet
    try:
        if flight.price != "N/A" and float(flight.price) < row["lowestPrice"]:
            message = (
                f"✈️ Cheap flight alert!\n\n"
                f"Price: £{flight.price}\n"
                f"From: {flight.origin_airport}\n"
                f"To: {flight.destination_airport}\n"
                f"Outbound: {flight.out_date}\n"
                f"Return: {flight.return_date}"
            )
            notifier.send_message(message)
    except ValueError:
        # Handles if flight.price == "N/A"
        pass
