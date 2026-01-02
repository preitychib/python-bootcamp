# Doctor Appointment System API

## 🚀 Quick Start with Docker

1. **Prerequisites**
   - Docker and Docker Compose installed
   - Git (for cloning the repository)

2. **Setup**
   ```bash
   # Clone the repository
   git clone https://github.com/preitychib/python-bootcamp.git
   cd week-5
   
   # Copy environment variables
   cp .env.example .env
   
   # Start the services
   docker-compose up -d

   # View logs
   docker-compose logs -f
   
   # Stop services
   docker-compose down
   
   # Test case execution
   # run this first to collect all the test cases
   pytest --collect-only
   
   # run actual tests
   pytest



## Authentication Flow and RBAC Design

### Authentication Flow

- Authentication is implemented using JWT (JSON Web Tokens).
- Users log in using:
```text
POST api/v1/auth/login
```
- On successful authentication, an access token is returned.
- The token must be sent with every protected request:
```http
Authorization: Bearer <access_token>
```
- The JWT token contains the user identity and role.

---


### RBAC (Role-Based Access Control)

The system supports:
- Doctor
- Patient
- Admin

RBAC is enforced at multiple levels:

1. **Token Level**
   - User role is embedded inside the JWT token.

2. **API Level**
   - FastAPI dependencies restrict endpoint access based on roles.

3. **Business Logic Level**
   - Domain-level checks ensure:
     - Only doctors can add availability.
     - Only patients can book appointments.
     - Invalid role actions are rejected.
