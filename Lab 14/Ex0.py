import importlib.util

# List of packages to check
packages = ['scipy', 'statsmodels', 'matplotlib']

# Check if each package is installed
for package in packages:
    spec = importlib.util.find_spec(package)
    if spec is not None:
        print(f"✓ {package} is installed")
    else:
        print(f"✗ {package} is NOT installed")
