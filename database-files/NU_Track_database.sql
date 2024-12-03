SHOW databases;
USE mysql;



-- Drop all tables to reset the database
DROP TABLE IF EXISTS Interview;
DROP TABLE IF EXISTS Interviewer;
DROP TABLE IF EXISTS Application;
DROP TABLE IF EXISTS Offers;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS Job;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS VisaSponsor;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Departments;
DROP TABLE IF EXISTS FlowChart;
DROP TABLE IF EXISTS Student;



-- Recreate tables
CREATE TABLE Student (
    NUID INT PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    VisaStatus VARCHAR(50) NOT NULL,
    CountryOfOrigin VARCHAR(50) NOT NULL
);

CREATE TABLE FlowChart (
    FlowChartID INT PRIMARY KEY NOT NULL,
    NumApplications INT,
    NumProgress INT,
    NumRejected INT,
    NumAccepted INT,
    FOREIGN KEY (FlowChartID) REFERENCES Student(NUID)
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Head VARCHAR(100) NOT NULL,
    NumberOfEmployees INT
);

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY NOT NULL,
    FullName VARCHAR(100) NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    DepartmentID INT NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Ticket (
    TicketID INT PRIMARY KEY NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL,
    Priority INT NOT NULL,
    TicketType VARCHAR(50) NOT NULL,
    EmployeeID INT NOT NULL,
    StudentNUID INT NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (StudentNUID) REFERENCES Student(NUID)
);

CREATE TABLE VisaSponsor (
    SponsorID INT PRIMARY KEY NOT NULL,
    VisaType VARCHAR(50) NOT NULL,
    SponsorshipPercentage INT
);

CREATE TABLE Company (
    CompanyID INT PRIMARY KEY NOT NULL,
    CompanyName VARCHAR(100) NOT NULL,
    Industry VARCHAR(100),
    Location VARCHAR(100),
    SponsorID INT NOT NULL,
    SponsorshipHistory VARCHAR(100),
    FOREIGN KEY (SponsorID) REFERENCES VisaSponsor(SponsorID)
);

CREATE TABLE Job (
    JobID INT PRIMARY KEY NOT NULL,
    JobDescription TEXT,
    SponsorshipRequired BOOLEAN,
    Deadline DATE NOT NULL,
    CompanyID INT NOT NULL,
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

CREATE TABLE Application (
    ApplicationID INT PRIMARY KEY NOT NULL,
    DateSubmitted DATE NOT NULL,
    Status VARCHAR(50) NOT NULL,
    Priority INT NOT NULL,
    StudentNUID INT NOT NULL,
    JobID INT NOT NULL,
    Notes TEXT,
    FOREIGN KEY (StudentNUID) REFERENCES Student(NUID),
    FOREIGN KEY (JobID) REFERENCES Job(JobID)
);


CREATE TABLE Offers (
    OfferID INT PRIMARY KEY NOT NULL,
    PayRate INT NOT NULL,
    OfferType VARCHAR(50) NOT NULL,
    Location VARCHAR(100),
    CompanyID INT NOT NULL,
    StudentNUID INT NOT NULL,
    FOREIGN KEY (StudentNUID) REFERENCES Student(NUID)
);

CREATE TABLE Interviewer (
    InterviewerID INT PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL

);

CREATE TABLE Interview (
    InterviewID INT PRIMARY KEY NOT NULL,
    Date DATE NOT NULL,
    Location VARCHAR(100),
    InterviewType VARCHAR(50) NOT NULL,
    Round VARCHAR(50) NOT NULL,
    CompanyID INT NOT NULL,
    InterviewerID INT NOT NULL,
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID),
    FOREIGN KEY (InterviewerID) REFERENCES Interviewer(InterviewerID)
);


-- Sample Data

-- Student
INSERT INTO Student (NUID, FirstName, LastName, VisaStatus, CountryOfOrigin)
VALUES
(1001, 'John', 'Doe', 'F1', 'USA'),
(1002, 'Jane', 'Smith', 'H1B', 'India'),
(1003, 'Alice', 'Johnson', 'F1', 'Canada'),
(1004, 'Bob', 'Williams', 'L1', 'Mexico'),
(1005, 'Charlie', 'Brown', 'F1', 'Germany'),
(1006, 'David', 'Davis', 'H1B', 'India'),
(1007, 'Eva', 'Miller', 'F1', 'UK'),
(1008, 'Frank', 'Wilson', 'F1', 'Australia'),
(1009, 'Grace', 'Moore', 'H1B', 'China'),
(1010, 'Hannah', 'Taylor', 'F1', 'Brazil'),
(1011, 'Ivy', 'Martinez', 'F1', 'Mexico'),
(1012, 'Jack', 'Thomas', 'H1B', 'USA'),
(1013, 'Lily', 'Lopez', 'L1', 'Brazil'),
(1014, 'Mason', 'Jackson', 'F1', 'Canada'),
(1015, 'Noah', 'Hernandez', 'H1B', 'Spain'),
(1016, 'Olivia', 'Clark', 'F1', 'Germany'),
(1017, 'Paul', 'Roberts', 'F1', 'France'),
(1018, 'Quinn', 'Walker', 'L1', 'USA'),
(1019, 'Riley', 'Young', 'F1', 'UK'),
(1020, 'Sophia', 'Adams', 'F1', 'Italy'),
(1021, 'Theo', 'Evans', 'H1B', 'Australia'),
(1022, 'Uma', 'King', 'F1', 'India'),
(1023, 'Violet', 'Scott', 'F1', 'Germany'),
(1024, 'Will', 'Green', 'H1B', 'USA'),
(1025, 'Xander', 'Baker', 'L1', 'France'),
(1026, 'Yara', 'Nelson', 'F1', 'Brazil'),
(1027, 'Zane', 'Carter', 'H1B', 'Canada'),
(1028, 'Amelia', 'Perez', 'F1', 'India'),
(1029, 'Blake', 'Mitchell', 'L1', 'USA'),
(1030, 'Chloe', 'Robinson', 'F1', 'Australia'),
(1031, 'Dylan', 'Simmons', 'H1B', 'China'),
(1032, 'Eva', 'Phillips', 'F1', 'Germany'),
(1033, 'Felix', 'Evans', 'F1', 'Spain'),
(1034, 'Gavin', 'Collins', 'H1B', 'USA'),
(1035, 'Holly', 'Morris', 'L1', 'Italy'),
(1036, 'Ian', 'Reed', 'F1', 'Mexico'),
(1037, 'Jasmine', 'Bennett', 'F1', 'UK'),
(1038, 'Kai', 'Foster', 'H1B', 'Canada'),
(1039, 'Liam', 'Gonzalez', 'F1', 'Australia'),
(1040, 'Maya', 'Howard', 'L1', 'USA'),
(1041, 'Nina', 'Wright', 'F1', 'India'),
(1042, 'Oscar', 'Diaz', 'F1', 'Spain'),
(1043, 'Piper', 'Hughes', 'H1B', 'Mexico'),
(1044, 'Quincy', 'Wood', 'F1', 'UK'),
(1045, 'Rachel', 'Price', 'L1', 'USA'),
(1046, 'Sam', 'Jenkins', 'F1', 'Germany'),
(1047, 'Tessa', 'Fox', 'H1B', 'Brazil'),
(1048, 'Ursula', 'Grant', 'F1', 'Canada'),
(1049, 'Victor', 'Ross', 'L1', 'USA'),
(1050, 'Zoe', 'Taylor', 'F1', 'Italy');

-- FlowChart
INSERT INTO FlowChart (FlowChartID, NumApplications, NumProgress, NumRejected, NumAccepted)
VALUES
(1001, 5, 2, 1, 2),
(1002, 6, 3, 2, 1),
(1003, 8, 5, 2, 1),
(1004, 4, 1, 2, 1),
(1005, 7, 4, 3, 0),
(1006, 3, 2, 1, 0),
(1007, 9, 6, 3, 0),
(1008, 10, 7, 1, 2),
(1009, 4, 2, 1, 1),
(1010, 6, 3, 2, 1),
(1011, 5, 3, 1, 1),
(1012, 8, 4, 3, 1),
(1013, 7, 5, 1, 1),
(1014, 6, 2, 2, 2),
(1015, 9, 7, 1, 1),
(1016, 5, 3, 1, 1),
(1017, 4, 2, 1, 1),
(1018, 6, 4, 1, 1),
(1019, 8, 5, 2, 1),
(1020, 7, 6, 1, 0),
(1021, 3, 2, 1, 0),
(1022, 5, 3, 2, 0),
(1023, 9, 7, 2, 0),
(1024, 6, 3, 2, 1),
(1025, 4, 2, 1, 1),
(1026, 8, 6, 1, 1),
(1027, 5, 3, 1, 1),
(1028, 7, 5, 2, 0),
(1029, 6, 4, 1, 1),
(1030, 4, 2, 1, 1),
(1031, 8, 5, 3, 0),
(1032, 6, 4, 1, 1),
(1033, 7, 5, 1, 1),
(1034, 9, 6, 2, 1),
(1035, 5, 3, 1, 1),
(1036, 6, 3, 2, 1),
(1037, 8, 6, 2, 0),
(1038, 7, 5, 1, 1),
(1039, 4, 2, 1, 1),
(1040, 8, 5, 2, 1),
(1041, 6, 4, 1, 1),
(1042, 5, 3, 1, 1),
(1043, 7, 5, 1, 1),
(1044, 6, 3, 2, 1),
(1045, 8, 6, 2, 0),
(1046, 5, 3, 1, 1),
(1047, 9, 6, 2, 1),
(1048, 4, 2, 1, 1),
(1049, 6, 3, 2, 1),
(1050, 7, 4, 1, 2);

-- Departments
INSERT INTO Departments (DepartmentID, Name, Head, NumberOfEmployees)
VALUES
(1, 'Human Resources', 'Sarah Johnson', 10),
(2, 'Engineering', 'Michael Lee', 30),
(3, 'Marketing', 'Emma White', 15);

-- Employee
INSERT INTO Employee (EmployeeID, FullName, EmailAddress, PhoneNumber, Role, DepartmentID)
VALUES
(1, 'Robert Brown', 'robert.brown@company.com', '555-1234', 'HR Manager', 1),
(2, 'Lily Green', 'lily.green@company.com', '555-5678', 'Software Engineer', 2),
(3, 'David Black', 'david.black@company.com', '555-9876', 'Marketing Specialist', 3);

-- Ticket
INSERT INTO Ticket (TicketID, Description, Status, Priority, TicketType, EmployeeID, StudentNUID)
VALUES
(101, 'Issue with visa status update', 'Open', 1, 'Visa Issue', 1, 1001),
(102, 'Application submission error', 'Closed', 2, 'Application Issue', 2, 1002),
(103, 'Job offer clarification needed', 'In Progress', 3, 'Job Application', 3, 1003);

-- VisaSponsor
INSERT INTO VisaSponsor (SponsorID, VisaType, SponsorshipPercentage)
VALUES
(1, 'H-1B', 75),
(2, 'F-1 OPT', 50),
(3, 'L-1', 60);

-- Company
INSERT INTO Company (CompanyID, CompanyName, Industry, Location, SponsorID, SponsorshipHistory)
VALUES
(1, 'TechCorp', 'Technology', 'New York, NY', 1, 'H-1B Sponsorship since 2015'),
(2, 'AutoWorks', 'Automotive', 'Detroit, MI', 2, 'F-1 OPT Sponsorship since 2018'),
(3, 'FinServ Inc.', 'Finance', 'Chicago, IL', 3, 'L-1 Sponsorship since 2020');


-- Job
INSERT INTO Job (JobID, JobDescription, SponsorshipRequired, Deadline, CompanyID)
VALUES
(1, 'Software Engineer for new platform development', TRUE, '2024-12-31', 1),
(2, 'Automotive Engineer for product design', FALSE, '2024-11-30', 2),
(3, 'Financial Analyst for market trends', TRUE, '2024-12-15', 3);

-- Application
INSERT INTO Application (ApplicationID, DateSubmitted, Status, Priority, StudentNUID, JobID, Notes)
VALUES
(1, '2024-10-15', 'In Progress', 1, 1001, 1, 'Strong candidate, visa sponsorship required'),
(2, '2024-10-10', 'Accepted', 2, 1002, 2, 'Successful application, no sponsorship needed'),
(3, '2024-11-05', 'Rejected', 3, 1003, 3, 'Application not shortlisted');

-- Offers
INSERT INTO Offers (OfferID, PayRate, OfferType, Location, CompanyID, StudentNUID)
VALUES
(1, 95000, 'Full-time', 'New York, NY', 1, 1001),
(2, 80000, 'Internship', 'Detroit, MI', 2, 1002),
(3, 110000, 'Full-time', 'Chicago, IL', 3, 1003);

-- Interviewer
INSERT INTO Interviewer (InterviewerID, FirstName, LastName, Email, Role)
VALUES
(1, 'Alice', 'Jones', 'alice.jones@company.com', 'HR Specialist'),
(2, 'Chris', 'Taylor', 'chris.taylor@company.com', 'Engineering Manager'),
(3, 'Sophia', 'Wilson', 'sophia.wilson@company.com', 'Finance Director');

-- Interview
INSERT INTO Interview (InterviewID, Date, Location, InterviewType, Round, CompanyID, InterviewerID)
VALUES
(1, '2024-11-10', 'New York Office', 'Technical', '1st Round', 1, 2),
(2, '2024-11-12', 'Detroit Office', 'Behavioral', '1st Round', 2, 1),
(3, '2024-11-15', 'Chicago Office', 'Technical', '2nd Round', 3, 3);


