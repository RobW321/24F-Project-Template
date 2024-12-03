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
(1, 'Engineering', 'Dr. Alan Smith', 50),
(2, 'HR', 'Ms. Sarah Johnson', 15),
(3, 'Finance', 'Mr. Michael Brown', 20),
(4, 'Marketing', 'Ms. Laura White', 30),
(5, 'Sales', 'Mr. Robert Green', 40),
(6, 'Operations', 'Ms. Helen King', 25),
(7, 'IT', 'Mr. William Clark', 35),
(8, 'Legal', 'Ms. Patricia Moore', 12),
(9, 'Product Management', 'Mr. Richard Lewis', 22),
(10, 'R&D', 'Dr. James Miller', 18),
(11, 'Customer Service', 'Mr. David Harris', 50),
(12, 'Logistics', 'Ms. Angela Young', 10),
(13, 'Business Development', 'Mr. Edward King', 15),
(14, 'Design', 'Ms. Sophia Adams', 8),
(15, 'Operations', 'Mr. Steven Knight', 10),
(16, 'Sales Support', 'Mr. James Wilson', 22),
(17, 'Public Relations', 'Ms. Maria Scott', 12),
(18, 'Security', 'Mr. Richard Harper', 25),
(19, 'Compliance', 'Mr. Peter Roy', 10),
(20, 'Audit', 'Mr. Luke Taylor', 12),
(21, 'Procurement', 'Ms. Jane Black', 14),
(22, 'Retail', 'Mr. Tom Brown', 45),
(23, 'Administration', 'Ms. Mary Walker', 10),
(24, 'Training', 'Mr. Arnold Green', 20),
(25, 'Legal Affairs', 'Mr. Greg Hall', 5),
(26, 'Strategy', 'Ms. Diana Evans', 13),
(27, 'Corporate Social Responsibility', 'Mr. Henry Nelson', 8),
(28, 'Sourcing', 'Ms. Alice Collins', 10),
(29, 'Tech Support', 'Ms. Linda Howard', 25),
(30, 'Innovation', 'Mr. Daniel Martin', 15),
(31, 'Business Intelligence', 'Mr. David George', 12),
(32, 'Customer Retention', 'Ms. Lauren Lee', 20),
(33, 'Field Operations', 'Ms. Jennifer White', 12),
(34, 'Supply Chain', 'Mr. William Green', 15),
(35, 'Product Development', 'Mr. Allen Moore', 20),
(36, 'Quality Assurance', 'Mr. Charles Williams', 25),
(37, 'Marketing Strategy', 'Ms. Emily Turner', 12),
(38, 'Retail Operations', 'Mr. James Harris', 40),
(39, 'Customer Insights', 'Ms. Rachel King', 10),
(40, 'Business Analysis', 'Ms. Nancy Young', 30),
(41, 'Digital Marketing', 'Mr. Alan Clark', 15),
(42, 'Legal Compliance', 'Ms. Claire Stevens', 10),
(43, 'Partnerships', 'Mr. Richard Cox', 15),
(44, 'Community Engagement', 'Ms. Betty Scott', 12),
(45, 'Government Relations', 'Mr. Frank Moore', 8),
(46, 'Human Capital', 'Ms. Patricia Taylor', 30),
(47, 'Retail Analytics', 'Mr. Kevin Brown', 10),
(48, 'Brand Management', 'Mr. Thomas Clark', 18),
(49, 'IT Support', 'Ms. Lisa Parker', 12),
(50, 'Customer Experience', 'Mr. David Harris', 50);

-- Employee
INSERT INTO Employee (EmployeeID, FullName, EmailAddress, PhoneNumber, Role, DepartmentID)
VALUES
(1, 'Robert Brown', 'robert.brown@company.com', '555-1234', 'HR Manager', 1),
(2, 'Lily Green', 'lily.green@company.com', '555-5678', 'Software Engineer', 2),
(3, 'David Black', 'david.black@company.com', '555-9876', 'Marketing Specialist', 3)
(4, 'Laura White', 'laura.white@company.com', '555-1001', 'Marketing Manager', 4),
(5, 'Robert Green', 'robert.green@company.com', '555-1002', 'Sales Director', 5),
(6, 'Helen King', 'helen.king@company.com', '555-1003', 'Operations Supervisor', 6),
(7, 'William Clark', 'william.clark@company.com', '555-1004', 'IT Manager', 7),
(8, 'Patricia Moore', 'patricia.moore@company.com', '555-1005', 'Legal Advisor', 8),
(9, 'Richard Lewis', 'richard.lewis@company.com', '555-1006', 'Product Manager', 9),
(10, 'James Miller', 'james.miller@company.com', '555-1007', 'R&D Specialist', 10),
(11, 'David Harris', 'david.harris@company.com', '555-1008', 'Customer Service Representative', 11),
(12, 'Angela Young', 'angela.young@company.com', '555-1009', 'Logistics Coordinator', 12),
(13, 'Edward King', 'edward.king@company.com', '555-1010', 'Business Development Manager', 13),
(14, 'Sophia Adams', 'sophia.adams@company.com', '555-1011', 'Creative Designer', 14),
(15, 'Steven Knight', 'steven.knight@company.com', '555-1012', 'Operations Analyst', 15),
(16, 'James Wilson', 'james.wilson@company.com', '555-1013', 'Sales Support Specialist', 16),
(17, 'Maria Scott', 'maria.scott@company.com', '555-1014', 'PR Officer', 17),
(18, 'Richard Harper', 'richard.harper@company.com', '555-1015', 'Security Analyst', 18),
(19, 'Peter Roy', 'peter.roy@company.com', '555-1016', 'Compliance Officer', 19),
(20, 'Luke Taylor', 'luke.taylor@company.com', '555-1017', 'Auditor', 20),
(21, 'Jane Black', 'jane.black@company.com', '555-1018', 'Procurement Manager', 21),
(22, 'Tom Brown', 'tom.brown@company.com', '555-1019', 'Retail Manager', 22),
(23, 'Mary Walker', 'mary.walker@company.com', '555-1020', 'Administrator', 23),
(24, 'Arnold Green', 'arnold.green@company.com', '555-1021', 'Training Specialist', 24),
(25, 'Greg Hall', 'greg.hall@company.com', '555-1022', 'Legal Affairs Consultant', 25),
(26, 'Diana Evans', 'diana.evans@company.com', '555-1023', 'Strategy Analyst', 26),
(27, 'Henry Nelson', 'henry.nelson@company.com', '555-1024', 'CSR Coordinator', 27),
(28, 'Alice Collins', 'alice.collins@company.com', '555-1025', 'Sourcing Specialist', 28),
(29, 'Linda Howard', 'linda.howard@company.com', '555-1026', 'Tech Support Lead', 29),
(30, 'Daniel Martin', 'daniel.martin@company.com', '555-1027', 'Innovation Officer', 30),
(31, 'David George', 'david.george@company.com', '555-1028', 'Business Intelligence Analyst', 31),
(32, 'Lauren Lee', 'lauren.lee@company.com', '555-1029', 'Customer Retention Specialist', 32),
(33, 'Jennifer White', 'jennifer.white@company.com', '555-1030', 'Field Operations Manager', 33),
(34, 'William Green', 'william.green@company.com', '555-1031', 'Supply Chain Analyst', 34),
(35, 'Allen Moore', 'allen.moore@company.com', '555-1032', 'Product Development Manager', 35),
(36, 'Charles Williams', 'charles.williams@company.com', '555-1033', 'Quality Assurance Specialist', 36),
(37, 'Emily Turner', 'emily.turner@company.com', '555-1034', 'Marketing Strategist', 37),
(38, 'James Harris', 'james.harris@company.com', '555-1035', 'Retail Operations Supervisor', 38),
(39, 'Rachel King', 'rachel.king@company.com', '555-1036', 'Customer Insights Analyst', 39),
(40, 'Nancy Young', 'nancy.young@company.com', '555-1037', 'Business Analyst', 40),
(41, 'Alan Clark', 'alan.clark@company.com', '555-1038', 'Digital Marketing Specialist', 41),
(42, 'Claire Stevens', 'claire.stevens@company.com', '555-1039', 'Legal Compliance Officer', 42),
(43, 'Richard Cox', 'richard.cox@company.com', '555-1040', 'Partnership Manager', 43),
(44, 'Betty Scott', 'betty.scott@company.com', '555-1041', 'Community Engagement Officer', 44),
(45, 'Frank Moore', 'frank.moore@company.com', '555-1042', 'Government Relations Specialist', 45),
(46, 'Patricia Taylor', 'patricia.taylor@company.com', '555-1043', 'Human Capital Manager', 46),
(47, 'Kevin Brown', 'kevin.brown@company.com', '555-1044', 'Retail Analyst', 47),
(48, 'Thomas Clark', 'thomas.clark@company.com', '555-1045', 'Brand Manager', 48),
(49, 'Lisa Parker', 'lisa.parker@company.com', '555-1046', 'IT Support Specialist', 49),
(50, 'David Harris', 'david.harris@company.com', '555-1047', 'Customer Experience Officer', 50);


-- Ticket
INSERT INTO Ticket (TicketID, Description, Status, Priority, TicketType, EmployeeID, StudentNUID)
VALUES
(1, 'Student requested a recommendation letter.', 'Open', 1, 'General', 1, 1001),
(2, 'Technical issue with HR system access.', 'Closed', 2, 'IT Support', 2, 1002),
(3, 'Request for visa sponsorship clarification.', 'In Progress', 3, 'Visa Query', 3, 1003),

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


