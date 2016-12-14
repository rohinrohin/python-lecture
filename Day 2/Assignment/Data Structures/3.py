dept_struct = [
    {
        "dept_id": "125",
        "deptname": "ARCH",
        "emplist": ["Rohin", "Ravi", "Sai"]
    },
    {
        "dept_id": "123",
        "deptname": "CSE",
        "emplist": ["Rohin", "Ravi", "Sai", "Ram", "Ravi"]
    },
    {
        "dept_id": "124",
        "deptname": "MECH",
        "emplist": ["Rohin", "Ravi", "Sai"]
    }
]

emp_no = map(lambda x: (x["deptname"], len(x["emplist"])), dept_struct)
max_size = max(dept_struct, key=lambda y: len(y["emplist"]))

print("Frequency: ", list(emp_no))
print("Highest Employee", max_size)