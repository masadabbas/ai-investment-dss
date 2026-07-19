# 📈 AI-Based Long-Term Investment Advisory System

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript)
![HTML5/CSS3](https://img.shields.io/badge/HTML5_&_CSS3-UI-E34F26?style=for-the-badge&logo=html5)
![Machine Learning](https://img.shields.io/badge/AI-Optimization-FF6F00?style=for-the-badge)

An intelligent, data-driven Decision Support System (DSS) that provides personalized long-term investment portfolios. The system evaluates live market data, applies propositional logic based on user risk profiles, and utilizes advanced meta-heuristic algorithms (Simulated Annealing & Hill Climbing) to optimize capital allocation.

---

## ✨ Core Features
*   **Live Market Data Integration:** Connects to Yahoo Finance (`yfinance`) to fetch live ticker data and news.
*   **Smart TTL Caching:** Implements daily local caching (`.csv`) to prevent network bottlenecks and API rate limits.
*   **Heuristic Scoring Engine:** Evaluates assets based on CAGR, Volatility, Stability, Dividend Yield, and Liquidity.
*   **Portfolio Optimization:** Utilizes mathematical optimization algorithms to calculate the exact weight and capital allocation for each approved asset.
*   **Interactive UI:** A lightweight, responsive HTML/JS frontend dashboard to interact seamlessly with the FastAPI backend.

---
#🚀 Installation & Setup1. Clone the RepositoryBashgit clone [https://github.com/masadabbas/ai-investment-dss.git](https://github.com/masadabbas/ai-investment-dss.git)
cd ai-investment-dss
2. Configure the Python BackendCreate and activate a clean virtual environment, then install the dependencies:Bash# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
3. Run the Backend APIStart the FastAPI server. This acts as the data engine for the system.Bashuvicorn api:app --reload
Base URL: http://127.0.0.1:8000Swagger API Docs: http://127.0.0.1:8000/docs💻 Running the Frontend DashboardThe frontend is built using standard web technologies and connects to the API via REST.Open your code editor (e.g., VS Code).Install the Live Server extension.Navigate to the frontend/ folder.Right-click index.html and select "Open with Live Server".The dashboard will automatically launch in your browser at http://127.0.0.1:5500.🛠️ Tech Stack DirectoryBackend Framework: FastAPI, UvicornData Sourcing: yfinance, Pandas, NumPyMachine Learning/Optimization: Scikit-learn, Custom Meta-HeuristicsFrontend: HTML5, CSS3, Vanilla JavaScript (ES6)🔒 API EndpointsMethodEndpointDescriptionGET/API Root Health CheckPOST/api/run-pipelineCore processing engine. Accepts User constraints (JSON) and returns the evaluated matrix & optimized capital allocations.

---

## 📊 System Architecture & Data Flow

```mermaid
graph TD
    %% Nodes
    A([User Dashboard UI])
    B(FastAPI Backend Endpoints)
    C{Smart Data Cache}
    D[(Local CSV Files)]
    E((YFinance API))
    F[Feature Engineering & Indicators]
    G[Heuristic Scoring Model]
    H[Simulated Annealing Optimizer]
    I([Final Optimized Portfolio])

    %% Connections
    A -- JSON: Capital, Risk, Sectors --> B
    B --> C
    C -- "If today's data exists" --> D
    C -- "If data is old/missing" --> E
    E -- "Save new data" --> D
    D --> F
    F -- "CAGR, Volatility, etc." --> G
    G -- "Approved Stocks Matrix" --> H
    H -- "Algorithm Weights" --> B
    B -- "JSON Response" --> I
    I -- "Renders Charts" --> A

    %% Define Styles
    classDef user fill:#2b3a42,stroke:#3f5765,stroke-width:2px,color:#fff
    classDef api fill:#009688,stroke:#00796b,stroke-width:2px,color:#fff
    classDef logic fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff
    classDef data fill:#2980b9,stroke:#2471a3,stroke-width:2px,color:#fff
    classDef front fill:#8e44ad,stroke:#732d91,stroke-width:2px,color:#fff

    %% Assign Styles
    class A user
    class B api
    class C,D,E data
    class F,G,H logic
    class I front