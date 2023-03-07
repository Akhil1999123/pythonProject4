def salary():
    basic_salary=float(input("enter the baic salary = "))
    #hra=float(input("enter the hra"))
    #da=float(input("enter the daily allowance"))

    hra=basic_salary*(20/100)
    da=basic_salary*(23/100)
    total_salary = basic_salary + hra + da
    print("hra",hra)
    print("da",da)
    print("Total salary =",total_salary)
salary()