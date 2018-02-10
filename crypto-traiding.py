
# market is the nake of the market Neo/ETH
# type is the type of the transation usualy buy limit
# quoted_units is the units that you bought
# actual_rate is the rate that you bought quoted_units
# actual_fee is the quoted_units that is the fee
# break even is the persent that you want to gain ex. (0.1)
#!/usr/bin/python
import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def findGoodtrades(quoted_units,actual_rate,break_even,actual_fee):
	# example NEO/ETH
	# calculate the fee units
	fee_units_buy = quoted_units * actual_fee;
	print ("fee_units_buy", fee_units_buy)

	#calculate how many etherum did you spend to buy Units
	#this is  etherum units
	initial_unit_base_currency = quoted_units * actual_rate - fee_units_buy;
	print ("initial_unit_base_currency: ",initial_unit_base_currency)

	#calculate fees when sell
	fee_units_sell = initial_unit_base_currency * actual_fee;
	print ("fee_units_sell: ",fee_units_sell)
	#calculate how many etherum want to have back
	#this is  final etherum units
	final_unit_base_currency = initial_unit_base_currency * ( 1 + break_even) + fee_units_sell;
	print("final_unit_base_currency: ",final_unit_base_currency)
	#calculate the value of the rate that you want tou sell
	Final_rate = final_unit_base_currency / quoted_units;
	print("Final_rate: ",Final_rate)
	#calculate how much unit have to sell to break even
	units_to_sell_to_break_even = final_unit_base_currency / Final_rate;
	print("units_to_sell_to_break_even: ",units_to_sell_to_break_even)
	print ("To break even at ",break_even , " you have to sell at ", Final_rate ," ,units", units_to_sell_to_break_even)

def binance(price,amount,total,fee,break_even):
	final_price = price *(1+ break_even)
	print("final_price: ",final_price)
	break_even_amount = total/final_price
	print("break_even_amount:",break_even_amount)
	final_bace_curr = break_even_amount / final_price
	print("final_bace_curr: ",final_bace_curr)



class Transaction:


	def __init__(self, date,market,type,current_price,amount,total,fee,fee_coin):
		self.date = date
		self.market = market
		self.type = type
		self.current_price = current_price
		self.amount = amount
		self.total = total
		self.fee = fee
		self.feecoin = fee_coin
		self.print_transaction()

#culculates the price that you want to sell
	def set_break_even(self,break_even):
		self.break_even = break_even

	def culc_final_price():
		self.final_price = self.price *(1+ self.break_even)
	#the amount of coins that tou have to sell to breake even
	def culc_break_even_amount():
		self.break_even_amount = self.total/self.final_price
	#the final value if you sell all the coins
	def culc_final_base_curr():
		self.final_bace_curr = self.break_even_amount / self.final_price
	#the value of the initial coin
	def culc_final_unit_base_currency():
		self.initial_unit_base_currency = self.amount * self.current_price - self.fee;
	def print_transaction(self):
		print(self.date)
		print(self.market)
		print(self.type)
		print(self.current_price)
		print(self.amount)
		print(self.total)
		print(self.fee)
		print(self.feecoin)




#NEo/ETH

# date = '2018-01-28 18:17:51'
# market = 'VIBETH'
# type = 'buy'
# curr_price = 0.00029501
# amount = 80
# total = 0.01839996
# break_even = 0.3
# fee = 0.003

df = pd.read_excel('hi.xlsx', sheetname='hi')

date = []	# here are stored all the dates from the exel file
market = []
typeM = []
price = []
amount = []
total = []
fee = []
fee_coin = []

transation_list= []


for i in df.index:
	#print(df['Date'][i])
	date.append(df['Date'][i])
	market.append(df['Market'][i])
	typeM.append(df['Type'][i])
	price.append(df['Price'][i])
	amount.append(df['Amount'][i])
	total.append(df['Total'][i])
	fee.append(df['Fee'][i])
	fee_coin.append(df['Fee Coin'][i])
	#print(date)
	transation_list.append(Transaction (date[i],market[i],typeM[i],price[i],amount[i],total[i],fee[i],fee_coin[i]))



# print ("price: ",curr_price)
# print ("amount: ", amount)
# print ("Break_even: " , break_even)
# print ("fee: ", fee)
# print ("total:",total)
# binance(curr_price,amount,total,fee,break_even)

# line = 'VIBETH'
# n=3
# print ([line[i:i+n] for i in range(0, len(line), n)])

#findGoodtrades(Quoted_units,Actual_rate,Break_even,Actual_fee)
