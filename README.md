# Osdag Bridge Module — Web UI

> OSDAG Screening Task · Bridge Module UI Development by Aradhana Singh

> React + Django · Dark/Light Theme · Full IRC 6 Database (Option A +20%)

---

## Overview

A full-stack web application implementing the **Osdag Bridge Module UI** as specified in the OSDAG Screening Task. The application handles all user input, validation, IRC location data lookup, and design management through a clean engineering interface styled after the real Osdag desktop application.

**Key highlights:**
- Complete IRC 6 (2017) database — 152 districts across 36 Indian states (Option A, +20% extra credit)
- Location data served entirely from the embedded frontend database — zero latency, works without backend
- Dark and light theme with toggle, persisted to localStorage
- Full input validation with real-time error feedback per IRC/IS standards
- Modify Additional Geometry popup with auto-calculation of interdependent fields
- Save / Load / Duplicate / Delete designs via Django REST API

---

## Screenshots

| IRC Values (Green) | Modify Geometry Popup |
|---|---|
| ![IRC Values](screenshots/irc-values-green.png) | ![Geometry Popup](screenshots/modify-geometry.png) |

| Other Structure Disabled | Custom Parameters Modal |
|---|---|
| ![Other Disabled](screenshots/other-disabled.png) | ![Custom Params](screenshots/custom-params.png) |

---

## Features

### Basic Inputs Tab

**Type of Structure**
- Choices: Highway Bridge or Other
- Selecting "Other" displays error message and disables all remaining inputs

**Project Location** — two mutually exclusive modes

| Mode | Behaviour |
|---|---|
| Enter Location Name | State → District cascade dropdowns; auto-populates IRC 6 values in **green** |
| Tabulate Custom Parameters | Opens spreadsheet-style popup for manual wind/seismic/temperature entry |

**Superstructure Geometric Details**

| Field | Validation |
|---|---|
| Span (m) | Must be 20 – 45 m (`Outside the software range` otherwise) |
| Carriageway Width (m) | Must be ≥ 4.25 m and < 24 m |
| Footpath | None / Single-sided / Both |
| Skew Angle (°) | Must be within ±15° (IRC 24:2010) |

**Modify Additional Geometry Popup**

| Field | Format | Rule |
|---|---|---|
| Girder Spacing (m) | Float, 1 decimal | < Overall Bridge Width |
| No. of Girders | Integer | Whole number only |
| Deck Overhang Width (m) | Float, 1 decimal | < Overall Bridge Width |

Auto-calculation rule:
```
Overall Bridge Width = Carriageway Width + 5 m
(Overall Width − Deck Overhang) / Girder Spacing = No. of Girders
```
Changing any one field automatically updates the other two.

**Material Inputs**

| Component | Allowed Grades |
|---|---|
| Girder | E250 (Fe 410W)A, E350, E450 |
| Cross Bracing | E250 (Fe 410W)A, E350, E450 |
| End Diaphragm | E250 (Fe 410W)A, E350, E450 |
| Deck | M25, M30, M35, M40, M45, M50, M55, M60 |

### Additional Inputs Tab
Placeholder tab — visible in UI, no functionality required per spec.

---

## IRC Database (Option A — Extra Credit +20%)

The frontend embeds a complete database derived from official IRC 6 (2017) tables:

- **36 states** and union territories
- **152 districts** total
- **3 values per district:** Basic Wind Speed (m/s), Seismic Zone & Zone Factor, Max/Min Shade Air Temperature (°C)

Sources: IS 875 Part 3, IS 1893 Part 1, IRC 6:2017

The database is compiled in `frontend/src/services/locationData.js` and `location_db.json` (included in repo root).

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Tailwind CSS, Lucide React |
| Styling | IBM Plex Sans + IBM Plex Mono, CSS Variables (dark/light) |
| Backend | Django 4.2, Django REST Framework |
| Database | SQLite — IRC location data + saved designs |
| Location Data | Embedded JS module — no backend call needed |

---

## Project Structure

```
osdag-bridge-module/
├── README.md
├── Database_Processed.csv        ← IRC source data
├── location_db.json              ← Processed JSON database
├── screenshots/                  ← UI screenshots
│
├── frontend/
│   ├── public/
│   │   └── bridge-section.png   ← Bridge cross-section reference image
│   ├── src/
│   │   ├── App.js               ← Root + ThemeProvider wrapper
│   │   ├── App.css              ← Full design system (dark + light CSS variables)
│   │   ├── index.css            ← Tailwind base + theme root styles
│   │   ├── ThemeContext.js      ← Global dark/light theme state (localStorage)
│   │   ├── services/
│   │   │   ├── locationData.js  ← Embedded IRC database (152 districts)
│   │   │   └── api.js           ← Location API (local) + Bridge Design API (Django)
│   │   └── components/
│   │       ├── BridgeDesign.jsx          ← Main UI — all Basic Inputs logic
│   │       ├── BridgeDesign.css          ← Component-level style overrides
│   │       ├── SaveDesignModal.jsx       ← Save design dialog
│   │       ├── LoadDesignModal.jsx       ← Load / search / delete designs
│   │       └── CustomParametersModal.jsx ← Tabulate custom IRC parameters
│   └── package.json
│
└── backend/
    ├── osdag_backend/            ← Django project settings
    ├── bridge_design/            ← Django app (models, views, serializers, urls)
    ├── db.sqlite3                ← SQLite database
    ├── load_comprehensive_data.py ← Script to seed IRC location data
    └── manage.py
```

---

## Setup & Installation

### Prerequisites
- Node.js 18+
- Python 3.10+

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/osdag-bridge-module.git
cd osdag-bridge-module
```

### 2. Backend setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install django djangorestframework django-cors-headers

# Run migrations
python manage.py migrate

# Seed IRC location database (optional — frontend has embedded DB)
python load_comprehensive_data.py

# Start server
python manage.py runserver
```

Backend runs at `http://localhost:8000`

> **Note:** The frontend embeds the full location database directly, so the backend is only needed for Save/Load design functionality. Location lookup works without the backend running.

### 3. Frontend setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at `http://localhost:3000`

---

## Demo Values (Satisfying All Validations)

| Field | Value |
|---|---|
| Structure Type | Highway Bridge |
| State | Maharashtra |
| District | Mumbai |
| Span | `30.0` m |
| Carriageway Width | `7.5` m |
| Footpath | None |
| Skew Angle | `0.0` ° |
| Girder Spacing | `2.5` m |
| No. of Girders | `4` |
| Deck Overhang | `2.5` m |

Geometry equation: `(7.5 + 5 − 2.5) / 2.5 = 4.0` ✅

Custom Parameters demo:

| Field | Value |
|---|---|
| Wind Speed | `44` m/s |
| Seismic Zone | Zone III (Z = 0.16 auto) |
| Max Shade Temp | `45` °C |
| Min Shade Temp | `11` °C |

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/locations/states/` | All states |
| `GET` | `/api/locations/districts/?state=Maharashtra` | Districts for state |
| `GET` | `/api/locations/data/?state=X&district=Y` | IRC 6 values |
| `GET` | `/api/designs/` | List saved designs |
| `POST` | `/api/designs/` | Create design |
| `GET` | `/api/designs/:id/` | Get design |
| `PUT` | `/api/designs/:id/` | Update design |
| `DELETE` | `/api/designs/:id/` | Delete design |
| `POST` | `/api/designs/:id/duplicate/` | Duplicate design |
| `POST` | `/api/designs/:id/toggle_favorite/` | Toggle favourite |

---

## Evaluation Checklist

| Criterion | Status |
|---|---|
| UI layout clarity and adherence to spec | ✅ |
| Enter Location Name mode with IRC values in green | ✅ |
| Tabulate Custom Parameters mode | ✅ |
| Mutually exclusive location mode checkboxes | ✅ |
| "Other" structure type disables all inputs | ✅ |
| Span validation (20–45 m) | ✅ |
| Carriageway width validation (≥ 4.25, < 24 m) | ✅ |
| Skew angle validation (± 15°) | ✅ |
| Modify Geometry popup — auto-adjust all three fields | ✅ |
| Geometry equation validation with error messages | ✅ |
| Material grade options (E250/E350/E450, M25–M60) | ✅ |
| Additional Inputs tab (placeholder) | ✅ |
| Bridge cross-section reference image | ✅ |
| Code organisation — UI separated from logic | ✅ |
| README | ✅ |
| Option A — full IRC database (+20% extra credit) | ✅ 36 states, 152 districts |
| Dark / Light theme toggle | ✅ Bonus |
| Save / Load / Duplicate designs | ✅ Bonus |
