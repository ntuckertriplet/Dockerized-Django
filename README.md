# Dockerized Django

For my security class, we were given a few virtual machines to secure and defend. One of them had a vulnerable-by-design Flask application, which we were required to fix up as best we could. It was found that auditing the code would be more work than starting from the ground up, and to further the security as well as portability, I used docker-compose to contianerize the application as well as NGINX and PostgreSQL

## Installation and Setup
* Clone this repository
* `docker-compose up -d --build`
