# Isso exibe uma mensagem de boas-vindas no console.
print("Welcome to the tip calculator.")
# Isso solicita o valor total da conta e o armazena na variável total_bill.
total_bill = float(input("What was the total bill? $"))
# Isso solicita o número de pessoas que dividirão a conta e o armazena na variável number_of_people.
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(
    # Isso solicita a porcentagem da gorjeta e a armazena na variável tip_percentage.
    input("What percentage tip would you like to give? 10, 12, or 15? "))
# Isso calcula a gorjeta e a armazena na variável tip.
tip = total_bill * (tip_percentage / 100)
# Isso adiciona a gorjeta ao valor total da conta e armazena o resultado na variável total_bill.
total_bill += tip
# Isso calcula o valor que cada pessoa deve pagar e o armazena na variável bill_per_person.
bill_per_person = total_bill / number_of_people
# Isso arredonda o valor que cada pessoa deve pagar para duas casas decimais e o armazena na variável final_amount.
final_amount = round(bill_per_person, 2)
# Isso exibe o valor que cada pessoa deve pagar no console.
print(f"Each person should pay: ${final_amount}")
