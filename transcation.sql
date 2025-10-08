CREATE TABLE accounts (
  empId INTEGER PRIMARY KEY auto_increment,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  balance decimal(10,2)
);

INSERT INTO accounts (name, dept, balance)
VALUES ('clark', 'Sales',11000),
('mani', 'BDM',50000),
('praveen', 'LDM',15000),
('syed', 'TT',60000),
('vicky', 'RM',55000);

SELECT * FROM accounts;
start TRANSACTION;

SAVEPOINT TRANS1;
UPDATE accounts
SET balance = balance-5000 WHERE empId = 2;
UPDATE accounts
SET balance = balance+5000 WHERE empId = 4;

SAVEPOINT TRANS2;
UPDATE accounts
SET balance = balance+15000 WHERE empId = 1;

SAVEPOINT TRANS3;
delete FROM accounts WHERE empId = 3;

ROLLBACK TO SAVEPOINT TRANS3;
select * from accounts;
COMMIT;