def forecast_production_volume(hourly_production_rate, shift_hours, shifts_per_day, days_in_a_month, maintenance_hours_per_month, unplanned_downtime_hours_per_month):

    #calculate total production hours available in a month
    total_hours_in_a_month = shift_hours * shifts_per_day * days_in_a_month

    #calculate effective production hours (excluding maintenance and downtime)
    effective_production_hours = total_hours_in_a_month - (maintenance_hours_per_month + unplanned_downtime_hours_per_month)

    #calculate the total production volume for the month
    monthly_production_volume = effective_production_hours * hourly_production_rate

    return monthly_production_volume

forecast_volume = forecast_production_volume (hourly_production_rate= 1000, shift_hours=12 , shifts_per_day=2 , days_in_a_month= 30, maintenance_hours_per_month=20 , unplanned_downtime_hours_per_month=40)
print(f"Forecast production volume for the month: {forecast_volume} units")


