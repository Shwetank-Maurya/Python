import matplotlib.pyplot as plt

sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

total = 0
max = 0
maxmonth = 0
i=0
for  sales in sales_data:
    total += sales
    
    if sales > max:
        max = sales
        maxmonth= i
    i=i+1


average_sales = total / len(sales_data)

print(f"Total Sales: {total:,} thousand")
print(f"Average Sales: {average_sales:.2f} thousand")
print(f"Month with Highest Sales: {months[maxmonth]} {max:,} in thousand")


plt.figure(figsize=(10, 6))
plt.bar(months, sales_data,)


plt.bar(months[maxmonth], sales_data[maxmonth], label='Maximum Sales in a Single Month')

plt.title('Monthly Sales for the Last 12 Months')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y')
plt.show()