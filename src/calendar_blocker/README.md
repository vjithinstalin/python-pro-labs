# Google Calendar Blocker

Automatically block time on Google Calendar based on schedules defined in an Excel file.

**👤 Creator:** [vjithinstalin](https://github.com/vjithinstalin)

---

## 📝 Description

A Python utility that reads time blocking data from an Excel file and automatically creates calendar events in your Google Calendar. Perfect for scheduling focus time, meeting prep, breaks, recurring team meetings, and other activities that should prevent calendar conflicts.

## 🎯 Use Cases

- **Focus Time** - Block daily/weekly focus periods for deep work
- **Meeting Prep** - Pre-block time before important meetings
- **Lunch Breaks** - Schedule recurring lunch time blocks
- **Team Standup** - Automated team meeting time blocks
- **Admin Time** - Regular administrative task blocks
- **No Meeting Days** - Company-wide or personal no-meeting blocks

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+** installed
2. **Google Calendar API** credentials configured (see [OAUTH_SETUP.md](OAUTH_SETUP.md) for detailed instructions)
3. **Required Python packages** installed

### Installation

1. Install required packages:
```bash
pip install openpyxl google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dateutil
```

2. Set up Google Calendar API authentication:
   - Follow the step-by-step guide in [OAUTH_SETUP.md](OAUTH_SETUP.md)
   - You'll need to create a Google Cloud project and download credentials

3. Create your Excel file with calendar blocks (see format below)

4. Run the script:
```bash
# From calendar_blocker folder
python calendar_blocker_oauth.py schedule.xlsx

# From project root
python src/calendar_blocker/calendar_blocker_oauth.py schedule.xlsx
```

## 📋 Excel File Format

Your Excel file should have the following columns:

| Column | Required | Format | Example |
|--------|----------|--------|---------|
| **Date** | Yes | YYYY-MM-DD or MM/DD/YYYY | 2025-01-15 |
| **Start Time** | Yes | HH:MM (24-hour) | 09:00 |
| **End Time** | Yes | HH:MM (24-hour) | 10:30 |
| **Title** | Yes | Text (event name) | Focus Time |
| **Description** | No | Text | Deep work on project |
| **Recurring** | No | Daily, Weekly, Monthly, None | Weekly |
| **Color** | No | red, blue, green, etc. | blue |

### Example Excel Content

```
Date          | Start Time | End Time | Title          | Description           | Recurring | Color
2025-01-15    | 09:00      | 10:00   | Focus Time     | Deep work block       | Daily     | blue
2025-01-15    | 12:00      | 13:00   | Lunch          | Team lunch            | Weekly    | green
2025-01-15    | 14:00      | 14:30   | Meeting Prep   | Prepare slides        |           | yellow
2025-01-15    | 15:00      | 16:00   | Admin Time     | Email & admin tasks   | Daily     | orange
```

## 🎨 Supported Colors

- red
- orange
- yellow
- green
- blue
- purple
- gray
- none

## 🔄 Recurring Options

- **None** - One-time event (default)
- **Daily** - Every day
- **Weekly** - Every week on the same day
- **Monthly** - Every month on the same date

## 📊 Example Usage

### Example 1: Weekly Focus Time
```
Date: 2025-01-20
Start Time: 09:00
End Time: 10:00
Title: Focus Time
Recurring: Weekly
Color: blue
```
Creates a recurring event every Monday from 9:00-10:00 AM (assuming the date is a Monday)

### Example 2: One-Time Meeting Prep
```
Date: 2025-02-01
Start Time: 14:00
End Time: 14:30
Title: Meeting Prep
Description: Prepare Q1 review presentation
Color: yellow
```
Creates a single event on Feb 1 from 2:00-2:30 PM

### Example 3: Daily Lunch Block
```
Date: 2025-01-15
Start Time: 12:00
End Time: 13:00
Title: Lunch Break
Recurring: Daily
Color: green
```
Creates a daily recurring lunch block starting Jan 15

## 💡 Learning Concepts

This project demonstrates:

### 1. **Excel File Processing**
   - Using openpyxl to parse Excel files
   - Reading headers and rows
   - Handling different cell types and data validation

### 2. **Google Calendar API Integration**
   - OAuth 2.0 authentication flow
   - Creating calendar events programmatically
   - Setting event properties (color, time, recurrence)
   - API request/response handling

### 3. **Date/Time Handling**
   - Parsing multiple date formats
   - Time string validation and conversion
   - Creating ISO 8601 formatted timestamps
   - Timezone management

### 4. **Error Handling & Logging**
   - Structured logging for debugging
   - Input validation and error reporting
   - Graceful failure handling
   - Success/failure tracking

## 🔧 Advanced Features

### Custom Timezone
Modify the timezone in the script (currently set to `America/New_York`):
```python
'timeZone': 'America/Los_Angeles',  # Change as needed
```

### Batch Import
Process multiple Excel files:
```python
for file in ['schedule1.xlsx', 'schedule2.xlsx']:
    block_calendar(file)
```

### Error Recovery
The script logs all errors and continues processing remaining events.

## 🐛 Troubleshooting

### Issue: Authentication errors
**Solution:** Follow the setup guide in [OAUTH_SETUP.md](OAUTH_SETUP.md)

### Issue: `openpyxl not installed`
**Solution:** Run `pip install openpyxl`

### Issue: `Date format error`
**Solution:** Ensure dates are in YYYY-MM-DD or MM/DD/YYYY format

### Issue: `Time format error`
**Solution:** Ensure times are in HH:MM format (24-hour), e.g., 14:30 for 2:30 PM

### Issue: Events not appearing
**Solution:** Verify authentication and permissions - see [OAUTH_SETUP.md](OAUTH_SETUP.md)

## 📊 Output Example

```
============================================================
Calendar Blocking Complete
============================================================
Successfully created: 8 events
Failed: 0 events
============================================================
```

## 🔗 Required Libraries

```
openpyxl              # Excel file reading
google-auth-oauthlib  # Google authentication
google-api-python-client # Google Calendar API
python-dateutil       # Date parsing
```

Install all at once:
```bash
pip install openpyxl google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dateutil
```

## 📚 Resources

- [Google Calendar API Documentation](https://developers.google.com/calendar)
- [openpyxl Documentation](https://openpyxl.readthedocs.io/)
- [python-dateutil Documentation](https://dateutil.readthedocs.io/)

## ⚠️ Important Notes

- **Authentication:** This project uses OAuth 2.0 for secure access to your Google Calendar
- **Timezone:** Currently set to `America/New_York`. Adjust in the script as needed.
- **Date Format:** Supports YYYY-MM-DD and MM/DD/YYYY formats
- **Time Format:** Must be in 24-hour format (HH:MM)
- **Privacy:** Events are created as opaque (block time from others)
- **Setup:** Detailed authentication setup instructions are in [OAUTH_SETUP.md](OAUTH_SETUP.md)

## 🔗 Related Projects

- `../hello_world/` - Basic Python concepts
- `../calculator/` - Functions and error handling
- `../file_organizer/` - File I/O operations
