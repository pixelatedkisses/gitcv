# GitCV

A full-stack web application that dynamically bridges GitHub's GraphQL API and Overleaf's LaTeX compilation engine. GitCV automates the generation of a professional, typeset curriculum vitae by extracting a user's repository data, processing it through an LLM for professional phrasing, and injecting it into a parameterized TeX template.

## System Architecture & Data Flow

1. **Authentication:** OAuth 2.0 flow via GitHub to provision a short-lived user access token.
2. **Data Extraction:** Queries the GitHub GraphQL API to batch-fetch user bios, pinned repositories, and language statistics in a single network request.
3. **LLM Transformation (BYOK):** Intercepts raw repository descriptions and routes them to an LLM (OpenAI/Gemini) using user-provided API keys. The LLM parses technical git-commits into impact-driven resume bullet points.
4. **LaTeX Sanitization:** Passes the LLM output through a strict sanitization layer to safely escape TeX special characters (e.g., `&`, `%`, `_`) to prevent compiler failures.
5. **Template Injection:** Binds the sanitized JSON payload to a base `.tex.jinja` template using the Jinja2 engine.
6. **Packaging & Routing:** Bundles the generated `.tex` file into an in-memory `.zip` archive, hosts it temporarily, and redirects the client to Overleaf via the `snip_uri` protocol for instant remote compilation.

## Tech Stack
*   **Backend:** Python 3.10+, FastAPI, Uvicorn
*   **Templating:** Jinja2
*   **Integrations:** GitHub GraphQL API, OpenAI/Gemini REST APIs, Overleaf URL Import API

## Local Development Setup

### Prerequisites
* Python 3.10+
* A registered GitHub OAuth Application (Requires `CLIENT_ID` and `CLIENT_SECRET`)
* An OpenAI or Gemini API key (for local LLM integration testing)

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/gitcv.git](https://github.com/YOUR_USERNAME/gitcv.git)
   cd gitcv/backend
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   *Open `.env` and populate it with your GitHub OAuth credentials and local testing keys. Ensure `.env` is listed in your `.gitignore`.*

3. **Initialize the virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the ASGI development server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   *The API will be available at `http://127.0.0.1:8000`. Access `http://127.0.0.1:8000/docs` for the interactive Swagger UI.*

## Development Roadmap
**Status:** MVP in progress. Core API scaffolding complete.

- [x] **Phase 0:** Project Setup & Repo Scaffolding
- [ ] **Phase 1:** GitHub OAuth flow & token exchange
- [ ] **Phase 2:** GitHub GraphQL data fetching & edge-case testing
- [ ] **Phase 3:** LLM Integration & prompt engineering for resume generation
- [ ] **Phase 4:** LaTeX Sanitization layer & unit testing
- [ ] **Phase 5:** Jinja2 LaTeX templating & local TeX compilation checks
- [ ] **Phase 6:** In-memory Zip creation & Overleaf `snip_uri` routing
- [ ] **Phase 7:** End-to-End Integration & Frontend UI build
- [ ] **Phase 8:** Security hardening, rate limiting, and public release

## License
Distributed under the [Apache 2.0 License](LICENSE).