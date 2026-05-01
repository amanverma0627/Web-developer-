# AI Health Chatbot & Assistant for Kinjal Ji

A comprehensive Python-based AI chatbot designed to assist with personal health issues and wellness support.

## Features

✅ **Symptom Checker** - Identify potential health conditions based on symptoms
✅ **Health Tips** - Get personalized wellness recommendations
✅ **Medicine Reminder** - Set and track medication schedules
✅ **Appointment Scheduling** - Book health appointments
✅ **Emergency Hotline Links** - Quick access to emergency services
✅ **General Wellness** - Daily health tips and guidance

## Tech Stack

- **Backend**: Python with Flask
- **Database**: SQLite (easily upgradeable to PostgreSQL)
- **API Integration**: Multiple health and wellness APIs
- **NLP**: NLTK for natural language processing

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Setup environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. Run the application:
   ```bash
   python app.py
   ```

## Project Structure

```
health-chatbot/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── models/
│   ├── user.py        # User model
│   ├── appointment.py # Appointment model
│   └── medicine.py    # Medicine reminder model
├── routes/
│   ├── chat.py        # Chat routes
│   ├── symptoms.py    # Symptom checker routes
│   ├── appointments.py # Appointment management
│   └── health_tips.py # Health tips routes
├── services/
│   ├── nlp_service.py      # NLP processing
│   ├── symptom_checker.py  # Symptom analysis
│   ├── health_api_client.py # API integrations
│   └── reminder_service.py  # Medicine reminders
├── templates/
│   └── index.html     # Web interface
└── static/
    ├── css/
    └── js/
```

## API Features

### 1. Symptom Checker
```bash
POST /api/symptoms/check
{
  "symptoms": ["fever", "cough", "fatigue"]
}
```

### 2. Medicine Reminder
```bash
POST /api/reminders/add
{
  "medicine_name": "Aspirin",
  "dosage": "500mg",
  "frequency": "twice daily",
  "time": "08:00, 20:00"
}
```

### 3. Appointment Scheduling
```bash
POST /api/appointments/schedule
{
  "doctor_specialty": "Cardiology",
  "preferred_date": "2026-05-10",
  "reason": "Checkup"
}
```

### 4. Health Tips
```bash
GET /api/health-tips?category=wellness
```

### 5. Emergency Hotlines
```bash
GET /api/emergency/hotlines
```

## Environment Setup

Create a `.env` file with:
- `HEALTH_API_KEY`: API key for health data services
- `DATABASE_URL`: Database connection string
- `FLASK_ENV`: Environment (development/production)

## Contributing

1. Create a feature branch
2. Commit your changes
3. Push to the branch
4. Create a Pull Request

## License

MIT License - feel free to use for personal and commercial projects

## Support

For issues or questions, please create an issue in the repository.

---
Built with ❤️ for health and wellness assistance
