# LangChain Learning Projects

A collection of LangChain notebooks and five small Streamlit apps covering chat, prompt chains, web search, weather, email, and task management.

## Projects

| Project | What it does | Required credentials |
| --- | --- | --- |
| `projects/001_QNA_BOT` | Streamlit Q&A chat using Groq | `GROQ_API_KEY` |
| `projects/002_Blog_bot` | Generates a blog outline, draft, and polished version | `GROQ_API_KEY`, `MODEL` |
| `projects/003_weather+Search_Agent` | Searches the web with Nimble and retrieves current weather from OpenWeatherMap | `GROQ_API_KEY`, `NIMBLE_API_KEY`, `OPENWEATHERMAP_API_KEY` |
| `projects/004_email_agent` | Drafts and sends email through Gmail SMTP | `GROQ_API_KEY`, `MODEL`, `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD` |
| `projects/005_task_agent` | Manages todos stored in a local SQLite database | `OPENROUTER_API_KEY` |

`basic_langchain.ipynb` and `core_langchain.ipynb` are learning notebooks. The core notebook defaults to Groq and also has OpenRouter examples. `PROVIDER` and `MODEL` can be set in `.env` for cells that use `init_chat_model`.

## Setup

Use Python 3.10 or later. From the repository root, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `.env` and fill in only the credentials for the apps you plan to run. `.env` is excluded by `.gitignore`; keep it private and never commit real keys. `.env.example` contains placeholders only.

## Get API Credentials

Create only the credentials your chosen project needs:

1. **Groq** (`GROQ_API_KEY`): sign in to the [Groq Console](https://console.groq.com/keys), create an API key, and paste it into `.env`. Used by the Q&A, blog, weather/search, and email projects.
2. **OpenRouter** (`OPENROUTER_API_KEY`): sign in to [OpenRouter](https://openrouter.ai/settings/keys), create a key, and paste it into `.env`. Used by the task agent and OpenRouter notebook examples.
3. **Nimble** (`NIMBLE_API_KEY`): create/sign in to a [Nimbleway account](https://nimbleway.com/) and create an API key in its account dashboard. The LangChain integration reads this variable for web search.
4. **OpenWeatherMap** (`OPENWEATHERMAP_API_KEY`): create/sign in to [OpenWeather](https://home.openweathermap.org/users/sign_up), then create or copy a key from [API keys](https://home.openweathermap.org/api_keys). The weather tool uses the Current Weather API; a new key may take a short time to become active.
5. **Gmail** (`GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`): use the Gmail address that will send mail. In that Google Account, enable 2-Step Verification, then create an App Password at [Google App Passwords](https://myaccount.google.com/apppasswords). Put the 16-character app password in `GMAIL_APP_PASSWORD` (spaces removed), not your normal Google password. App Passwords may be unavailable for some managed Workspace accounts or accounts with Advanced Protection.

Never paste API keys or passwords into chat, source code, notebooks, screenshots, or commits. If a key is exposed, revoke it in its provider dashboard and create a replacement.

## Run an App

Run commands from the repository root with the virtual environment active:

```powershell
streamlit run projects/001_QNA_BOT/app.py
streamlit run projects/002_Blog_bot/app.py
streamlit run "projects/003_weather+Search_Agent/app.py"
streamlit run projects/004_email_agent/app.py
cd projects/005_task_agent #due to sqlite db creation in workspace
streamlit run app.py
```

Each command starts one app; open the local URL printed by Streamlit. The task agent creates `todos.db` in the working directory when it first runs.

## Configuration

The sample `MODEL` value is `openai/gpt-oss-20b`, matching the model already used by the Groq projects. The blog and email agents read `MODEL`; the Q&A and weather/search agents currently specify that model in code. For notebook cells using `init_chat_model`, `PROVIDER` defaults to `groq` and can be changed to a provider supported by LangChain when the matching credentials and package are installed.

If an app reports a missing credential, check that the variable is set in `.env`, that the key is active, and that Streamlit was started from the repository root. For Gmail, confirm 2-Step Verification and SMTP access are enabled for the sending account.