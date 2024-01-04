crypto_amount = []
total_buy = []

def take_input():
    count = 0
    while True:
        count += 1
        ns = int(input(f"\nTotal Purchase in naira for transaction {count}: "))
        fee = int(input(f"\nCharges for transaction {count}: "))
        bp = int(input(f"\nUnit Buying Price for transaction {count}: "))
        
        value = (ns + fee)/bp
        
        crypto_amount.append(value)
        
        total_buy.append(ns)

        check = input("Another transaction? y/n")
        if check == 'y':
            continue
        break
    
    return sum(crypto_amount), sum(total_buy) 


def trade():
    crypto_amount, total_buy = take_input()
    
    sp = int(input("\nUnit selling price? "))
    
    trade_value = (sp * crypto_amount) - total_buy
    # print(sp, crypto_amount, total_buy)
    
    return trade_value

print(trade())