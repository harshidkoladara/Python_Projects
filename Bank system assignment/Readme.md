# Coursework: Object-Oriented Programming meets Database

# to run the code run the command

    python assignment.py

# How to Use:

    The code is design like Object Reletional Mapper to reflect CRUD operarions

    ---> Create object of SQLWapper class
            wrapper = SQLWrapper()

    ---> Read data from dataframe and add into table (Create Operation)
            wrapper.create_database('DSA8002 (2021-2022)-dataset.csv')

    ---> Read from the database (READ Operation)
            obj = wrapper.get_data(property = "provider_id",
            value="230002")

    ---> Update value in the Table (UPDATE Operation)
            wrapper.update_data("230002", "hospital_name", "New Hospital")

    ---> Delete record from the database table (DELETE Operation)
            wrapper.delete_data("230002")
