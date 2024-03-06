# Amazon Offers Scraper

This project consists of a system that performs web scraping to obtain daily offers from Amazon and then loads them into a database. The frontend is developed in Angular and the backend in FastAPI.

## Features

- **Web Scraping**: Utilizes web scraping techniques to extract daily offers from Amazon.
- **Database**: Stores the obtained offers in a database for later querying.
- **Frontend**: Displays daily offers from Amazon in an intuitive and easy-to-navigate manner

## Technologies Used

- **Frontend**:
  - Angular: Frontend development framework based on TypeScript.
  - HTML/CSS: Standard languages for creating web interfaces.

- **Backend**:
  - FastAPI: Modern, fast web framework for building APIs with Python.
  - BeautifulSoup: Python library for extracting information from web pages.
  - SQLAlchemy: Python library for interacting with relational databases.

## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the `frontend` folder and run `npm install` to install frontend dependencies.
3. Navigate to the `backend` folder and create a virtual environment. Then, run `pip install -r requirements.txt` to install backend dependencies.
4. Configure the necessary environment variables for database connection and other relevant parameters.
5. Start the frontend and backend by executing the appropriate commands.

## Contribution

Contributions are welcome! If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them with descriptive messages.
4. Push the branch (`git push origin feature/new-feature`).
5. Open a Pull Request and describe your changes in detail.

## License

This project is licensed under the Apache License. Please see the `LICENSE` file for more details.
