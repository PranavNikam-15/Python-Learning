def currency_converter():

    rates = {"USD": 1.0, "EUR": 0.92, "INR": 83.2, "GBP": 0.79}

    print("Basic Currency Converter (Base: USD)")
    print("Available currencies:", list(rates.keys()))
    
    from_curr = input("From currency: ").upper()
    to_curr = input("To currency: ").upper()
    
    if from_curr not in rates or to_curr not in rates:
        print("Invalid currency choice.")
        return
    
    try:
        amount = float(input(f"Enter amount in {from_curr}: "))
        amount_in_usd = amount / rates[from_curr]
        converted = amount_in_usd * rates[to_curr]

        print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")

    except ValueError:
        print("Please enter a valid amount.")

currency_converter()