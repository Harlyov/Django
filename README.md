# Documentation

## Project Overview

The goal of this project is to develop a Django web application for managing football-related data for Real Madrid.

The system allows users to manage:

- Players  
- Matches  
- Fans  
- Match Comments  

The application demonstrates relational database design, form validation, full CRUD functionality, template inheritance, and clean architecture using Django best practices.

Authentication and user management are intentionally excluded as per project requirements.


## Contents

- Project Setup  
- Database Architecture  
- Key Components  
- Models  
- Forms & Validation  
- Views  
- Templates  
- Relationships  
- Design Decisions

## Project Setup

The project is built using:

- Django 6.0.1  
- PostgreSQL  
- Bootstrap 5  

It follows a modular architecture with separate Django apps:

- players
- matches
- fans
- comments
- common

Each app has a clearly defined responsibility.


## Database Architecture

The project includes multiple database models with properly defined relationships.

### Many-to-One Relationships

- A **Fan** has one favourite **Player**.
- A **Comment** belongs to one **Match**.
- A **Comment** belongs to one **Fan**.

### Many-to-Many Relationship

- A **Match** can include multiple **Players**.
- A **Player** can participate in multiple **Matches**.

This ensures proper relational structure and data consistency.


## Design Decisions

### Modular Architecture

Each functional domain (players, matches, fans, comments) is implemented as a separate Django app.

This ensures:

- Strong cohesion  
- Loose coupling  
- Better maintainability  
- Easier testing  
