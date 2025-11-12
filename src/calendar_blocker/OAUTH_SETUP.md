# OAuth 2.0 Setup Guide for Calendar Blocker

**This is the EASIER alternative that uses your personal Google account login.**

## Quick Setup (5 minutes)

### Step 1: Create OAuth 2.0 Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Make sure your **"Python Calendar Blocker"** project is selected
3. Go to **"APIs & Services" > "Credentials"**
4. Click **"Create Credentials"** at the top
5. Select **"OAuth 2.0 Client ID"**
6. When asked for application type, select **"Desktop application"**
7. Click **"Create"**
8. Click the download button (looks like a down arrow) next to the credential
9. A file will download called something like `client_secret_xxxxxxx.json`

### Step 2: Save the File

1. Rename the downloaded file to: `client_secret.json`
2. Move it to: `c:\Users\jithinstalin\Projects\python-pro-labs\src\calendar_blocker\`
3. Your folder should now have:
   - `calendar_blocker_oauth.py`
   - `client_secret.json` (the file you just added)
   - `test.xlsx`

### Step 3: Run the Script

```bash
cd c:\Users\jithinstalin\Projects\python-pro-labs\src\calendar_blocker\
python calendar_blocker_oauth.py test.xlsx
```

### Step 4: Login When Prompted

1. A **browser window will open automatically**
2. **Login with your Google account** (the one you use for Calendar)
3. Click **"Allow"** when asked for permissions
4. The browser will show "The authentication flow has completed"
5. Close the browser tab - you're done!

### Step 5: Verify

Check your Google Calendar - the events should now appear! 🎉

---

## How It Works

- **First run:** Opens your browser for login, saves a token (`token.pickle`)
- **Subsequent runs:** Uses the saved token (no login needed)
- **Your account:** Uses your personal Google account, not a service account
- **More reliable:** Works with personal Google accounts without special configuration

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "client_secret.json not found" | Download it from Google Cloud Console and save in calendar_blocker folder |
| Browser doesn't open | Check your firewall/antivirus - it may be blocking the login |
| "Invalid client" error | Make sure client_secret.json is valid and hasn't been edited |
| Events still not appearing | Check your Google Calendar is selected in the permissions |

---

## Files Created

- `calendar_blocker_oauth.py` - The main OAuth version (USE THIS)
- `client_secret.json` - Your OAuth credentials (keep this safe!)
- `token.pickle` - Your login token (created after first login)

---

**Note:** Use `calendar_blocker_oauth.py` instead of `calendar_blocker.py` for this method.
