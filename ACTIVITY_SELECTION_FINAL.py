from prettytable import PrettyTable

def activity_selection(activities):
    n = len(activities)
    
    # Sort activities by their end times
    activities.sort(key=lambda x: x[1])
    
    selected_activities = [activities[0]]
    last_activity = activities[0]

    for i in range(1, n):
        if activities[i][1] >= last_activity[2]:
            selected_activities.append(activities[i])
            last_activity = activities[i]

    return selected_activities

# Get the number of activities from the user
try:
    print("\n\t\tA C T I V I T Y   S E L E C T I O N\n\n")
    n = int(input("Enter the number of activities: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

activities = []
for i in range(n):
    try:
        start, end = map(int, input(f"Enter start and end times for activity {i + 1}: ").split())
        activities.append((i + 1, start, end))  # Include the original activity number
    except ValueError:
        print(f"Invalid input for activity {i + 1}. Please enter a valid start and end time.")
        exit()

# Create a table to visualize the original activities
table = PrettyTable()
table.field_names = ["Activity", "Start Time", "End Time"]

for activity in activities:
    table.add_row([f"Activity {activity[0]}", f"{activity[1]}", f"{activity[2]}"])

print("\nOriginal Activities:\n")
print(table)

selected_activities = activity_selection(activities)

# Create a table to visualize the selected activities
table = PrettyTable()
table.field_names = ["Selected Activity", "Start Time", "End Time"]

for i, activity in enumerate(selected_activities, start=1):
    table.add_row([f"{activity[0]}", f"{activity[1]}", f"{activity[2]}"])

print("\nSelected Activities:\n")
print(table)
