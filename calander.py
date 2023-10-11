import calendar

# Define the years for which you want to generate calendars
years = [2024, 2025]

# Iterate through the years and print the calendars
for year in years:
    print(f"Calendar for the year {year}:\n")
    
    # Create a calendar object for the specified year
    cal = calendar.TextCalendar(calendar.SUNDAY)  # You can change the starting day if needed

    # Generate and print the calendar for each month
    for month in range(1, 13):
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)

    print("\n")
