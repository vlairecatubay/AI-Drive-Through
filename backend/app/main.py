from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import menu, orders, asr, nlu

app = FastAPI(title="AI Drive-Thru Ordering System", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(asr.router, prefix="/asr", tags=["ASR (Mock)"])
app.include_router(nlu.router, prefix="/nlu", tags=["NLU (Mock)"])

@app.get("/")
def root():
    return {"status": "ok", "service": "AI Drive-Thru API"}
