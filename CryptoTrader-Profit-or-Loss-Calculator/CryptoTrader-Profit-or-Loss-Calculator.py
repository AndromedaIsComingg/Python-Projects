trades = []
spent = []

close = str(input('press s to stop or any other key to continue: '))
closed = close.lower()


while True:
    
    if closed != 's':

        buy_price = int(input ("Enter purchase amount in Naira against USDT: "))
        naira_spent = int(input ("Enter how much naira was used to purchase asset: "))
        transfer_fee = int(input ("Enter transfer fee(s): "))
        selling_price = int(input ("Enter selling amount in Naira against USDT: "))

        crypto_amount = (naira_spent + transfer_fee) / buy_price
 
        trades.append(crypto_amount)
        spent.append(naira_spent)
        print(crypto_amount)
        print (naira_spent)

        total_sale = selling_price * crypto_amount 
        profit_loss = (sum(trades) * selling_price) - sum(spent)

        continue
    else:
        selling_price = 0 
        profit_loss = (sum(trades) * selling_price) - sum(spent)

        print(f'your profit is', {profit_loss})
        break