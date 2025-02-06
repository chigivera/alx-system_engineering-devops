# MySQL Replication Setup

## **Step 1: Install MySQL 5.7**
Run the following commands on both **web-01** and **web-02**:

```bash
sudo apt-get update
sudo apt-get install -y mysql-server-5.7
```

Verify installation:

```bash
mysql --version
```

---

## **Step 2: Create MySQL User (`holberton_user`)**
Run the following SQL commands on both servers:

```sql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

Verify:

```bash
mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost';"
```

---

## **Step 3: Create Database and Table (Primary Server `web-01` Only)**

```sql
CREATE DATABASE tyrell_corp;
USE tyrell_corp;

CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO nexus6 (name) VALUES ('Leon');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

Verify:

```bash
mysql -uholberton_user -p -e "USE tyrell_corp; SELECT * FROM nexus6;"
```

---

## **Step 4: Create Replication User (on `web-01` only)**

```sql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'YourStrongPassword';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

Verify:

```bash
mysql -uholberton_user -p -e "SELECT user, Repl_slave_priv FROM mysql.user;"
```

---

## **Step 5: Configure Primary-Replica Infrastructure**

### **On Primary Server (`web-01`)**
Edit MySQL configuration:

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Modify:

```ini
[mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp
```

Restart MySQL:

```bash
sudo systemctl restart mysql
```

Check replication info:

```bash
mysql -uroot -p -e "SHOW MASTER STATUS;"
```

Note down **File** and **Position** values.

---

### **On Replica Server (`web-02`)**
Edit MySQL configuration:

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Modify:

```ini
[mysqld]
server-id = 2
relay_log = /var/log/mysql/mysql-relay-bin.log
```

Restart MySQL:

```bash
sudo systemctl restart mysql
```

Set up replication:

```sql
CHANGE MASTER TO
    MASTER_HOST='54.234.41.125',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='YourStrongPassword',
    MASTER_LOG_FILE='mysql-bin.000009', -- Replace with actual file
    MASTER_LOG_POS=107; -- Replace with actual position

START SLAVE;
```

Check status:

```bash
mysql -uroot -p -e "SHOW SLAVE STATUS\G"
```

---

## **Step 6: Verify Replication**
1. Add a new record on **web-01**:
   
   ```sql
   INSERT INTO tyrell_corp.nexus6 (name) VALUES ('Roy');
   ```

2. Check if it appears on **web-02**:
   
   ```sql
   SELECT * FROM tyrell_corp.nexus6;
   ```

If replication is working, you're done! 🎉

