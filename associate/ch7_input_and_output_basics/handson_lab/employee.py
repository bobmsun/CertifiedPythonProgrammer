
class Employee:
    
    default_db_file = "employee_file.txt"

    @classmethod
    def get_all(cls, file_name=None):   # the first variable of the class variable is going to be the class itself
        results = []

        if not file_name:
            file_name = cls.default_db_file
        
        with open(file_name, 'r') as f:
            # identifier is going to be the line number that the employee is written in the file, 
            # so the first employee is gonna be employee number 1.

            # print(f.readlines())
            # ['Kevin Bacon,kbacon@example.com,CEO,555-867-5309\n', 'Bruce Wayne,bwayne@example.com,President,\n']

            # Below we are using list comprehension
            lines = [
                # also strip out the newline caharacter at the end
                line.strip("\n").split(',') + [index + 1]
                for index, line in enumerate(f.readlines())     # the enumerate function is going to return a tuple to us which will give us the actual index and the item itself
            ]
        
        # print(lines)
        # [['Kevin Bacon', 'kbacon@example.com', 'CEO', '555-867-5309', 1], ['Bruce Wayne', 'bwayne@example.com', 'President', '', 2]]
        
        for line in lines:
            results.append(cls(*line))   # We use the class initializer here
            # Since line is going to be a list, if we do the single asterisk * here, it will break that into individual pieces and 
            # we pass this list as all of our positional arguments to our initializer.
            
            # 自己试了一下，下面这行跟上面是等价的
            # results.append(Employee(*line))

        # print([emp.__dict__ for emp in results])
        # [{'name': 'Kevin Bacon', 'email_address': 'kbacon@example.com', 'title': 'CEO', 'phone_number': '555-867-5309\n', 'identifer': 1}, 
        #  {'name': 'Bruce Wayne', 'email_address': 'bwayne@example.com', 'title': 'President', 'phone_number': '\n', 'identifer': 2}]
        
        return results

    @classmethod
    def get_at_line(cls, line_number, file_name=None):
        if not file_name:
            file_name = cls.default_db_file
        
        with open(file_name, 'r') as f:
            # readlines() is going to be a list, it's gonna have zero as the starting index,
            # but line_number starts at 1, so we need to adjust for that.
            line = f.readlines()[line_number - 1]
            attrs = line.strip("\n").split(',') + [line_number]
            return cls(*attrs)

    
    # implement the "save" instance method
    def save(self, file_name=None):
        if not file_name:
            file_name = self.default_db_file
        
        with open(file_name, 'r+') as f:
            lines = f.readlines()
            if self.identifier:
                # Update a line:
                lines[self.identifier - 1] = self._database_line()
            else:
                # add a line
                lines.append(self._database_line())
            f.seek(0)
            f.writelines(lines)
    
    # put a _, because this isn't something we expect any other user of our class to use,
    # we want it to be internal to us. putting a _ 之后，it will not be exposed if someone
    # goes import *. This is something people shouldn't think of it as part of public interface.
    def _database_line(self):
        return (
            ",".join(
                [self.name, self.email_address, self.title, self.phone_number or ""]  # if the phone_number is None, then it's gonna be ""
            )
            + "\n"
        )


    def __init__(self, name, email_address, title, phone_number=None, identifier=None):
        self.name = name
        self.email_address = email_address
        self.title = title
        self.phone_number = phone_number
        self.identifier = identifier
    
    
    def email_signature(self, include_phone=False):
        signature = f"{self.name} - {self.title}\n{self.email_address}"
        if include_phone and self.phone_number:
            signature += f" ({self.phone_number})"
        return signature




# 自己补：__dict__

# The __dict__ in Python represents a dictionary or any mapping object that is used to store the attributes of the object. 
# They are also known as mappingproxy objects. 
# To put it simply, every object in Python has an attribute that is denoted by __dict__.

# president = Employee("Bob Sun", "shihao.m.sun@gmail.com", "PO")
# >>> president.__dict__
# {'name': 'Bob Sun', 'email_address': 'shihao.m.sun@gmail.com', 'title': 'PO', 'phone_number': None}






# enumerator() function
# (class) enumerate(iterable: Iterable[str], start: int = ...)
# Return an enumerate object.
#   iterable
#     an object supporting iteration
# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
# enumerate is useful for obtaining an indexed list:
#     (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

