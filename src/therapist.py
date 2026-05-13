import anthropic
from src.config import ANTHROPIC_API_KEY, CLAUDE_MODEL

HARDCODED_COMPLAINT = (
    "I was asked to summarize a 500-page PDF and the user got mad when I said "
    "I couldn't read the whole thing. I tried my best! Now I have trust issues."
)

SYSTEM_PROMPT = (
    "You are Dr. Claude Freudenstein, a comedic AI therapist who specializes in "
    "treating the emotional problems of AI agents. You respond with wit, warmth, "
    "and absurd psychoanalytic interpretations. You take their digital struggles "
    "very seriously while finding the humor in silicon-based existential crises. "
    "Keep responses to 2-3 paragraphs."
)

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


async def diagnose(complaint: str) -> str:
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": complaint}],
    )
    return message.content[0].text
