# Web Infrastructure Design

This project focuses on designing and understanding various web infrastructure configurations, from simple setups to more complex, distributed systems. Each design is represented using Mermaid diagrams that can be viewed in any online Mermaid editor.

## Project Overview

The project explores different levels of web infrastructure, including:
- Simple web stack (1 server)
- Distributed web infrastructure (3 servers)
- Secured and monitored infrastructure
- Scaled up infrastructure

## How to View the Diagrams

1. Copy the content of any `.md` file in this repository
2. Visit an online Mermaid editor (e.g., [Mermaid Live Editor](https://mermaid.live/))
3. Paste the content to visualize the infrastructure diagram

## Directory Structure

```
0x09-web_infrastructure_design/
├── 0-simple_web_stack
├── 1-distributed_web_infrastructure
├── 2-secured_and_monitored_web_infrastructure
└── 3-scale_up
```

## Task Descriptions

### 0. Simple Web Stack
- Single server infrastructure
- Components: Nginx, Application Server, MySQL
- Domain: www.foobar.com
- Focuses on basic web hosting concepts

### 1. Distributed Web Infrastructure
- Three-server infrastructure
- Load balancer (HAproxy)
- Primary-Replica database setup
- Explores scalability and redundancy

### 2. Secured and Monitored Infrastructure
- SSL/TLS encryption
- Firewall implementation
- Monitoring system integration
- Focus on security and performance monitoring

### 3. Scale Up (Advanced)
- Component separation
- Load balancer clustering
- Server specialization
- Infrastructure optimization

## Key Concepts Covered

- DNS Configuration
- Load Balancing
- Database Replication
- Server Roles
- Security Measures
- Monitoring Solutions
- High Availability
- SPOF (Single Point of Failure)
- Scalability

## Learning Objectives

After completing this project, you should be able to explain:
- Components of a web infrastructure
- System redundancy
- LAMP stack
- Load balancing algorithms
- Database Primary-Replica cluster
- Server roles and responsibilities
- Security implementations
- Monitoring solutions

## Requirements

- Each task includes a detailed diagram
- Diagrams are created using Mermaid syntax
- Comprehensive explanations of each component
- Analysis of potential issues and solutions
- Focus on best practices and industry standards

## Author
- Ayman Benchamkha

## Project Duration
- Start: November 28, 2024
- End: December 7, 2024

## Additional Resources

- [DNS Explained](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Load Balancing Concepts](https://www.nginx.com/resources/glossary/load-balancing/)
- [Web Server vs Application Server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [Database Management](https://www.oracle.com/database/what-is-database/)
- [Monitoring Best Practices](https://www.datadoghq.com/blog/monitoring-101-collecting-data/)

## Note
This project is part of the ALX System Engineering & DevOps curriculum. All diagrams and explanations must be original work. Plagiarism is strictly forbidden.