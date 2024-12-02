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
(1001, 'John', 'Doe', 'F-1', 'USA'),
(1002, 'Jane', 'Smith', 'H-1B', 'India'),
(1003, 'Ali', 'Ahmed', 'F-1', 'Pakistan');

-- FlowChart
INSERT INTO FlowChart (FlowChartID, NumApplications, NumProgress, NumRejected, NumAccepted)
VALUES
(1001, 5, 3, 1, 1),
(1002, 7, 5, 0, 2),
(1003, 4, 2, 2, 0);

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


