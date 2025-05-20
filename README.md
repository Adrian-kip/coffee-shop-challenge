Project Overview
This project implements a coffee shop management system using Python classes to model customers, coffee items, and orders. The system enforces strict validation rules and maintains relationships between objects while providing aggregate data analysis.

Key Components
1. Customer Class

Validates customer names (must be strings between 1-15 characters)

Tracks all orders placed by the customer

Provides a list of unique coffees ordered

2. Coffee Class

Validates coffee names (must be strings of at least 3 characters)

Enforces immutability of coffee names after creation

Calculates order statistics including total orders and average price

3. Order Class

Links customers to coffee items with validated pricing (must be float between 1.0-10.0)

Maintains immutability of order price after creation

Provides access to related customer and coffee objects

Bonus Feature
The most_aficionado class method identifies which customer has spent the most on a specific coffee item, returning None if no orders exist.

Implementation Details
Validation and Relationships

All classes enforce strict type and value validation

Order objects maintain bidirectional relationships with both Customer and Coffee objects

Methods return proper unique collections where required

Circular Import Solution
The project handles circular dependencies between classes by using class name checking instead of direct type checking, while maintaining all validation requirements.

Testing
The test suite verifies:

Proper validation of all attributes

Correct relationship maintenance

Accurate aggregate calculations

Edge case handling

To run tests:

bash

pytest

This implementation meets all specified requirements and demonstrates proper object-oriented design principles. The code is structured for clarity while maintaining strict data integrity.