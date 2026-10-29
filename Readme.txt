LITTLE LEMON WEB APPLICATION

Project: Little Lemon Django REST Framework Capstone

Requirements:
- Django and Django REST Framework
- MySQL database
- Insomnia REST client

API endpoints:

1. Home page
   GET /restaurant/

2. Menu items
   GET /restaurant/api/menu-items/
   POST /restaurant/api/menu-items/

3. Individual menu item
   GET /restaurant/api/menu-items/2/
   PUT /restaurant/api/menu-items/2/
   DELETE /restaurant/api/menu-items/2/

4. Table bookings
   GET /restaurant/api/bookings/
   POST /restaurant/api/bookings/

5. User registration
   POST /auth/users/

6. Authentication token
   POST /auth/token/login/

7. Protected message
   GET /restaurant/api/message/

Authentication:
Register a user and obtain an authentication token. For protected endpoints, send the request header:

Authorization: Token YOUR_AUTH_TOKEN

Replace example IDs with IDs that exist in the database. Protected endpoints require authentication.

Unit tests:
python manage.py test restaurant

Note:
Use POST for registration and token creation. The API is intended to be tested using Insomnia.