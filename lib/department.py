from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        sql = "CREATE TABLE IF NOT EXISTS departments (id INTRGER PRIMARY KEY, name TEXT, location TEXT)"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO departments (name, location) VALUES (?,?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance"""
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()

    

# creating table
    @classmethod
    def create(cls, name, location):
        sql = "INSERT INTO departments (name, location) VALUES (?,?)"
        CURSOR.execute(sql, (name, location))
        CONN.commit()
        return cls(name, location).save()

# example usage
create_table = Department.create_table()
# drop_table = Department.drop_table()
user = Department.create("Human Resources", "Building C, East Wing")
print(user)


Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

hr.name = "HR"
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>


def Addition(a, b):
    ''' Calculates the addition of two numbers'''
    print("Addition is: ", a + b)
    return a + b
Addition(2, 3)