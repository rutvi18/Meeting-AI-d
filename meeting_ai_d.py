import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_meeting_transcript(file_path):
    """Reads a meeting transcript from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            transcript = f.read()
        return transcript
    except FileNotFoundError:
        print(f"Error: Transcript file not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def summarize_transcript(transcript, model="gpt-3.5-turbo"):
    """Generates a concise summary of the meeting transcript."""
    prompt = f"""
    Please provide a concise summary of the following meeting transcript.
    Focus on the main topics discussed, key decisions made, and overall conclusions.

    Transcript:
    \"\"\"{transcript}\"\"\"

    Summary:
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in summarizing meeting transcripts."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250, # Adjust as needed for summary length
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except openai.APIError as e:
        print(f"OpenAI API Error during summarization: {e}")
        return "Summary generation failed."
    except Exception as e:
        print(f"An unexpected error occurred during summarization: {e}")
        return "Summary generation failed."

def extract_action_items(transcript, model="gpt-3.5-turbo"):
    """Extracts action items, assigned persons, and due dates from the transcript."""
    prompt = f"""
    From the following meeting transcript, extract all action items.
    For each action item, identify the task, the person responsible (if mentioned), and any deadlines (if mentioned).
    Present the action items as a numbered list. If no person or deadline is specified for an item, indicate 'N/A'.

    Example format for an action item:
    1. Task: Research new market trends.
       Person: John Doe
       Deadline: End of Q3

    Transcript:
    \"\"\"{transcript}\"\"\"

    Action Items:
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant specialized in extracting action items from meeting notes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500, # Adjust as needed for number of action items
            temperature=0.3 # Lower temperature for more factual extraction
        )
        return response.choices[0].message.content.strip()
    except openai.APIError as e:
        print(f"OpenAI API Error during action item extraction: {e}")
        return "Action item extraction failed."
    except Exception as e:
        print(f"An unexpected error occurred during action item extraction: {e}")
        return "Action item extraction failed."


# --- Main execution logic ---
if __name__ == "__main__":
    # Create a dummy transcript file for testing
    dummy_transcript_content = """
    Attendees: Alice, Bob, Carol, David
    Date: July 8, 2025
    Topic: Q3 Marketing Strategy Review

    Alice: Hi team, thanks for joining. Let's start with a quick review of Q2 performance. Bob, can you share the sales figures?
    Bob: Sure. Q2 sales were up 15% year-over-year, largely due to the social media campaign. However, customer acquisition cost increased.
    Carol: That's concerning. I think we need to re-evaluate our targeting. Alice, could you look into optimizing the Facebook ad spend by end of next week?
    Alice: Yes, I can do that.
    David: I've started drafting the Q3 campaign proposals. I need input on new content ideas. Bob, could you brainstorm some viral content concepts by Friday?
    Bob: Got it. I'll get some ideas ready.
    Alice: Also, Carol, we need to schedule a follow-up with the SEO agency. Please send out calendar invites for next Tuesday.
    Carol: On it. I'll ensure everyone is available.
    Bob: Regarding the new product launch, we need a strong press release. David, can you finalize the draft for review by next Monday?
    David: Absolutely. I'll have it ready.
    Alice: Great. Let's aim to finalize the strategy by the end of July.
    """
    with open("meeting_transcript.txt", "w", encoding="utf-8") as f:
        f.write(dummy_transcript_content)

    transcript_file = "meeting_transcript.txt"
    transcript = get_meeting_transcript(transcript_file)

    if transcript:
        print("--- Meeting Transcript Loaded ---")
        # print(transcript[:200] + "...\n") # Print first 200 chars for verification

        print("\n--- Generating Summary ---")
        summary = summarize_transcript(transcript)
        print(summary)

        print("\n--- Extracting Action Items ---")
        action_items = extract_action_items(transcript)
        print(action_items)