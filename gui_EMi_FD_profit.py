import tkinter as tk
from tkinter import messagebox

def calculate_emi(principal, rate, years):
    r = rate / (12 * 100)  # Monthly interest rate
    n = years * 12  # Total number of monthly installments
    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return emi

def calculate_years(emi, principal, rate):
    r = rate / (12 * 100)  # Monthly interest rate
    n = 0
    while principal > 0:
        principal = principal + (principal * r) - emi
        n += 1
    years = n // 12
    return years

def calculate_extra_repayment():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    years = int(years_entry.get())
    percentage = float(percentage_entry.get())

    emi = calculate_emi(principal, rate, years)
    target_interest = percentage * principal / 100

    extra_pay_list = np.arange(0.1 * principal, principal, 0.05 * principal)
    for i in extra_pay_list:
        new_years = calculate_years(emi, principal - i, rate)
        paying_interest = emi * 12 * new_years - principal
        if paying_interest <= target_interest:
            part_payment_interest = emi * 12 * new_years - principal
            remaining_principal = principal - i
            fdrate=float(fdrate_entry.get())
            fd_interest = calculate_fd_interest(i, fdrate, years)
            savings = emi*12*(years-new_years)
            result_text = "\nAdditional repayment required: {:.2f}\n".format(i)
            result_text = "\n EMI for {} years: {:.2f}\n".format(new_years,emi)
            result_text += "\nTotal interest we pay {} year: {:.2f}\n".format(new_years, part_payment_interest)
            result_text += "\nSavings without FD: {:.2f}\n".format(savings)
            result_text += "\nFixed Deposit (FD) interest: {:.2f}\n".format(fd_interest)
            result_text += "\n (+) profit/ (-) loss with part payment option: {:.2f}".format(savings - fd_interest-i)
            result_box.configure(state='normal')
            result_box.delete('1.0', tk.END)
            result_box.insert(tk.END, result_text)
            result_box.configure(state='disabled')
            break
    else:
        messagebox.showinfo("Result", "No solution found!")

def calculate_fd_interest(principal, fd_rate, years):
    r = fd_rate / 100  # Convert rate to decimal
    interest=0
    for run in range (years//10):
        principal+=interest
        interest = principal * (1 + r)**10 - principal
    after_tax=interest*0.7
    return after_tax

# Create the main window
window = tk.Tk()
window.title("EMI Calculator")

# Create input labels and entry boxes
principal_label = tk.Label(window, text="Principal amount:")
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

rate_label = tk.Label(window, text="Interest rate per annum:")
rate_label.pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

years_label = tk.Label(window, text="Number of years:")
years_label.pack()
years_entry = tk.Entry(window)
years_entry.pack()

percentage_label = tk.Label(window, text="Percentage of principal needed for total interest payment:")
percentage_label.pack()
percentage_entry = tk.Entry(window)
percentage_entry.pack()

fdrate_label = tk.Label(window, text="FD rate:")
fdrate_label.pack()
fdrate_entry = tk.Entry(window)
fdrate_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_extra_repayment)
calculate_button.pack()

# Create the result box
result_label = tk.Label(window, text="Result:")
result_label.pack()
result_box = tk.Text(window, height=10, width=80, state='disabled')
result_box.pack()

window.mainloop()