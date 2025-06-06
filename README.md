# Hockey Analysis Project

This project uses Jupyter notebooks for data analysis and visualization.

## Setup Instructions

1. Navigate to the project directory:
```bash
cd hyland-hockey
```

2. Create and activate a virtual environment:
```bash
#python -m venv venv
pyenv virtualenv 3.10.12 hockey
#source venv/bin/activate  # On Linux/Mac
pyenv local hockey
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Running Jupyter Notebook

1. Make sure your virtual environment is activated
2. Start the Jupyter server:
```bash
jupyter notebook
```

3. The Jupyter interface will open in your default web browser at http://localhost:8888
   - If it doesn't open automatically, copy and paste the URL from the terminal output

## Using Jupyter Notebooks

- Click "New" → "Python 3" to create a new notebook
- Use Shift + Enter to run a cell
- Use Ctrl + Enter to run a cell without moving to the next one
- Use the toolbar buttons to add new cells, run cells, and save your work

## Project Structure

```
hyland-hockey/
├── requirements.txt    # Lists all Python package dependencies
├── *.ipynb            # Jupyter notebook files
└── venv/             # Virtual environment directory (not tracked in git)
```

## Common Libraries Available

- NumPy: Numerical computing
- Pandas: Data manipulation and analysis
- Matplotlib & Seaborn: Data visualization 