from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS openzetten voor lokale frontend tests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/meldingen")
def get_meldingen():
    df = pd.read_csv("m2m_meldingen_logisch.csv")
    # Kies alleen de kolommen die je wilt tonen
    return df.to_dict(orient="records")
