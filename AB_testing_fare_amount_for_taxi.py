import pandas as pd
from scipy import stats

taxi_data = pd.read_csv("google_data_analitics\\2017_Yellow_Taxi_Trip_Data.csv", index_col = 0)

#  Data exploration
# In the dataset, payment_type is encoded in integers:
# 1: Credit card
# 2: Cash
# 3: No charge
# 4: Dispute
# 5: Unknown

print(taxi_data.describe(include='all'))
print(taxi_data.info())
print(f'The shape of the dataset: rows are {taxi_data.shape[0]} and columns are {taxi_data.shape[1]}')

# We are intersted in relationship between payment type and the fare amount the customer pays
credit_card = taxi_data[taxi_data['payment_type'] == 1]['fare_amount']
cash = taxi_data[taxi_data['payment_type'] == 2]['fare_amount']
diff_card_vs_cash = credit_card.mean() - cash.mean()

print(f'The mean fare for paying a credit card is {round(credit_card.mean(), 2)}$')
print(f'The mean fare for paying cash is {round(cash.mean(), 2)}$')
print(f'The absolute difference between fare for the credit card and for cash is {round(diff_card_vs_cash, 2)}$')

# Or we can use this code for the same goal/aim
print(taxi_data.groupby('payment_type')['fare_amount'].mean())

# Hypothesis testing

# 𝐻0: There is no difference in the average fare amount between customers who use credit cards and customers who use cash.
# 𝐻a: There is a difference in the average fare amount between customers who use credit cards and customers who use cash.

significance_level = 0.05
statistic_t_score, p_value = stats.ttest_ind(a=credit_card, b=cash, equal_var=False)

print(f'The significance level = {significance_level} or {significance_level*100}%')
print(f'The p-value for our samples is {p_value} or {p_value*100}%')

if p_value < significance_level:
    print('''Since the p-value is significantly smaller than the significance level of 5%, we reject the null hypothesis:
there is a difference in the average fare amount between customers who use credit cards and customers who use cash.''')
else:
    print('Since the p-value is significantly larger/bigger than the significance level of 5%, we fail to reject the null hypothesis.')

# We can conclude that there is a statistically significant difference 
# in the average fare amount between customers who use credit cards and customers who use cash.

# The key business insight is that encouraging customers to pay 
# with credit cards can generate more revenue for taxi cab drivers.
# This project requires an assumption that passengers were forced to pay one way or the other, 
# and that once informed of this requirement, they always complied with it. 
# The data was not collected this way; so, an assumption had to be made to randomly group data 
# entries to perform an A/B test. This dataset does not account for other likely explanations. 
# For example, riders might not carry lots of cash, so it's easier to pay for longer/farther trips 
# with a credit card. In other words, it's far more likely that fare amount determines payment type, rather than vice versa.