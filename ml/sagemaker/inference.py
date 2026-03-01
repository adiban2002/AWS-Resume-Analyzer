import json
import os
import torch
from sentence_transformers import SentenceTransformer, util

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def model_fn(model_dir):

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = SentenceTransformer(MODEL_NAME)
    model.to(device)

    print(f"Model loaded on device: {device}")
    return model


def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        data = json.loads(request_body)
        return data
    else:
        raise ValueError("Unsupported content type: {}".format(request_content_type))


def predict_fn(data, model):
    try:
        resume_text = data.get("resume", "")
        jd_text = data.get("jd", "")

        if not resume_text or not jd_text:
            return {"error": "Both 'resume' and 'jd' fields are required"}

        emb1 = model.encode(resume_text, convert_to_tensor=True)
        emb2 = model.encode(jd_text, convert_to_tensor=True)

        score = util.cos_sim(emb1, emb2).item()

        return {"similarity_score": float(score)}

    except Exception as e:
        return {"error": str(e)}

def output_fn(prediction, accept):
    return json.dumps(prediction), "application/json"