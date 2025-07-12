# Nutrient and Calorie Tracker

A web application built with Django that allows users to track their daily food consumption, monitor macronutrients (carbohydrates, protein, fats), and calories. The app provides a simple interface to add foods, view consumption history, and visualize nutritional breakdowns.

## Features
- User authentication (via Django's built-in User model)
- Add foods with nutritional information (carbs, protein, fats, calories)
- Log daily food consumption
- View a table of consumed foods with nutritional breakdown
- Remove consumed food entries
- Visualize macronutrient breakdown with charts
- Calorie progress bar towards a daily goal (default: 2000 kcal)
- Admin interface for managing foods and consumption records

## Screenshots
*Add your screenshots here*

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd nutrientandcalorietracker
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install Django==5.1.4 djangorestframework
   ```
   Or, to install all packages (if you want to match the dev environment):
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   - Main app: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Usage
- Log in with your user account.
- Add foods to the database via the admin panel or directly in the database.
- Use the main page to log foods you have consumed.
- View your daily nutritional breakdown and calorie progress.
- Remove items as needed.

## Project Structure
```
nutrientandcalorietracker/
├── main/                # Main Django app
│   ├── models.py        # Food and Consumption models
│   ├── views.py         # Views for logging and deleting consumption
│   ├── templates/       # HTML templates
│   └── ...
├── nutrientandcalorietracker/ # Project settings and URLs
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── db.sqlite3           # SQLite database (auto-generated)
```

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/) 