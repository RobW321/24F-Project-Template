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
