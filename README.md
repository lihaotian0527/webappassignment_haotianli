# webappassignment_haotianli

Selwyn Panel Beaters Web Application Report

## Project Report – Part 1

### Structure of the Solution

#### Routes & Functions

- `@app.route("/")`: Redirects to the `/currentjobs` page.
- `@app.route("/currentjobs")`: Displays the current jobs that are not completed.
- `@app.route("/addcustomer", methods=["GET", "POST"])`: Form to add a new customer to the system.
- `@app.route("/searchcustomer", methods=["GET", "POST"])`: Search for customers by name.

Each route is associated with a specific function that either renders a template or handles form submission.

#### Design Decisions

- **Assumptions**:
  - Assumed that the user interaction would be mostly form-based with minimal use of JavaScript for simplicity and ease of use.
  - Assumed that technicians are less likely to require access to customer addition or search functionality, hence these features are placed in the administrator interface.

- **Design Choices**:
  - Used Bootstrap to provide a consistent and responsive layout across various devices.
  - Chose to use Flask's built-in `redirect` and `url_for` functions for clean URL management and navigation.
  - Decided against adding JavaScript-heavy features to maintain ease of use for non-technical users.

### Project Report – Part 2

#### Database Questions

1. **SQL Statement for Job Table Creation**:
   The job table is created with the following SQL statement: `CREATE TABLE job (job_id INT PRIMARY KEY, ...);`

2. **Relationship Between Customer and Job Tables**:
   The foreign key constraint in the job table defines the relationship: `FOREIGN KEY (customer_id) REFERENCES customer(customer_id);`
