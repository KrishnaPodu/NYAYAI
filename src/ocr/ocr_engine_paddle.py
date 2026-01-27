from pathlib import Path
from unittest import result
from paddleocr import PaddleOCR
from typing import Optional, List, Dict
from src.common.config import USE_GPU, LANGUAGES

_engine: Optional[PaddleOCR] = None


def _get_engine() -> PaddleOCR:
    global _engine

    if _engine is not None:
        return _engine

    # lang = "+".join(LANGUAGES)
    lang = 'devanagari' if 'devanagari' in LANGUAGES else 'en'

    # Try GPU first
    if USE_GPU:
        try:
            _engine = PaddleOCR(
                use_angle_cls=True,
                use_gpu=True,
                lang=lang,
            )

            print("PaddleOCR running on GPU during ocr")
            return _engine
        except Exception as e:
            print(f"[WARN] GPU OCR init failed, falling back to CPU: {e}")

    # Fallback to CPU
    _engine = PaddleOCR(
        use_angle_cls=True,
        use_gpu=False,
        lang=lang,
    )

    print(
    "[INFO] PaddleOCR running on ","GPU" if _engine.use_gpu else "CPU"
    )

    return _engine







def run_ocr(image_path: Path, regions=None) -> List[Dict]:
    """
    Run OCR on a single image.

    This function assumes the caller has already decided
    that OCR is actually needed.
    """

    engine = _get_engine()

    result = engine.ocr(str(image_path), cls=True)

    blocks: List[Dict] = []

    if not result:
        print("no result during ocr")
        return blocks

    for item in result:
        try:
            text, confidence = item[1]

            # Unwrap weird PaddleOCR shapes
            if isinstance(text, (tuple, list)):
                text = text[0]

            if isinstance(confidence, (tuple, list)):
                confidence = confidence[0]

            text = str(text).strip()
            confidence = float(confidence)

            print("hi")
            print(text, confidence)

            if not text:
                continue
            blocks.append({
                "text": text,
                "confidence": confidence
            })

        except Exception:
            # Skip malformed OCR entries
            continue


    return blocks
