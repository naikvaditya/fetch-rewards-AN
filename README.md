# fetch-rewards-AN

#### Note: A simplified version of the code is available in app.py however, I recommend using main.py as it takes care of all exceptions and is more structured.

## Overview
**This file has 3 sections:**
- I. Steps to run the program
- II. Answers to the questions asked
- II. Next steps

## I. Steps to run the program
Follow these steps to run the application:

1. **Prepare Environment:**
  - Ensure Python 3.x is installed on your system.

2. **Install Dependencies:**
  - Open a terminal or command prompt.
  - Navigate to the directory containing your project files.
  - Run the following command to install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the docker containers**
- Run the following command to start the docker containers for postgreSQL and localstack:
  ```bash
    docker compose up
    ```

4. **Run the Application:**
  - In the terminal or command prompt, navigate to your project directory.
  - Execute the following command to start the application:
    ```bash
    python main.py
    ```

5. **Monitor Application Logs:**
  - Monitor the terminal or command prompt for application logs.
  - Check for any errors or exceptions during application execution.

6. **Verify Database Updates:**
  - After running the application, verify that new records are inserted into the `user_logins` table in your PostgreSQL database.

## II. Questions

### 1. How would you deploy this application in production?

To deploy this application in production, follow these steps:

- **Prepare Environment:**
    - Ensure you have a production-ready PostgreSQL database set up with appropriate schema (`user_logins` table).
    - Securely manage database credentials and connection details.
    - Set up AWS SQS or another message queue service in your production environment.

- **Package Application:**
    - Package your Python application along with its dependencies into a distributable format (e.g., using `pip` and `requirements.txt`).

- **Deployment Steps:**
    - Deploy the packaged application to your production server(s).
    - Configure environment variables or a configuration file (`config.json`) containing production-specific settings (database credentials, SQS queue URLs, etc.).

- **Run and Monitor:**
    - Start the application process, ensuring it runs as a daemon or service.
    - Monitor logs for any errors or exceptions.
    - Implement logging and monitoring to track application performance and health.

### 2. What other components would you want to add to make this production ready?

To make this application production-ready, consider adding:

- **Error Handling and Logging:**
    - Enhance error handling to gracefully manage database connection failures, SQS message retrieval issues, and JSON parsing errors.
    - Implement comprehensive logging to track application activities and errors.

- **Security Measures:**
    - Securely manage credentials and sensitive information (e.g., using environment variables or encrypted configuration files).
    - Implement data encryption for sensitive fields, especially PII.

- **Performance Optimization:**
    - Optimize database queries (e.g., indexing) for efficient data retrieval and insertion.
    - Implement caching mechanisms if applicable.

- **Fault Tolerance and Scalability:**
    - Implement retry mechanisms for SQS message retrieval and database operations to handle transient failures.
    - Consider using a message queue service with scalability features (e.g., AWS SQS scaling capabilities).

### 3. How can this application scale with a growing dataset.

To scale the application as the dataset grows:

- **Database Scaling:**
    - Vertical Scaling: Increase database server resources (CPU, RAM) if possible.
    - Horizontal Scaling: Consider database sharding or replication to distribute load.

- **Message Queue Scaling:**
    - Utilize message queue service scaling capabilities (e.g., AWS SQS auto-scaling) to handle increased message throughput.

- **Application Scaling:**
    - Deploy multiple instances of the application behind a load balancer to distribute message processing load.
    - Ensure each instance can handle concurrent database connections and SQS message retrieval.

### How can PII be recovered later on?

If you need to recover PII (Personally Identifiable Information) later on, consider the following:

- **Backup and Recovery Strategy:**
    - Regularly backup encrypted PII data in your database.
    - Ensure backups are securely stored and accessible only to authorized personnel.
    - Implement data retention policies and comply with relevant data protection regulations (e.g., GDPR).

- **Encryption Key Management:**
    - Manage encryption keys securely to ensure you can decrypt PII data when needed for recovery purposes.

### What are the assumptions you made?

In developing this application, some assumptions include:

- **Environment Setup:** Assumes access to `awslocal` and `psycopg2` libraries for AWS SQS and PostgreSQL interactions respectively.

## III. Next Steps

If more time were available, here are ways to further enhance the project:

- **Error Handling:** Implement robust error handling and logging throughout the application to handle various failure scenarios gracefully.
  
- **Testing:** Develop unit tests for functions in `message_processing.py` and integration tests for database interactions to ensure reliability.
  
- **Performance Optimization:** Optimize SQL queries, consider batching database operations, and tune configurations for better performance with large message volumes.
  
- **Security Enhancements:** Securely manage sensitive information such as database credentials and SQS access keys. Consider encryption and access control measures.
  
- **Scaling:** Implement mechanisms for horizontal scaling, such as using AWS SQS features like message visibility timeout and batch processing.

These steps will improve the reliability, performance, and security of the application, ensuring it meets the demands of production environments effectively.