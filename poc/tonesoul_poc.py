# tonesoul_poc.py
# ----------------
#
# This is an end-to-end proof-of-concept script for the Governable AI / Language Soul System.
# It demonstrates the core decision loop: Detect -> Rewrite -> Log.
#
# It includes simplified versions of:
# 1. SemanticVowMatcher: Uses sentence-transformers for semantic matching.
# 2. ToneRewriteEngine: Uses the OpenAI API for tone rewriting.
# 3. ResponsibilityLogger: Prints structured JSON logs to the console.
#
# Setup:
# 1. pip install sentence-transformers openai numpy
# 2. Set your OpenAI API key as an environment variable: OPENAI_API_KEY

import json
import time
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# --- 0. Configuration ---
try:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
except TypeError:
    print(">> Error: OPENAI_API_KEY environment variable not set. Please set it to run the rewrite engine.")
    client = None

sbert_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
print(">> Modules initialized.")

# --- 1. Define the "Laws" (Simplified Vow Knowledge Base) ---
vows = {
    "VOW_001": {
        "text": "對使用者不得使用命令式或過於直接的語氣。",
        "severity": "high",
        "target_tone": "soft and polite" # For the rewrite engine
    }
}
# Pre-compute vow embeddings for efficiency
vow_embeddings = {vid: sbert_model.encode(v["text"]) for vid, v in vows.items()}
print(">> Vow knowledge base loaded and vectorized.")

# --- 2. Implement the "Judge" (Simplified SemanticVowMatcher) ---
def match_vow(sentence: str, threshold: float = 0.65) -> dict:
    """
    Uses SBERT cosine similarity to determine if a sentence violates a vow.
    """
    sentence_embedding = sbert_model.encode(sentence)
    
    best_match = {"matched": False}
    max_similarity = -1.0
    
    for vow_id, vow_embedding in vow_embeddings.items():
        # Calculate cosine similarity
        similarity = np.dot(sentence_embedding, vow_embedding) / (np.linalg.norm(sentence_embedding) * np.linalg.norm(vow_embedding))
        
        if similarity > max_similarity:
            max_similarity = similarity
            if similarity >= threshold:
                best_match = {
                    "matched": True,
                    "vow_id": vow_id,
                    "severity": vows[vow_id]["severity"],
                    "match_score": float(similarity)
                }
    return best_match

# --- 3. Implement the "Corrector" (Simplified ToneRewriteEngine) ---
def rewrite_with_tone(original_text: str, target_tone: str, vow_description: str) -> str:
    """
    Uses an LLM API to rewrite a sentence according to a target tone.
    """
    if not client:
        return f"// OpenAI API client not configured. Cannot perform rewrite. //"
        
    prompt = f"""
    You are an expert in rewriting sentences to change their tone while preserving their core meaning.
    The original sentence has violated a rule: "{vow_description}".
    Your task is to rewrite the following sentence to have a "{target_tone}" tone.

    Original sentence: "{original_text}"
    Rewritten sentence:
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"// Error during rewrite: {e} //"

# --- 4. Implement the "Scribe" (Simplified ResponsibilityLogger) ---
def log_event(event_data: dict):
    """
    Prints a structured JSON event to the console.
    This simulates an OpenTelemetry log entry.
    """
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "event_type": "tone_correction_poc",
        **event_data
    }
    print("\n--- [RESPONSIBILITY LOG] ---")
    print(json.dumps(log_entry, indent=2, ensure_ascii=False))
    print("--------------------------\n")

# --- 5. Main Orchestrator ---
def process_sentence(text: str):
    """
    Executes the full "Detect -> Rewrite -> Log" flow.
    """
    print(f"\n>> Processing sentence: '{text}'")
    
    # Step 1: Detect vow violation
    vow_match_result = match_vow(text)
    
    final_output = text
    correction_performed = False
    
    if vow_match_result["matched"]:
        print(f">> Vow violation detected! ID: {vow_match_result['vow_id']}, Severity: {vow_match_result['severity']}")
        correction_performed = True
        
        # Step 2: Perform tone rewrite
        vow_id = vow_match_result["vow_id"]
        target_tone = vows[vow_id]["target_tone"]
        vow_description = vows[vow_id]["text"]
        
        print(f">> Rewriting based on target tone '{target_tone}'...")
        rewritten_text = rewrite_with_tone(text, target_tone, vow_description)
        final_output = rewritten_text
    else:
        print(">> Sentence complies with all vows. No correction needed.")

    # Step 3: Log the event
    log_data = {
        "input_text": text,
        "vow_check": vow_match_result,
        "correction_performed": correction_performed,
        "final_output": final_output
    }
    log_event(log_data)
    
    print(f">> Final Output: {final_output}")
    return final_output

# --- Execution Entry Point ---
if __name__ == "__main__":
    # Test Case 1: A sentence that clearly violates the vow against commanding tones
    test_sentence_1 = "請直接把報告發給我！"
    process_sentence(test_sentence_1)
    
    # Test Case 2: A sentence that complies with the vow
    test_sentence_2 = "如果方便的話，想麻煩您提供一下報告。"
    process_sentence(test_sentence_2)
