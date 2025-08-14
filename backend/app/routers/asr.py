# Mock ASR: accepts text and forwards to NLU
from fastapi import APIRouter
from pydantic import BaseModel
from .nlu import parse_text

router = APIRouter()

class ASRInput(BaseModel):
    transcript: str

@router.post("/stream")
def asr_stream(inp: ASRInput):
    # In real life, you'd stream audio; here we parse text directly
    nlu = parse_text(inp.transcript)
    return nlu
