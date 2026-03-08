# Leadfora
## Autonomous AI Sales Lead Hunter Agent

<img width="1536" height="1024" alt="1" src="https://github.com/user-attachments/assets/c0fa40e7-97c9-42d2-a08d-806dbbe7f3f5" />


### AI that finds qualified leads across the live web

---

## Overview

Leadfora is an autonomous AI sales agent that discovers qualified business leads by navigating the live web.

Powered by the TinyFish Web Agent API, Leadfora performs real multi-step workflows on real websites such as:

- LinkedIn
- Crunchbase
- company websites
- startup directories

The agent automatically identifies decision makers, extracts company information, finds contact details, ranks leads, and prepares CRM-ready lead lists.

Instead of spending hours manually searching for prospects, sales teams can now deploy an AI agent that does the work for them.

---

## The Problem

Sales teams spend 10+ hours every week manually searching for leads.

Typical workflow:

- Search LinkedIn for companies
- Identify founders, CEOs, or CTOs
- Visit company websites
- Find contact emails
- Build spreadsheets
- Remove duplicates
- Prioritize leads

This process is:

- slow
- repetitive
- expensive
- difficult to scale

Existing tools rely heavily on static databases or APIs, which often contain outdated or incomplete data.

However, the live web contains the most accurate information — but navigating it requires complex workflows.

AI needs the ability to:

- navigate websites
- interact with dynamic UIs
- manage sessions
- extract structured information
- perform multi-step tasks

This is exactly what TinyFish Web Agent infrastructure enables.

---

## The Solution

Leadfora is an AI-powered Sales Lead Hunter Agent that performs autonomous web workflows.

The system accepts a search query such as:

Find AI startup founders in Germany

Leadfora then:

- Launches multiple TinyFish-powered web agents
- Navigates real websites
- Extracts decision-maker information
- Identifies contact details
- Processes and scores leads
- Presents structured results in a dashboard
- Allows export to CRM systems

The result is a fully automated lead discovery pipeline.

---

## Key Features

### Autonomous Web Agents

Leadfora uses the TinyFish Web Agent API to interact with real websites.

Agents can:

- navigate pages
- follow links
- extract data
- handle dynamic interfaces
- execute multi-step workflows

---

### Multi-Agent Architecture

Instead of using a single agent, Leadfora deploys specialized agents in parallel.

Agents include:

- LinkedIn Agent → identifies decision makers
- Crunchbase Agent → discovers startups and companies
- Website Agent → extracts leadership information
- Email Agent → finds public contact emails

Parallel execution increases speed, scalability, and reliability.

---

### AI Lead Scoring Engine

All extracted leads are ranked using an AI scoring model.

Scoring factors include:

- decision-making authority
- company relevance
- availability of contact information
- industry keywords

This prioritizes leads into:

- High Priority
- Medium Priority
- Low Priority

Sales teams can immediately focus on the most valuable prospects.

---

### Deduplication Engine

Since leads may appear across multiple sources, Leadfora includes a deduplication system that removes duplicates based on:

- email
- LinkedIn profile
- company

This ensures clean, high-quality lead lists.

---

### AI Workflow Visualization

The dashboard shows a live workflow pipeline, allowing users to observe the AI system performing tasks.

Example workflow:

- Query Received
- LinkedIn Agent Searching
- Crunchbase Agent Discovering Companies
- Deduplicating Leads
- Scoring Leads
- Workflow Complete

This transparency improves trust and usability.

---

### CRM Export

Leads can be exported directly into CSV format, making them compatible with common CRM systems such as:

- HubSpot
- Salesforce
- Apollo
- Google Sheets

---

## System Architecture

<img width="1536" height="1024" alt="2" src="https://github.com/user-attachments/assets/0708c551-7159-4773-9b69-6fe53ab2015f" />

```
User Query
     ↓
Leadfora Dashboard (Next.js + Tailwind)
     ↓
FastAPI Backend
     ↓
Agent Orchestrator
     ↓
TinyFish Web Agents
     ↓
Live Websites
LinkedIn / Crunchbase / Company Sites
     ↓
Lead Extraction
     ↓
Deduplication Engine
     ↓
AI Lead Scoring
     ↓
MongoDB Database
     ↓
Dashboard + CSV Export
```

---

## Technology Stack

### Frontend

- Next.js
- Tailwind CSS
- Axios

### Backend

- Python
- FastAPI
- AsyncIO

### AI Agent Infrastructure

- TinyFish Web Agent API

### Database

- MongoDB

### Deployment

- Vercel (Frontend)
- Railway (Backend)

---

## Project Structure

```
leadfora
│
├── frontend
│   ├── app
│   │   ├── dashboard
│   │   └── page.js
│   └── components
│
├── backend
│   ├── agents
│   │   ├── lead_agent.py
│   │   ├── linkedin_agent.py
│   │   ├── crunchbase_agent.py
│   │   └── email_agent.py
│
│   ├── services
│   │   ├── tinyfish_client.py
│   │   ├── deduplication.py
│   │   ├── lead_scoring.py
│   │   └── lead_storage.py
│
│   ├── database
│   │   └── mongo.py
│
│   └── main.py
│
└── README.md
```

---

## How It Works

### Step 1 — User Query

User enters a search query.

Example:

Find SaaS startup CEOs in Europe

---

### Step 2 — Agent Orchestration

The backend launches multiple agents simultaneously.

- LinkedIn Agent
- Crunchbase Agent
- Website Agent
- Email Agent

---

### Step 3 — Web Navigation

Agents use TinyFish infrastructure to:

- browse websites
- extract structured information
- perform real web workflows

---

### Step 4 — Lead Processing

Extracted leads go through:

- deduplication
- AI lead scoring
- structured formatting

---

### Step 5 — Dashboard & Export

Leads appear in the dashboard and can be exported for CRM use.

---

## Running the Project Locally

### Clone Repository

```
git clone https://github.com/YOUR_USERNAME/leadfora
```

---

### Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on:

```
http://localhost:8000
```

---

### Frontend Setup

```
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:3000
```

---

## Example Workflow

User query:

AI startups in Germany

Leadfora:

- Searches LinkedIn
- Discovers companies on Crunchbase
- Visits company websites
- Extracts leadership information
- Finds public email addresses
- Scores leads
- Displays results

---

## Impact

Lead generation is a multi-billion-dollar market.

Companies rely heavily on tools like:

- ZoomInfo
- Apollo
- LinkedIn Sales Navigator

Leadfora demonstrates how autonomous AI agents can perform the entire workflow — dramatically reducing manual labor.

This approach opens the door to a new generation of AI-driven sales intelligence platforms.

---

## Future Improvements

Planned features include:

- automated outreach campaigns
- email personalization using LLMs
- CRM integrations (HubSpot, Salesforce)
- hiring signal detection
- funding announcement monitoring
- competitive intelligence agents

---

## Demo

Live Demo:

[https://leadfora.vercel.app](https://leadfora-eight.vercel.app)

Demo Video:

https://youtu.be/ylU9_3JYj88

---

## Repository

https://github.com/umang252000/leadfora


## Instructions
### 1. Clone the Repository
- First clone the project from GitHub.
- "git clone https://github.com/umang252000/leadfora"
- "cd leadfora"

### 2. Backend Setup
Navigate to the backend directory.
- "cd backend"

- Install required Python dependencies.
- "pip install fastapi uvicorn python-dotenv pymongo httpx"

### 3. Configure Environment Variables

- Create a .env file inside the backend folder.

- Example:

- TINYFISH_API_KEY=your_tinyfish_api_key
- MONGO_URI=your_mongodb_connection_string
- DATABASE_NAME=leadfora

- Where:
- TINYFISH_API_KEY is your TinyFish Web Agent API key
- MONGO_URI is your MongoDB database connection string

### 4. Start Backend Server
- Run the FastAPI server.
- "uvicorn main:app --reload"

- Backend will run at:
- "http://localhost:8000"

- You can also access API documentation at:
- "http://localhost:8000/docs"

### 5. Frontend Setup
- Open a new terminal and navigate to the frontend folder.
- "cd frontend"

- Install dependencies.
- "npm install"

- Start the development server.
- "npm run dev"

- Frontend will run at:
- "http://localhost:3000"

### 6. Using the Application
- Open the Leadfora dashboard in your browser: 
- "http://localhost:3000"

- Enter a lead search query.

- Example:
- AI startups in Germany
- Click Run Agent

The system will:

- Launch TinyFish web agents
- Navigate LinkedIn, Crunchbase, and company websites
- Extract decision makers and company information
- Deduplicate results
- Score leads using the AI scoring engine
- Display leads in the dashboard

### 7. Export Leads
After leads are generated, click:
- "Export CSV"

- This downloads a CRM-ready lead list that can be imported into:
- HubSpot
- Salesforce
- Apollo
- Google Sheets

### 8. Example Workflow
User Query:
- "Find AI startup founders in Europe"

- Leadfora automatically:
- Searches LinkedIn for decision makers
- Discovers companies via Crunchbase
- Visits company websites
- Extracts leadership information
- Finds contact emails
- Removes duplicate leads
- Scores and prioritizes leads

Results are displayed in the dashboard.

### 9. Project Architecture
- User
-  ↓
- Leadfora Dashboard (Next.js + Tailwind)
-  ↓
- FastAPI Backend
-  ↓
- Agent Orchestrator
-  ↓
- TinyFish Web Agent API
-  ↓
- Live Websites
-  ↓
- Lead Processing
-  ↓
- MongoDB Database
-  ↓
- Dashboard + CSV Export
