from datetime import date

def update_streak(last_done , streak):
    """Update the current streak based on the last completion date."""
    today = date.today()
    gap = (today - last_done).days
    if gap == 1:
        return streak +1
    elif gap>1:
        return 1
    else:
        return streak                     #this function increases your streak if you complete the habit yesterday.
    
# Main Program
habit = input("Enter your habit: ")

last_done = None
streak = 0

while True:
    print("\n1. Complete habit")
    print("2. Show streak")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        today = date.today()

        if last_done is None:
            # First time completing the habit
            streak = 1

        else:
            streak = update_streak(last_done, streak)

        last_done = today

        print(f"✅ Habit completed!")
        print(f"🔥 Current streak: {streak} day(s)")

    elif choice == "2":
        print(f"\nHabit: {habit}")
        print(f"🔥 Current streak: {streak} day(s)")

        if last_done:
            print(f"Last completed: {last_done}")
        else:
            print("Habit has not been completed yet.")

    elif choice == "3":
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")    
        