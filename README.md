# Smart Inventory System

## Overview
The Smart Inventory System is a Django-based web application designed to help businesses manage their inventory efficiently. It provides features for tracking stock levels, managing suppliers, automating reorder processes, and sending notifications via email. The system also leverages Celery for handling background tasks and Flower for monitoring Celery workers.

## Features
- **Real-time Inventory Tracking**: Monitor stock levels in real-time.
- **Supplier Management**: Keep track of suppliers and their contact information.
- **Automatic Reordering**: Automatically generate supply orders when stock levels fall below a specified threshold.
- **Email Notifications**: Send email notifications to suppliers and admins for low stock levels and new orders.
- **Background Tasks**:  Use Celery to handle time-consuming tasks (e.g., sending emails) asynchronously.
- **Task Monitoring**:  Use Flower to monitor Celery workers and tasks in real-time.
- **Reporting**:  Generate detailed reports on inventory status and transactions.
- **User Management**:  Role-based access control for different user types.
- **Notifications**:  Alerts for low stock levels and other important events.


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/snipher-marube/django-inventory-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-inventory-system
    ```
3. Create a virtual environment (optional but recommended)::
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. set up the environment variables:
    - Create a `.env` file in the root directory and the following variables.
    ```bash
    DJANGO_SECRET_KEY=your-secret-key
    DEBUG=True
    DB_NAME=inventory_db
    DB_USER=db_user
    DB_PASSWORD=db_password
    DB_HOST=localhost
    DB_PORT=5432
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    CELERY_BROKER_URL=redis://localhost:6379/0
    ```
6. Apply migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Access the application at `http://127.0.0.1:8000/`.
2. Log in with the superuser credentials.
3. Add products, suppliers, and manage inventory through the admin interface.

## Running Celery and Flower

1. Start Redis:
    Celery requires a message broker like Redis. Install Redis and start the server:
    - On Ubuntu:
        ```bash
        sudo apt update
        sudo apt install redis
        redis-server
        ```
    - On macOS:
        ```bash
        brew install redis
        brew services start redis
        ```
2. Start Celery worker:
    Run the Celery worker to process background tasks:  
    ```bash
    celery -A inventory_system worker --loglevel=info
    ```

3. Start Celery beat (optional):
    If you want to schedule periodic tasks, start Celery beat:
    ```bash
    celery -A inventory_system beat --loglevel=info
  ```

4. Start Flower for Monitoring:
    Flower is a web-based tool for monitoring Celery tasks. Start Flower:
    ```bash
    celery -A inventory_system flower
    ```
    Access Flower at `http://localhost:5555/`.

## Testing

### Admin Interface
1. Access the Django admin interface at `http://127.0.0.1:8000/admin/`.
2. Log in with the superuser credentials.
3. Add products, suppliers, and manage inventory through the admin interface.

### Automatic Reordering
- When a product's stock level falls below the specified threshold, the system will:
    1. Automatically generate a new order for the product.
    2. Send an email notification to the supplier.
    3. Create a notification for the admin.

## Email Notifications
- Email notifications are sent asynchronous using Celery.
- The email includes both plain text and HTML versions.

## Monitoring Tasks
- User Flower to monitor Celery workers and tasks in real-time.
- Access Flower `http://localhost:5555`.

## Contributing
Contributions are welcome! Please follow this steps.
    1. Fork repository.
    2. Create a new branch for your feature or bugfix:
        ```bash
        git checkout -b feature/your-feature-name
        ```
    3. commit your changes:
        ```bash
        git commit -m "Add your feature"
        ```
    4. Push to the branch:
        ```bash
        git push origin feature/your-feature-name
        ```
    5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, please contact [sniphermarube@gmail.com](mailto:sniphermarube@gmail.com).
