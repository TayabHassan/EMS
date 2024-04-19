def add_event(events):
    '''
    This function adds events.
    '''
    event_name=input("event name:")
    event_date=input("event date:")
    event_time=input("event time:")
    items=[]
    while True: # Asks for items until enter is pressed to exit.
        item = input("item(or press enter to exit):")
        if item=="":
            break

        try:
             price=float(input("price:"))
        except ValueError:
            print("invalid price. Please enter a valid number.")
            continue
        items.append({"item":item,"price":price})
        event={
            "name":event_name,
            "date":event_date,
            "time":event_time,
            "items":items
        }

        events[event_name]=event
        print("event added successfully")

def edit_event(events,event_name):
    if event_name in events: 
        print("Editing event:", event_name)
        event_date=input("new event date:")
        event_time=input("new event time:")
        items=[]
        while True:

            item=input("new item(or press enter to exit):") #enter your choice
            if item=="":
                break

            try:
                price=float(input("price:"))
            except ValueError:
                    print("invalid price. Please enter a valid number.")
            continue
        items.append({"item":item,"price":price})
        events["date"]=event_date
        events["time"]=event_time
        print("event update successfully")

    else:
        print("event not found")

def delete_event(events, event_name):
    if event_name in events:
        del events[event_name]
        print ("event deleted successfully")
    else:
        print("event not found")

def display_event_names(events):
    if len(events)==0:
        print("event not found")
    else:
        print("event names")

    for event_names in events.keys():
        print("event name: ", event_names)

def display_event_details(events, event_name):
    if event_name in events:
        event=events[event_name]
        print("event_name:",event["name"])
        print("date:",event["date"])
        print("time:",event["time"])
        print("items:")
    
        for item in event["items"]:
            print(item["item"],"_",item["price"])
    else:
        print ("event not found")
def main():
    events={}
    while True:
        print("\n1.Add event\n2.edit event\n3.Delete event\n4.display event names\n5.display event detail\n6.exit")
        choice=input("enter your choice:")
        if choice=="1":
            add_event(events)
        elif choice=="2":
            event_name=input("enter name of my event which i want to edit:")
            edit_event(events,event_name)
        elif choice=="3":
            event_name=input("enter name of my event which i want to delete:")
            delete_event(events, event_name)
        elif choice=="4":
            display_event_names(events)
        elif choice=="5":
            event_name=input("enter name of my event which i want to display details:")
            display_event_details(events, event_name)
        elif choice=="6":
            break
if __name__== "__main__":
    main() 