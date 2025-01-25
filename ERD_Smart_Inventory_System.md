# Entity-Relationship Diagram (ERD) for Smart Inventory System

## Tables

### 1. Supplier
| Column Name   | Data Type       | Constraints               | Description                          |
|---------------|-----------------|---------------------------|--------------------------------------|
| `id`          | `PrimaryKey`    | `AutoField`               | Unique identifier for the supplier.  |
| `name`        | `CharField`     | `max_length=255`          | Name of the supplier.                |
| `email`       | `EmailField`    | `unique=True`             | Email address of the supplier.       |
| `phone`       | `CharField`     | `max_length=15`           | Phone number of the supplier.        |
| `address`     | `TextField`     |                           | Address of the supplier.             |
| `created_at`  | `DateTimeField` | `auto_now_add=True`       | Timestamp when the supplier was added. |

---

### 2. Product
| Column Name   | Data Type       | Constraints               | Description                          |
|---------------|-----------------|---------------------------|--------------------------------------|
| `id`          | `PrimaryKey`    | `AutoField`               | Unique identifier for the product.   |
| `name`        | `CharField`     | `max_length=255`          | Name of the product.                 |
| `description` | `TextField`     |                           | Description of the product.          |
| `quantity`    | `PositiveIntegerField` | `default=0`       | Current stock quantity of the product. |
| `threshold`   | `PositiveIntegerField` | `default=10`      | Minimum stock level before reordering. |
| `supplier_id` | `ForeignKey`    | `to=Supplier, on_delete=CASCADE` | Reference to the supplier. |
| `created_at`  | `DateTimeField` | `auto_now_add=True`       | Timestamp when the product was added. |

---

### 3. Order
| Column Name   | Data Type       | Constraints               | Description                          |
|---------------|-----------------|---------------------------|--------------------------------------|
| `id`          | `PrimaryKey`    | `AutoField`               | Unique identifier for the order.     |
| `product_id`  | `ForeignKey`    | `to=Product, on_delete=CASCADE` | Reference to the product.     |
| `quantity`    | `PositiveIntegerField` |                       | Quantity of the product to order.    |
| `supplier_id` | `ForeignKey`    | `to=Supplier, on_delete=CASCADE` | Reference to the supplier.    |
| `is_completed`| `BooleanField`  | `default=False`           | Whether the order is completed.      |
| `created_at`  | `DateTimeField` | `auto_now_add=True`       | Timestamp when the order was created. |

---

### 4. Notification
| Column Name   | Data Type       | Constraints               | Description                          |
|---------------|-----------------|---------------------------|--------------------------------------|
| `id`          | `PrimaryKey`    | `AutoField`               | Unique identifier for the notification. |
| `user_id`     | `ForeignKey`    | `to=User, on_delete=CASCADE` | Reference to the user (admin or supplier). |
| `message`     | `TextField`     |                           | Notification message.                |
| `is_read`     | `BooleanField`  | `default=False`           | Whether the notification is read.    |
| `created_at`  | `DateTimeField` | `auto_now_add=True`       | Timestamp when the notification was created. |

---

### 5. User (Django's Default User Model)
| Column Name   | Data Type       | Constraints               | Description                          |
|---------------|-----------------|---------------------------|--------------------------------------|
| `id`          | `PrimaryKey`    | `AutoField`               | Unique identifier for the user.      |
| `username`    | `CharField`     | `unique=True`             | Username for login.                  |
| `email`       | `EmailField`    |                           | Email address of the user.           |
| `password`    | `CharField`     |                           | Hashed password for authentication.  |
| `is_staff`    | `BooleanField`  | `default=False`           | Whether the user is an admin.        |
| `is_active`   | `BooleanField`  | `default=True`            | Whether the user account is active.  |

---

## Relationships

1. **Supplier → Product**:  
   - A supplier can supply multiple products.  
   - Relationship: `One-to-Many` (1 Supplier → Many Products).

2. **Product → Order**:  
   - A product can have multiple orders.  
   - Relationship: `One-to-Many` (1 Product → Many Orders).

3. **Supplier → Order**:  
   - A supplier can have multiple orders.  
   - Relationship: `One-to-Many` (1 Supplier → Many Orders).

4. **User → Notification**:  
   - A user (admin or supplier) can have multiple notifications.  
   - Relationship: `One-to-Many` (1 User → Many Notifications).

---

## ERD Diagram (Text Representation)

Supplier
|-- id (PrimaryKey)
|-- name (CharField)
|-- email (EmailField)
|-- phone (CharField)
|-- address (TextField)
|-- created_at (DateTimeField)

Product
|-- id (PrimaryKey)
|-- name (CharField)
|-- description (TextField)
|-- quantity (PositiveIntegerField)
|-- threshold (PositiveIntegerField)
|-- supplier_id (ForeignKey to Supplier)
|-- created_at (DateTimeField)

Order
|-- id (PrimaryKey)
|-- product_id (ForeignKey to Product)
|-- quantity (PositiveIntegerField)
|-- supplier_id (ForeignKey to Supplier)
|-- is_completed (BooleanField)
|-- created_at (DateTimeField)

Notification
|-- id (PrimaryKey)
|-- user_id (ForeignKey to User)
|-- message (TextField)
|-- is_read (BooleanField)
|-- created_at (DateTimeField)

User (Django's Default User Model)
|-- id (PrimaryKey)
|-- username (CharField)
|-- email (EmailField)
|-- password (CharField)
|-- is_staff (BooleanField)
|-- is_active (BooleanField)
