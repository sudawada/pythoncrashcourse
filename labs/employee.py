class Employee:
    def __init__(self, name='Default'):
        self.name = name
        self.address = 'Default'
        self.role = 'Default'
        self.manager = 'Default'
        # ID?
        
    def print_attr(self):
        # A custom print statement
        print('name:', self.name)
        print('address:', self.address)
        print('role:', self.role)
        print('manager:', self.manager)
#         print('id:', self.id)
        
    def set_name(self, name):
        self.name = name    
    
    def get_name(self):
        return self.name  
    
    def set_address(self, address):
        self.address = address
        
    def get_address(self):
        return self.address
    
    def set_role(self, role):
        self.role = role
        
    def get_role(self):
        return self.role

    def set_manager(self, manager):
        self.manager = manager
    
    def get_manager(self):
        return self.manager
        
