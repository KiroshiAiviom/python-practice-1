def main():
    # Read trip details from the user and convert numeric values to float.
    driver_name = input("Enter driver name: ")
    distance = float(input("Enter distance (km): "))
    consumption = float(input("Enter fuel consumption (L/100km): "))
    fuel_price = float(input("Enter fuel price (KZT/L): "))

    litres_needed = distance * consumption / 100
    fuel_cost = litres_needed * fuel_price
    cost_per_km = fuel_cost / distance

    border = "=" * 30
    divider = "-" * 30

    print()
    print(border)
    print("ROAD TRIP SUMMARY".center(30))
    print(border)
    print(f"Driver : {driver_name}")
    print(f"Distance : {distance} km")
    print(f"Consumption : {consumption} L/100km")
    print(f"Fuel price : {fuel_price} KZT/L")
    print(divider)
    print(f"Litres needed: {litres_needed} L")
    print(f"Fuel cost : {fuel_cost} KZT")
    print(f"Cost per km : {cost_per_km} KZT")
    print(border)
    print(f"Trip longer than 300 km: {distance > 300}")
    print(f"Fuel cost above 5000 KZT: {fuel_cost > 5000}")
    print()


if __name__ == "__main__":
    main()
