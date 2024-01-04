crypto_amount = []
total_buy = []


def handle_error(val):
    while True:
        try:
            return int(input (val))
        except ValueError:
            print ('enter a valid integer: ')

def take_input():
    count = 0
    while True:
        count += 1
        ns = handle_error(f"\nTotal Purchase in naira for transaction {count}: ")
        fee = handle_error(f"\nCharges for transaction {count}: ")
        bp = handle_error(f"\nUnit Buying Price for transaction {count}: ")
        
        value = (ns + fee)/bp
        
        crypto_amount.append(value)
        
        total_buy.append(ns)

        if input("Another transaction? y/n: ").lower() == 'y':
        # check = input("Another transaction? y/n").lower()
        # if check == 'y':
            continue
        break
    
    return sum(crypto_amount), sum(total_buy) 


def trade():
    
    crypto_amount, total_buy = take_input()
    
    sp = handle_error("\nUnit selling price? ")

    trade_value = (sp * crypto_amount) - total_buy
    # print(sp, crypto_amount, total_buy)
    
    return trade_value
print (trade())