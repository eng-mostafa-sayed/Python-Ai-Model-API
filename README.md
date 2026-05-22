# Local AI Model API

This is a simple local FastAPI project for serving an AI model on your laptop.

## Project Structure

```text
.
+-- main.py
+-- requirements.txt
+-- README.md
+-- app/
    +-- __init__.py
    +-- schemas.py
    +-- model_service.py
```

## Create a Virtual Environment on Windows

Open PowerShell in the project folder and run:

```powershell
python -m venv venv
```

## Activate the Virtual Environment

In PowerShell, run:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation scripts, run this command once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the virtual environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

## Install Requirements

After activating the virtual environment, install the required packages:

```powershell
pip install -r requirements.txt
```

## Run the API Locally

Start the FastAPI development server with Uvicorn:

```powershell
uvicorn main:app --reload
```

The API will run locally at:

```text
http://127.0.0.1:8000
```

Swagger API docs are available at:

```text
http://127.0.0.1:8000/docs
```

## Example Prediction Request

Send a POST request to:

```text
http://127.0.0.1:8000/predict
```

With this JSON body:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

The API predicts from the values you send in `features`. The order is `sepal_length`, `sepal_width`, `petal_length`, `petal_width`.
