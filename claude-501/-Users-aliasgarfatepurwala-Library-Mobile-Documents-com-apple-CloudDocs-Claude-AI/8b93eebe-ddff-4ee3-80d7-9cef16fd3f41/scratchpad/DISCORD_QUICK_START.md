# Discord OAuth 2.0 - 5 Minute Credential Setup

## Account Details ✅
- **Email**: gendawala1024@gmail.com  
- **Password**: Kp9#mL2@xR$vQ5w8

## Quick Steps

### 1. Go to Developer Portal
https://discord.com/developers/applications → Click "Log In"

### 2. Create App
- Click **New Application**
- Name: `Trading OS`
- Click Create

### 3. Get CLIENT ID
- Left sidebar → General Information
- Copy **CLIENT ID** value

### 4. Get CLIENT SECRET  
- Same page → Click **Reset Secret** below CLIENT ID
- Confirm → Copy new secret

### 5. Add OAuth Redirect
- Left sidebar → OAuth2 → General
- Add Redirect: `http://localhost:5173/`
- Save

### 6. Update .env.local
```bash
VITE_DISCORD_CLIENT_ID=<your-client-id>
DISCORD_CLIENT_SECRET=<your-client-secret>
```

**That's it!** 5 minutes and you're done.

---

## Why Manual?
Discord's CAPTCHA and MFA blocked automated creation. Manual takes 5 min (faster than automation workarounds).

## All Code Already Ready
- ✅ Frontend components built
- ✅ OAuth flow implemented  
- ✅ Token storage configured
- ✅ Database schema ready

**Just add the 2 credentials above to .env.local and go!**

