# Video Game Sales Dashboard

An interactive data dashboard built with Streamlit for exploring video game sales and release trends. The app loads cleaned VGChartz-style game data, categorizes platforms by brand, and displays yearly trends and brand statistics.

## Features

- Line chart of games released per year for each brand
- Year with the highest number of recorded game releases
- First year, last year, lifespan, and total game count by brand
- Peak release year for each brand
- Release counts for 1999

## Project Structure

```text
First_dashboard/
|-- main.py
|-- README.md
|-- data/
|   `-- clean_games.csv
`-- .gitignore
```

## Dataset

The application reads `data/clean_games.csv`. The dataset must include these columns:

- `Game Name`
- `System Full`
- `Units(m)`
- `Release Year`

Additional columns, such as `Publisher`, `Developer`, and `Release Date`, are also supported if present.

## Requirements

- Python 3.9 or newer
- Streamlit
- pandas
- NumPy
- Matplotlib
- Seaborn

## Installation

Clone the repository and move into its directory:

```bash
git clone https://github.com/ahmadbinsohail/First_dashboard.git
cd First_dashboard
```

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
```

Activate the environment:

- Windows:

  ```powershell
  .venv\Scripts\Activate.ps1
  ```

- macOS/Linux:

  ```bash
  source .venv/bin/activate
  ```

Install the required packages:

```bash
python -m pip install streamlit pandas numpy matplotlib seaborn
```

## Running the Dashboard

Start the Streamlit application from the repository root:

```bash
streamlit run main.py
```

Streamlit will print a local URL, usually `http://localhost:8501`, which can be opened in a browser.
