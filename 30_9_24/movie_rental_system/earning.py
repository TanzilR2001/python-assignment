total_earn=0

def add_earnings(rate):
    global total_earn
    total_earn +=rate
    
def calculate_earnings():
    print(f"Total earning from rental: ${total_earn}")