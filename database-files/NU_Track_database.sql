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
(1001, 'Joe', 'Wellington', 'F1', 'USA'),
(1002, 'Josh', 'Brown', 'F1', 'USA'),
(1003, 'Thomas', 'Scott', 'L1', 'Norway'),
(1004, 'Kyrie', 'Irving', 'F1', 'USA'),
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
(1001, 13, 5, 5, 3),
(1002, 13, 5, 4, 4),
(1003, 12, 4, 3, 5),
(1004, 12, 5, 5, 2),
(1005, 5, 4, 3, 0),
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
(4, 'Technical error in application portal', 'Open', 1, 'System Error', 7, 1004),
(5, 'Request for guidance on career options', 'In Progress', 2, 'Career Advice', 24, 1015),
(6, 'Question regarding F-1 visa renewal', 'Closed', 3, 'Visa Query', 12, 1003),
(7, 'Payroll discrepancy for internship stipend', 'Open', 1, 'Payroll', 8, 1020),
(8, 'Issue with job application form submission', 'Closed', 2, 'System Error', 9, 1001),
(9, 'Help needed with LinkedIn profile optimization', 'In Progress', 3, 'Career Services', 36, 1019),
(10, 'Student ID card lost and needs replacement', 'Open', 1, 'Lost Item', 11, 1023),
(11, 'Clarification on tax deductions for students', 'Closed', 2, 'Finance Query', 3, 1027),
(12, 'Request for technical training session', 'In Progress', 3, 'Training', 24, 1030),
(13, 'Support required for securing internship housing', 'Open', 1, 'Internship Support', 41, 1008),
(14, 'Error in scholarship application system', 'Closed', 2, 'Scholarship', 36, 1002),
(15, 'Query regarding visa sponsorship policy', 'In Progress', 3, 'Visa Query', 12, 1009),
(16, 'Help with resume building for job applications', 'Open', 2, 'Career Services', 24, 1014),
(17, 'Issue with email communication system', 'Closed', 1, 'IT Support', 7, 1032),
(18, 'Assistance with interview preparation strategy', 'In Progress', 3, 'Career Services', 24, 1007),
(19, 'Issue with campus Wi-Fi connectivity', 'Open', 1, 'IT Support', 7, 1024),
(20, 'Clarification on company relocation policy', 'Closed', 2, 'HR Inquiry', 17, 1033),
(21, 'Request for job application deadline extension', 'In Progress', 1, 'Application Process', 16, 1016),
(22, 'Request for feedback on internship interview', 'Closed', 3, 'Interview Feedback', 18, 1006),
(23, 'Assistance with scholarship document upload', 'Open', 1, 'Scholarship', 36, 1011),
(24, 'Request for job shadowing opportunities', 'Closed', 2, 'Career Development', 33, 1017),
(25, 'Technical issue with department portal', 'In Progress', 3, 'System Issue', 7, 1025),
(26, 'Assistance with international job applications', 'Open', 1, 'Career Services', 24, 1005),
(27, 'Follow-up on payroll error resolution', 'Closed', 2, 'Payroll', 8, 1018),
(28, 'Request for a career mentoring session', 'In Progress', 3, 'Career Development', 33, 1010),
(29, 'Help with finalizing housing for internship', 'Open', 1, 'Internship Support', 41, 1029),
(30, 'Question about visa options for job', 'Closed', 2, 'Visa Query', 12, 1031),
(31, 'Error with online payment system', 'In Progress', 3, 'System Error', 7, 1012),
(32, 'Clarification on company tax policy for students', 'Open', 2, 'Finance Query', 3, 1034),
(33, 'Issue with technical training registration', 'Closed', 1, 'Training', 24, 1028),
(34, 'Help with securing on-campus employment', 'In Progress', 3, 'Employment Support', 35, 1035),
(35, 'Request for detailed feedback on interview', 'Open', 1, 'Interview Feedback', 18, 1036),
(36, 'Follow-up on lost items in dorm', 'Closed', 2, 'Lost Item', 11, 1039),
(37, 'Request for visa extension support', 'In Progress', 1, 'Visa Query', 12, 1038),
(38, 'Help with understanding F-1 OPT process', 'Open', 2, 'Visa Query', 12, 1040),
(39, 'Issue with campus ID renewal process', 'Closed', 3, 'Administrative Support', 23, 1037),
(40, 'Request for guidance on career switch', 'In Progress', 1, 'Career Advice', 24, 1042),
(41, 'Issue with technical systems in lab', 'Open', 2, 'IT Support', 7, 1043),
(42, 'Help needed with LinkedIn recommendations', 'Closed', 3, 'Career Services', 24, 1041),
(43, 'Clarification on housing subsidy policy', 'In Progress', 1, 'HR Inquiry', 17, 1044),
(44, 'Technical error in career portal access', 'Open', 2, 'System Error', 7, 1045),
(45, 'Request for special visa sponsorship', 'Closed', 3, 'Visa Query', 12, 1046),
(46, 'Assistance with housing options abroad', 'In Progress', 1, 'Internship Support', 41, 1047),
(47, 'Request for early career counseling', 'Open', 2, 'Career Development', 33, 1048),
(48, 'Error in application system submission', 'Closed', 1, 'System Error', 7, 1049),
(49, 'Question about tax implications for internships', 'In Progress', 3, 'Finance Query', 3, 1050),
(50, 'Request for document verification support', 'Open', 1, 'Administrative Support', 23, 1050);


-- VisaSponsor
INSERT INTO VisaSponsor (SponsorID, VisaType, SponsorshipPercentage)
VALUES
(1, 'H1B', 75),
(2, 'L1', 85),
(3, 'F1', 60),
(4, 'O-1', 90),
(5, 'H-2B', 70),
(6, 'B1', 50),
(7, 'TN', 65),
(8, 'J-1', 80),
(9, 'F-1 STEM', 100),
(10, 'O-1A', 95),
(11, 'L-2', 80),
(12, 'H1B', 70),
(13, 'O-1B', 85),
(14, 'F1', 60),
(15, 'L-1A', 90),
(16, 'B1', 55),
(17, 'H1B', 60),
(18, 'O-1', 100),
(19, 'L1', 75),
(20, 'H2A', 65),
(21, 'F-1', 50),
(22, 'O-2', 70),
(23, 'F1', 65),
(24, 'B2', 60),
(25, 'H-1B', 85),
(26, 'J-1', 80),
(27, 'L1B', 90),
(28, 'O-1', 100),
(29, 'TN', 75),
(30, 'H1B', 65),
(31, 'O-1', 75),
(32, 'F-1', 60),
(33, 'O-2A', 80),
(34, 'J1', 95),
(35, 'H1B', 90),
(36, 'L-2', 85),
(37, 'F1', 50),
(38, 'O-1B', 70),
(39, 'L-1A', 95),
(40, 'O-1', 80),
(41, 'H-2B', 75),
(42, 'F1', 100),
(43, 'O-1A', 85),
(44, 'TN', 60),
(45, 'J-1', 90),
(46, 'L-1', 75),
(47, 'B1', 80),
(48, 'H-1B', 85),
(49, 'L1B', 95),
(50, 'O-1', 70);

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
(3, 'Financial Analyst for market trends', TRUE, '2024-12-15', 3),
(4, 'Data Scientist for AI-based tools', TRUE, '2025-01-15', 4),
(5, 'UX Designer for web applications', FALSE, '2024-12-01', 5),
(6, 'Backend Developer for API development', TRUE, '2024-12-20', 6),
(7, 'Marketing Specialist for digital campaigns', FALSE, '2024-11-25', 7),
(8, 'Cybersecurity Analyst for threat detection', TRUE, '2025-02-01', 8),
(9, 'Product Manager for SaaS solutions', FALSE, '2024-12-10', 9),
(10, 'Business Analyst for process optimization', TRUE, '2024-12-05', 10),
(11, 'Cloud Engineer for AWS architecture', TRUE, '2025-01-30', 11),
(12, 'Mobile Developer for iOS applications', TRUE, '2024-11-28', 12),
(13, 'DevOps Engineer for CI/CD pipelines', TRUE, '2025-01-10', 13),
(14, 'Sales Associate for regional outreach', FALSE, '2024-12-08', 14),
(15, 'Content Writer for technical documentation', FALSE, '2024-11-30', 15),
(16, 'Research Scientist for machine learning', TRUE, '2025-02-20', 16),
(17, 'Software Test Engineer for automation testing', TRUE, '2024-12-20', 17),
(18, 'Database Administrator for large datasets', TRUE, '2024-12-15', 18),
(19, 'Technical Support Engineer for IT systems', FALSE, '2024-12-01', 19),
(20, 'AI Engineer for natural language processing', TRUE, '2025-01-25', 20),
(21, 'Full Stack Developer for e-commerce platforms', TRUE, '2025-01-05', 21),
(22, 'Game Developer for multiplayer experiences', TRUE, '2024-12-25', 22),
(23, 'HR Specialist for talent acquisition', FALSE, '2024-11-29', 23),
(24, 'Robotics Engineer for industrial automation', TRUE, '2025-01-20', 24),
(25, 'Operations Manager for logistics coordination', FALSE, '2024-12-18', 25),
(26, 'Digital Marketing Analyst for SEO strategies', FALSE, '2024-12-02', 26),
(27, 'Legal Advisor for contract reviews', FALSE, '2024-12-12', 27),
(28, 'Strategic Planner for business growth', TRUE, '2024-12-28', 28),
(29, 'Systems Engineer for infrastructure development', TRUE, '2025-02-10', 29),
(30, 'Healthcare Analyst for predictive modeling', TRUE, '2025-01-15', 30),
(31, 'Project Manager for software deployments', FALSE, '2024-12-07', 31),
(32, 'Customer Success Manager for SaaS tools', FALSE, '2024-11-30', 32),
(33, 'Blockchain Developer for smart contracts', TRUE, '2025-01-20', 33),
(34, 'Supply Chain Analyst for global operations', FALSE, '2024-12-05', 34),
(35, 'Creative Director for ad campaigns', FALSE, '2024-12-15', 35),
(36, 'AI Researcher for autonomous systems', TRUE, '2025-01-10', 36),
(37, 'Security Engineer for cloud environments', TRUE, '2024-12-25', 37),
(38, 'Embedded Systems Engineer for IoT devices', TRUE, '2025-01-05', 38),
(39, 'Mechanical Engineer for CAD designs', FALSE, '2024-11-28', 39),
(40, 'Social Media Manager for brand growth', FALSE, '2024-12-02', 40),
(41, 'Data Engineer for ETL pipelines', TRUE, '2025-01-30', 41),
(42, 'Quantum Computing Researcher', TRUE, '2025-02-15', 42),
(43, 'Architect for scalable software solutions', TRUE, '2025-01-25', 43),
(44, 'Video Editor for multimedia content', FALSE, '2024-12-08', 44),
(45, 'Finance Manager for budgeting and forecasting', FALSE, '2024-12-15', 45),
(46, 'Electrical Engineer for hardware development', TRUE, '2024-12-28', 46),
(47, 'IT Support Technician for remote assistance', FALSE, '2024-11-30', 47),
(48, 'Mobile Developer for Android applications', TRUE, '2024-12-10', 48),
(49, 'Technical Recruiter for engineering roles', FALSE, '2024-12-05', 49),
(50, 'Research Associate for biotechnology innovations', TRUE, '2025-02-01', 50);

-- Application
INSERT INTO Application (ApplicationID, DateSubmitted, Status, Priority, StudentNUID, JobID, Notes)
VALUES
(1, '2024-10-15', 'In Progress', 1, 1001, 1, 'Strong candidate, visa sponsorship required'),
(2, '2024-10-10', 'Accepted', 2, 1002, 2, 'Successful application, no sponsorship needed'),
(3, '2024-11-05', 'Rejected', 3, 1003, 3, 'Application not shortlisted'),
(4, '2024-10-20', 'In Progress', 1, 1001, 4, 'Awaiting interview schedule'),
(5, '2024-10-18', 'Rejected', 2, 1002, 5, 'Candidate did not meet role requirements'),
(6, '2024-10-25', 'Accepted', 1, 1003, 6, 'Offer pending visa sponsorship confirmation'),
(7, '2024-11-01', 'In Progress', 2, 1004, 7, 'Candidate is a strong match for the role'),
(8, '2024-11-10', 'Rejected', 3, 1001, 8, 'Application not selected for the next round'),
(9, '2024-11-12', 'In Progress', 2, 1002, 9, 'Interview scheduled for next week'),
(10, '2024-11-14', 'In Progress', 1, 1004, 10, 'Waiting for additional documentation from the candidate'),
(11, '2024-10-05', 'In Progress', 2, 1001, 11, 'Resume submitted and under review'),
(12, '2024-10-06', 'Rejected', 3, 1002, 12, 'Candidate lacks relevant experience'),
(13, '2024-10-10', 'Accepted', 1, 1003, 13, 'Role aligned with candidate skills'),
(14, '2024-10-11', 'In Progress', 2, 1004, 14, 'Preliminary screening passed'),
(15, '2024-10-12', 'Rejected', 3, 1001, 15, 'Position filled by another applicant'),
(16, '2024-10-15', 'In Progress', 1, 1002, 16, 'Application awaiting hiring manager review'),
(17, '2024-10-20', 'Accepted', 2, 1003, 17, 'Offer extended pending confirmation'),
(18, '2024-10-21', 'Rejected', 3, 1004, 18, 'Candidate declined to proceed'),
(19, '2024-10-22', 'In Progress', 1, 1001, 19, 'Pending feedback from recruiter'),
(20, '2024-10-25', 'Accepted', 2, 1002, 20, 'Offer accepted, onboarding in process'),
(21, '2024-10-26', 'In Progress', 3, 1003, 21, 'Awaiting further instructions'),
(22, '2024-10-28', 'Rejected', 1, 1004, 22, 'Position no longer available'),
(23, '2024-10-30', 'Accepted', 2, 1001, 23, 'Candidate successfully onboarded'),
(24, '2024-10-31', 'In Progress', 3, 1002, 24, 'Awaiting decision from hiring manager'),
(25, '2024-11-01', 'Rejected', 1, 1003, 25, 'Candidate not shortlisted for the next round'),
(26, '2024-11-02', 'In Progress', 2, 1004, 26, 'Pending feedback from hiring manager'),
(27, '2024-11-03', 'Rejected', 3, 1001, 27, 'Candidate profile not aligned with role requirements'),
(28, '2024-11-04', 'Accepted', 2, 1002, 28, 'Offer extended and accepted'),
(29, '2024-11-05', 'In Progress', 1, 1003, 29, 'Additional documentation requested'),
(30, '2024-11-06', 'Rejected', 2, 1004, 30, 'Candidate withdrew application'),
(31, '2024-11-07', 'Accepted', 3, 1001, 31, 'Candidate successfully completed onboarding'),
(32, '2024-11-08', 'Rejected', 1, 1002, 32, 'Position filled by another applicant'),
(33, '2024-11-09', 'In Progress', 2, 1003, 33, 'Awaiting interview feedback'),
(34, '2024-11-10', 'Accepted', 3, 1004, 34, 'Offer extended pending candidate confirmation'),
(35, '2024-11-11', 'Rejected', 1, 1001, 35, 'Candidate withdrew from the hiring process'),
(36, '2024-11-12', 'In Progress', 2, 1002, 36, 'Interview rescheduled for a later date'),
(37, '2024-11-13', 'Accepted', 3, 1003, 37, 'Offer extended and onboarding in progress'),
(38, '2024-11-14', 'Rejected', 1, 1004, 38, 'Position filled before interview process'),
(39, '2024-11-15', 'In Progress', 2, 1001, 39, 'Additional screening required'),
(40, '2024-11-16', 'Accepted', 3, 1002, 40, 'Candidate cleared background verification'),
(41, '2024-11-17', 'Rejected', 1, 1003, 41, 'Candidate declined interview invitation'),
(42, '2024-11-18', 'In Progress', 2, 1004, 42, 'Awaiting feedback from hiring manager'),
(43, '2024-11-19', 'Accepted', 3, 1001, 43, 'Offer accepted, onboarding in process'),
(44, '2024-11-20', 'Rejected', 1, 1002, 44, 'Candidate not a match for job role'),
(45, '2024-11-21', 'In Progress', 2, 1003, 45, 'Pending interview outcome'),
(46, '2024-11-22', 'Accepted', 3, 1004, 46, 'Offer extended pending visa confirmation'),
(47, '2024-11-23', 'Rejected', 1, 1001, 47, 'Candidate did not meet job requirements'),
(48, '2024-11-24', 'In Progress', 2, 1002, 48, 'Interview scheduled for next week'),
(49, '2024-11-25', 'Accepted', 3, 1003, 49, 'Role offered and accepted'),
(50, '2024-11-26', 'Rejected', 1, 1004, 50, 'Candidate withdrew from hiring process'),
(51, '2024-11-01', 'In Progress', 1, 1005, 1, 'Strong background in required skills, awaiting interview'),
(52, '2024-11-02', 'Accepted', 2, 1006, 2, 'Offer extended, no sponsorship required'),
(53, '2024-11-03', 'Rejected', 3, 1007, 3, 'Not a match for the role requirements'),
(54, '2024-11-04', 'In Progress', 1, 1008, 4, 'Resume under review, initial feedback positive'),
(55, '2024-11-05', 'Rejected', 2, 1009, 5, 'Application not shortlisted for next round'),
(56, '2024-11-06', 'Accepted', 3, 1010, 6, 'Offer extended and candidate accepted'),
(57, '2024-11-07', 'In Progress', 1, 1011, 7, 'Pending additional documents from the candidate'),
(58, '2024-11-08', 'Rejected', 2, 1012, 8, 'Position filled by another applicant'),
(59, '2024-11-09', 'Accepted', 3, 1013, 9, 'Candidate cleared all interview rounds'),
(60, '2024-11-10', 'In Progress', 1, 1014, 10, 'Awaiting final decision from the recruiter'),
(61, '2024-11-11', 'Rejected', 2, 1015, 11, 'Application withdrawn by candidate'),
(62, '2024-11-12', 'Accepted', 3, 1016, 12, 'Candidate successfully onboarded'),
(63, '2024-11-13', 'In Progress', 1, 1017, 13, 'Initial interview completed, awaiting feedback'),
(64, '2024-11-14', 'Rejected', 2, 1018, 11, 'Application not aligned with job role'),
(65, '2024-11-15', 'Accepted', 3, 1019, 12, 'Offer extended pending candidate confirmation'),
(66, '2024-11-16', 'In Progress', 1, 1020, 23, 'Strong candidate, pending hiring manager feedback'),
(67, '2024-11-17', 'Rejected', 2, 1021, 31, 'Candidate did not pass technical screening'),
(68, '2024-11-18', 'Accepted', 3, 1022, 42, 'Successful application, onboarding scheduled'),
(69, '2024-11-19', 'In Progress', 1, 1023, 43, 'Awaiting further updates from hiring manager'),
(70, '2024-11-20', 'Rejected', 2, 1024, 41, 'Application reviewed but not shortlisted'),
(71, '2024-11-21', 'Accepted', 3, 1025, 42, 'Offer extended, role aligned with candidate skills'),
(72, '2024-11-22', 'In Progress', 1, 1026, 43, 'Initial screening cleared, next round scheduled'),
(73, '2024-11-23', 'Rejected', 2, 1027, 41, 'Position filled before application review'),
(74, '2024-11-24', 'Accepted', 3, 1028, 42, 'Candidate successfully onboarded'),
(75, '2024-11-25', 'In Progress', 1, 1029, 43, 'Awaiting final decision from hiring team'),
(76, '2024-11-26', 'Rejected', 2, 1030, 21, 'Application not shortlisted due to lack of experience'),
(77, '2024-11-27', 'Accepted', 3, 1031, 22, 'Offer extended pending candidate confirmation'),
(78, '2024-11-28', 'In Progress', 1, 1032, 23, 'Pending hiring manager approval'),
(79, '2024-11-29', 'Rejected', 2, 1033, 21, 'Application not aligned with job description'),
(80, '2024-11-30', 'Accepted', 3, 1034, 32, 'Successful application, visa sponsorship confirmed'),
(81, '2024-12-01', 'In Progress', 1, 1035, 33, 'Awaiting additional information from candidate'),
(82, '2024-12-02', 'Rejected', 2, 1036, 13, 'Position filled by internal candidate'),
(83, '2024-12-03', 'Accepted', 3, 1037, 32, 'Candidate cleared all rounds, onboarding scheduled'),
(84, '2024-12-04', 'In Progress', 1, 1038, 33, 'Initial interview completed, awaiting final feedback'),
(85, '2024-12-05', 'Rejected', 2, 1039, 31, 'Application withdrawn by candidate'),
(86, '2024-12-06', 'Accepted', 3, 1040, 42, 'Offer extended, visa sponsorship in process'),
(87, '2024-12-07', 'In Progress', 1, 1041, 43, 'Resume under review, initial feedback positive'),
(88, '2024-12-08', 'Rejected', 2, 1042, 41, 'Application not aligned with hiring requirements'),
(89, '2024-12-09', 'Accepted', 3, 1043, 12, 'Successful application, onboarding scheduled'),
(90, '2024-12-10', 'In Progress', 1, 1044, 33, 'Awaiting final decision from recruiter'),
(91, '2024-12-11', 'Rejected', 2, 1045, 1, 'Application reviewed but not selected for next round'),
(92, '2024-12-12', 'Accepted', 3, 1046, 2, 'Offer extended, role aligned with skills'),
(93, '2024-12-13', 'In Progress', 1, 1047, 3, 'Initial screening cleared, next round scheduled'),
(94, '2024-12-14', 'Rejected', 2, 1048, 31, 'Position filled by another applicant'),
(95, '2024-12-15', 'Accepted', 3, 1049, 32, 'Offer extended, visa requirements met'),
(96, '2024-12-16', 'In Progress', 1, 1050, 33, 'Strong candidate, awaiting final interview feedback');


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


