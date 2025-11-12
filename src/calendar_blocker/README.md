# Google Calendar Blocker

Automatically block time on Google Calendar based on schedules defined in an Excel file.

**👤 Creator:** [vjithinstalin](https://github.com/vjithinstalin)

---

## 📝 Description

A utility that reads time blocking data from an Excel file and automatically creates blocked time events in Google Calendar. This is perfect for scheduling focus time, meeting prep, breaks, and other activities that should prevent calendar conflicts.

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
2. **Google Calendar API** credentials set up
3. **Required Python packages** installed

### Installation

1. Install required packages:
```bash
pip install openpyxl google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dateutil
```

2. Set up Google Calendar API:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable Google Calendar API
   - Create service account credentials
   - Download credentials as `credentials.json`
   - Place `credentials.json` in the `calendar_blocker` folder

3. Create your Excel file with calendar blocks (see format below)

4. Run the script:
```bash
# From calendar_blocker folder
python calendar_blocker.py schedule.xlsx

# From project root
python src/calendar_blocker/calendar_blocker.py schedule.xlsx
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

This project teaches:

### 1. **Excel File Reading**
   - Using openpyxl to parse Excel files
   - Reading headers and rows
   - Handling different cell types

### 2. **Google Calendar API**
   - OAuth 2.0 authentication
   - Service account credentials
   - Creating calendar events
   - Setting event properties (color, time, recurrence)

### 3. **Data Validation**
   - Validating date formats
   - Validating time formats
   - Required field checking
   - Error reporting

### 4. **Date/Time Handling**
   - Parsing various date formats
   - Time string validation
   - Creating ISO 8601 formatted timestamps
   - Timezone handling

### 5. **API Integration**
   - Building API requests
   - Handling API responses
   - Error handling for API calls
   - Batch operations

### 6. **Logging & Error Handling**
   - Structured logging
   - Error messages and warnings
   - Tracking success/failure
   - Reporting results

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

### Issue: `credentials.json not found`
**Solution:** Follow the Google Calendar API setup steps in the Quick Start section.

### Issue: `openpyxl not installed`
**Solution:** Run `pip install openpyxl`

### Issue: `Date format error`
**Solution:** Ensure dates are in YYYY-MM-DD or MM/DD/YYYY format

### Issue: `Time format error`
**Solution:** Ensure times are in HH:MM format (24-hour), e.g., 14:30 for 2:30 PM

### Issue: Events not appearing
**Solution:** Check calendar permissions on the service account in Google Calendar settings

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

- **Timezone:** Currently set to `America/New_York`. Adjust as needed.
- **Permissions:** Service account needs read/write access to your calendar
- **Date Format:** Supports YYYY-MM-DD and MM/DD/YYYY formats
- **Time Format:** Must be in 24-hour format (HH:MM)
- **Blocking:** Events are created as opaque (block time from others)

## 🔗 Related Projects

- `../hello_world/` - Basic Python concepts
- `../calculator/` - Functions and error handling
- `../file_organizer/` - File I/O operations
