![Image](https://github.com/user-attachments/assets/f19fbf51-36aa-46ce-9479-f1b08c07b869)
## Setup
### Backend Setup
#### 1. API Key
Register a TMDB API key and put it inside the `API_KEY` variable in server.py
#### 2. Running
Run `python server.py` after installing Python packages:
```bash
pip install requests Flask flask_cors
```
### Frontend Setup
#### 1. Hosting
Find a hosting provider that allows this type of content to be uploaded to their servers and host it there or selfhost it on your own computer using Cloudflare Tunnels.
#### 2. Setup
Edit all `http://localhost:5000` URLs in the .html files to point to your own backend site and you are good to use Notflix.
