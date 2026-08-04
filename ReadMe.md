# Selenium with Python Automation Framework

## Prerequisites

- Python 3.12 or later
- Git
- Google Chrome

---

# Project Setup

## 1. Clone Repository

```bash
git clone <repository-url>
cd SeleniumWithPython
```

---

## 2. Create Virtual Environment

### Windows (Command Prompt)

```cmd
python -m venv venv
```

### Windows (PowerShell)

```powershell
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

> If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Run the activation command again.

### Linux

```bash
source venv/bin/activate
```

### macOS

```bash
source venv/bin/activate
```

---

## 4. Upgrade pip

### Windows

```cmd
python -m pip install --upgrade pip
```

### Linux / macOS

```bash
python3 -m pip install --upgrade pip
```

---

## 5. Install Project Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 6. Install the Project

```bash
python -m pip install -e .
```

---

# Execute Tests
> Without Allure Reports

```bash
pytest
```

---

> With Allure Results

```bash
pytest --alluredir=allure-results
```

---

# Static Analysis

## Check Python Syntax

```bash
python -m compileall .
```

---

## Type Checking (Recommended)

```bash
python -m mypy .
```

---

# Deactivate Virtual Environment

### Windows

```cmd
deactivate
```

### Linux / macOS

```bash
deactivate
```

---

# Reinstall Dependencies

If `requirements.txt` is updated:

```bash
python -m pip install -r requirements.txt
```

If `pyproject.toml` is updated:

```bash
python -m pip install -e .
```