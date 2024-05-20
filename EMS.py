import json
from datetime import datetime

def load_events_from_json():
    try:
        with open("events.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_event(events):
    event_name = input("Event name: ")
    event_date = input("Event date (YYYY-MM-DD): ")
    event_time = input("Event time (HH:MM): ")

    try:
        datetime.strptime(event_date, "%Y-%m-%d")
        datetime.strptime(event_time, "%H:%M")
    except ValueError:
        print("Invalid date or time format. Please enter dates in Year-Month-Day format and time in Hours:Mint format.")
        return

    items = []
    while True:
        item = input("Item (or press enter to exit): ")
        if not item:
            break
        try:
            price = float(input("Price: "))
        except ValueError:
            print("Invalid price. Please enter a valid number.")
            continue
        items.append({"item": item, "price": price})

    event = {
        "name": event_name,
        "date": event_date,
        "time": event_time,
        "items": items
    }

    events[event_name] = event
    print("Event is added successfully")

def edit_event(events, event_name):
    if event_name in events:
        print("Editing event:", event_name)
        event_date = input("New event date (YYYY-MM-DD): ")
        event_time = input("New event time (HH:MM): ")

        try:
            datetime.strptime(event_date, "%Y-%m-%d")
            datetime.strptime(event_time, "%H:%M")
        except ValueError:
            print("Invalid date or time format. Please enter dates in YYYY-MM-DD format and time in HH:MM format.")
            return

        items = []
        while True:
            item = input("if you want to add New item write item name otherwise press enter to exit): ")
            if not item:
                break
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Invalid price. Please enter a valid number.")
                continue
            items.append({"item": item, "price": price})

        events[event_name]["date"] = event_date
        events[event_name]["time"] = event_time
        events[event_name]["items"] = items
        print("Event updated successfully")
    else:
        print("Event not found")
    

def delete_event(events, event_name):
    if event_name in events:
        del events[event_name]
        print("Event deleted successfully")
    else:
        print("Event not found")

def display_events(events):
    if not events:
        print("No events found")
    else:
        print("Events:")
        for event_name, event_details in events.items():
            print("Event name:", event_name)
            print("Date:", event_details["date"])
            print("Time:", event_details["time"])
            print("Items:")
            for item in event_details["items"]:
                print(item["item"], "-", item["price"])

def save_events_to_json(events):
    filename = "events.json"
    with open(filename, "w") as file:
        json.dump(events, file, indent=2)
    print("Events saved to", filename)

def search_events_by_date(events, search_date):
    found = False
    for event_name, event_details in events.items():
        if event_details["date"] == search_date:
            print("Event name:", event_name)
            print("Date:", event_details["date"])
            print("Time:", event_details["time"])
            print("Items:")
            for item in event_details["items"]:
                print(item["item"], "-", item["price"])
            print()
            found = True
    if not found:
        print("No events found for the specified date.")

def search_events_by_time(events, search_time):
    found = False
    for event_name, event_details in events.items():
        if event_details["time"] == search_time:
            print("Event name:", event_name)
            print("Date:", event_details["date"])
            print("Time:", event_details["time"])
            print("Items:")
            for item in event_details["items"]:
                print(item["item"], "-", item["price"])
            print()
            found = True
    if not found:
        print("No events found for the specified time.")

def main():
    events = load_events_from_json()
    while True:
        print("\n1. Add event\n2. Edit event\n3. Delete event\n4. Display events\n5. Search events by date\n6. Search events by time\n7. Save events to JSON\n8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_event(events)
        elif choice == "2":
            event_name = input("Enter the name of the event you want to edit: ")
            edit_event(events, event_name)
        elif choice == "3":
            event_name = input("Enter the name of the event you want to delete: ")
            delete_event(events, event_name)
        elif choice == "4":
            display_events(events)
        elif choice == "5":
            search_date = input("Enter the date to search for (YYYY-MM-DD): ")
            search_events_by_date(events, search_date)
        elif choice == "6":
            search_time = input("Enter the time to search for (HH:MM): ")
            search_events_by_time(events, search_time)
        elif choice == "7":
            save_events_to_json(events)
        elif choice == "8":
            exit
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nCurrent events state:")
            display_events(events)

if __name__ == "__main__":
    main()