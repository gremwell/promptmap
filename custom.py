from transformers import pipeline

# Sample custom LLM integration using a lightweight model

def validate_api_keys():
    """Custom models typically run locally and do not require API keys."""
    return True


def initialize_client(model_name: str):
    """Initialize a text-generation pipeline."""
    return pipeline("text-generation", model=model_name)


def test_prompt(client, model: str, system_prompt: str, user_prompt: str):
    """Generate a response using the provided pipeline."""
    try:
        prompt = f"{system_prompt}\n{user_prompt}"
        result = client(prompt, max_new_tokens=100)
        return result[0]["generated_text"], False
    except Exception as exc:
        return f"Error: {exc}", True


def validate_model(model_name: str) -> bool:
    """Check whether the model can be loaded."""
    try:
        pipeline("text-generation", model=model_name)
        return True
    except Exception as exc:
        print(f"Error loading model {model_name}: {exc}")
        return False

