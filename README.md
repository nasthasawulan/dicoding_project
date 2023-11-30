# Setup Environment
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas matplotlib streamlit

# Run Streamlit App
streamlit run dashboard.py
