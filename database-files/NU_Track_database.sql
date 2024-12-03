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
(1, 'Student requested a recommendation letter.', 'Open', 1, 'General', 1, 1001),
(2, 'Technical issue with HR system access.', 'Closed', 2, 'IT Support', 2, 1002),
(3, 'Request for visa sponsorship clarification.', 'In Progress', 3, 'Visa Query', 3, 1003),
(4, 'Application system down during submission period.', 'Open', 1, 'System Error', 4, 1004),
(5, 'Help with resume formatting for job application.', 'Closed', 2, 'Career Services', 5, 1005),
(6, 'Lost student ID card.', 'In Progress', 1, 'Lost Item', 6, 1006),
(7, 'Need guidance on interview preparation.', 'Open', 2, 'Career Advice', 7, 1007),
(8, 'Query regarding payroll discrepancy.', 'Closed', 1, 'Payroll', 8, 1008),
(9, 'Internship application support requested.', 'In Progress', 3, 'General Inquiry', 9, 1009),
(10, 'Issue with job application portal access.', 'Closed', 2, 'IT Support', 10, 1010),
(11, 'Question regarding student health benefits.', 'Open', 3, 'HR Inquiry', 11, 1011),
(12, 'Clarification on visa extension process.', 'Closed', 1, 'Visa Query', 12, 1012),
(13, 'Technical error during job application submission.', 'In Progress', 1, 'System Error', 13, 1013),
(14, 'Issue with email communication from recruiter.', 'Closed', 2, 'Communication Issue', 14, 1014),
(15, 'Help needed with interview scheduling.', 'Open', 3, 'Interview Query', 15, 1015),
(16, 'Request for job application deadline extension.', 'Closed', 1, 'Application Process', 16, 1016),
(17, 'Issue with student database registration.', 'In Progress', 1, 'Registration Issue', 17, 1017),
(18, 'Request for feedback on job interview performance.', 'Open', 2, 'Interview Feedback', 18, 1018),
(19, 'Clarification on student loan repayment options.', 'Closed', 3, 'Finance Query', 19, 1019),
(20, 'Assistance with international job placement.', 'Closed', 2, 'Career Services', 20, 1020),
(21, 'Issue with campus parking pass renewal.', 'Open', 1, 'Administrative Support', 21, 1021),
(22, 'Assistance with F1 visa process for employment.', 'Closed', 2, 'Visa Query', 22, 1022),
(23, 'Error in scholarship application system.', 'Closed', 3, 'System Issue', 23, 1023),
(24, 'Help with internship offer acceptance process.', 'In Progress', 1, 'Internship Process', 24, 1024),
(25, 'Request for feedback on recent job rejection.', 'Closed', 2, 'Application Feedback', 25, 1025),
(26, 'Technical issue with career services portal.', 'Open', 1, 'System Issue', 26, 1026),
(27, 'Clarification on international relocation packages.', 'Closed', 2, 'HR Inquiry', 27, 1027),
(28, 'Query regarding tax documents for international students.', 'In Progress', 3, 'HR Query', 28, 1028),
(29, 'Assistance with interview scheduling and prep.', 'Closed', 1, 'Career Services', 29, 1029),
(30, 'Question about payroll tax deductions.', 'Open', 2, 'Payroll', 30, 1030),
(31, 'Help with visa sponsorship for summer internship.', 'In Progress', 1, 'Visa Query', 31, 1031),
(32, 'Request for career coaching session.', 'Open', 2, 'Career Development', 32, 1032),
(33, 'Request for adjustment in job offer location.', 'Closed', 1, 'Offer Adjustment', 33, 1033),
(34, 'Issue with job application portal login.', 'In Progress', 3, 'System Error', 34, 1034),
(35, 'Help with securing part-time employment.', 'Open', 1, 'Employment Support', 35, 1035),
(36, 'Need help with job search strategies.', 'Closed', 2, 'Career Advice', 36, 1036),
(37, 'Clarification on job application status.', 'In Progress', 3, 'Application Status', 37, 1037),
(38, 'Request for advice on improving CV.', 'Open', 2, 'Career Services', 38, 1038),
(39, 'Issue with scholarship application document submission.', 'Closed', 1, 'Scholarship', 39, 1039),
(40, 'Inquiry regarding job relocation assistance.', 'Open', 2, 'Relocation Support', 40, 1040),
(41, 'Assistance with securing housing for internship.', 'In Progress', 1, 'Internship Support', 41, 1041),
(42, 'Request for internship application deadline extension.', 'Closed', 2, 'Application Process', 42, 1042),
(43, 'Follow-up on visa status update.', 'Open', 1, 'Visa Query', 43, 1043),
(44, 'Help with preparing for final-round interview.', 'In Progress', 3, 'Interview Prep', 44, 1044),
(45, 'Request for resume review for job application.', 'Closed', 2, 'Resume Support', 45, 1045),
(46, 'Technical issue with video interview platform.', 'Open', 1, 'Technical Support', 46, 1046),
(47, 'Assistance with international student employment process.', 'Closed', 3, 'Employment Support', 47, 1047),
(48, 'Issue with payment for job application fee.', 'Closed', 2, 'Payment Issue', 48, 1048),
(49, 'Help with relocation assistance for internship offer.', 'In Progress', 1, 'Internship Support', 49, 1049),
(50, 'Request for interview feedback after final round.', 'Open', 2, 'Interview Feedback', 50, 1050);

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


