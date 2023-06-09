import json
from datetime import datetime

def generate_balance_sheet(json_file):
    with open(json_file) as file:
        parsed_data = json.load(file)

    expense_data = parsed_data['expenseData']
    revenue_data = parsed_data['revenueData']
    balances = {}
    for revenue_entry in revenue_data:
        amount = revenue_entry['amount']
        start_date = datetime.fromisoformat(revenue_entry['startDate'])
        month = start_date.strftime('%Y-%m') 
        balance = amount

        # Update the balance for the month
        if month in balances:
            balances[month] += balance
        else:
            balances[month] = balance
    for expense_entry in expense_data:
        amount = expense_entry['amount']
        start_date = datetime.fromisoformat(expense_entry['startDate'])
        month = start_date.strftime('%Y-%m')
        balance = -amount

    
        if month in balances:
            balances[month] += balance
        else:
            balances[month] = balance

    
    sorted_balances = sorted(balances.items(), key=lambda x: x[0])

    
    output_data={
        'balance':[
            {
                'amount':balance,
                'startDate':f'{month}-01T:00:00.000Z',
            }
            for month,balance in sorted_balances
        ]
    }
    
    output_json=json.dumps(output_data,indent=2)
    print(output_json)

json_file = '1-input.json' 
generate_balance_sheet(json_file)
