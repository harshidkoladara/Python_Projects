CREATE TABLE Film (
    Film_No int NOT NULL PRIMARY KEY,
    Film_Name varchar(255),
    Classification varchar(255),
    Duration number(3),
    Description varchar(255),
    Year_Released number(4),
    CONSTRAINT Duration_Check CHECK(Duration > 0) 
);


CREATE TABLE Cinema (
  Cinema_Name varchar(255) NOT NULL PRIMARY KEY,
    Location varchar(255),
    Year_Opened number(4),
    Manager int
);

CREATE TABLE Staff (
    Employee_No int NOT NULL PRIMARY KEY,
    Name varchar(255),
    Address varchar(255),
    Phone_No char(15),
    DoB date,
    Date_Joined date,
    Salary float,
    Supervisor int REFERENCES Staff(Employee_No),
    Cinema varchar(255) REFERENCES Cinema(Cinema_Name),
    CONSTRAINT DoB_Check CHECK(EXTRACT(year from DoB)+ 18 <= EXTRACT(year from Date_Joined)),
    CONSTRAINT Contact_Check CHECK(LENGTH(Phone_No) >= 10)
);

ALTER TABLE Cinema 
ADD FOREIGN KEY (Manager) REFERENCES Staff(Employee_No);


CREATE TABLE Screen(
  Cinema varchar(255) NOT NULL REFERENCES Cinema(Cinema_Name),
    Screen int NOT NULL,
    Capacity int,
    CONSTRAINT Screen PRIMARY KEY(Screen),
    CONSTRAINT Check_Screen CHECK (Screen > 0),
    CONSTRAINT Check_Capacity CHECK (Capacity > 0)
);


CREATE TABLE Showing (
  Showing_No int NOT NULL PRIMARY KEY,
    Cinema varchar(255) REFERENCES Cinema(Cinema_Name),
    Screen int REFERENCES Screen(Screen),
    Film_No int REFERENCES Film(Film_No)
);



CREATE TABLE Performance(
  Showing_No int NOT NULL REFERENCES Showing(Showing_No),
    Performance_Date date NOT NULL,
    Performance_Time timestamp,
    Takings int,
    Attendees int,
    CONSTRAINT Showing_No PRIMARY KEY(Performance_Date, Showing_No),
    CONSTRAINT Taking CHECK (Takings > 0),
    CONSTRAINT Attendees CHECK (Attendees > 0)
);

