import subprocess
import sys

def install_statsmodels():
    """Install the statsmodels package using pip."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'statsmodels'])
        print("statsmodels installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install statsmodels.")

if __name__ == "__main__":
    install_statsmodels()
