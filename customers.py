"""Customers at Hackbright."""
open_file=open("customers.txt")

class Customer(object):
    """Ubermelon customer."""
    def __init__(
                self,
                first_name,
                last_name,
                email,
                password
                      ):
                self.first_name=first_name
                self.last_name=last_name
                self.email=email
                self.password=password
    
    def __repr__(self):
        """Convenience method to show information about customer in console."""
    
        return f"<Customer name: {self.first_name} {self.last_name}, email: {self.email}, password: {self.password}>"

def read_file(file_path):
    """Read and split information from customer file"""
    
    customer_data = {}

    with open(file_path) as file:
        for line in file:
            (first_name, 
            last_name,
            email,
            password) = line.strip().split("|")
        
            customer_data[email] = Customer(first_name, last_name, email, password)
    return customer_data

def get_by_email(email):
    """Get Customer object by email address"""
    
    return customer_data[email]

customer_data = read_file("customers.txt")


# to access class attributes: customer_data["jane@jane.com"].first_name gives Jane