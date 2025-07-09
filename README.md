# Meeting AI-d (Text-Based)

## Intelligent Meeting Summarization and Action Item Extraction

Meeting AI-d is a Python-based tool that leverages OpenAI's powerful GPT models to streamline your meeting workflows. It automates the tedious tasks of generating concise summaries and extracting actionable insights from plain text meeting transcripts.

-----

## Features

  * **Concise Summarization:** Generates a brief, intelligent summary of the meeting, highlighting key discussions, decisions, and overall conclusions using GPT.
  * **Action Item Extraction:** Automatically identifies and lists actionable tasks, including assigned persons and deadlines (if mentioned), making follow-ups effortless.
  * **Easy to Use:** Simple command-line interface for quick processing of text files.

-----

## Real-Life Use Cases

  * **Busy Professionals:** Quickly catch up on missed meetings or review discussion points from existing notes.
  * **Project Managers:** Efficiently track tasks, assignees, and deadlines derived directly from meeting discussions.
  * **Students & Researchers:** Summarize lectures, interviews, or research discussions from written notes.
  * **Sales & Customer Service:** Condense call transcripts (if already in text format) for CRM entry, compliance, or training purposes.

-----

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed. You can download it from [python.org](https://www.python.org/downloads/).

### Steps

1.  **Clone the Repository (or create the project folder):**

    ```bash
    git clone https://github.com/your-username/meeting-ai-d.git
    cd meeting-ai-d
    ```

    *(Replace `https://github.com/your-username/meeting-ai-d.git` with your actual repo URL if you plan to host it on GitHub)*

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install openai python-dotenv
    ```

4.  **Set up OpenAI API Key:**

      * Obtain an API key from your [OpenAI platform dashboard](https://platform.openai.com/api-keys).
      * Create a file named `.env` in the root directory of your project (`meeting-ai-d/`).
      * Add your API key to this file:
        ```
        OPENAI_API_KEY="your_openai_api_key_here"
        ```
      * **Important:** If you're using Git, add `.env` to your `.gitignore` file to prevent accidentally committing your key to version control.

-----

## Usage

1.  **Prepare your Transcript File:**

      * Create a plain text file (e.g., `my_meeting_transcript.txt`) containing the full transcript of your meeting.
      * Place this file in the project directory.

2.  **Run the Script:**
    Open your terminal, navigate to the `meeting-ai-d` project directory, activate your virtual environment, and run the script:

    ```bash
    # Make sure your virtual environment is active
    source venv/bin/activate # On Windows: .\venv\Scripts\activate

    python meeting_ai_d.py your_transcript_file.txt
    # Replace 'your_transcript_file.txt' with the actual name of your text file
    ```

    **Example:**

    ```bash
    python meeting_ai_d.py sample_transcript.txt
    ```

    The script will:

      * Load the text transcript.
      * Print a concise summary of the meeting.
      * Print a list of extracted action items.

### Command-Line Arguments (Simple Example)

The script expects the transcript file path as the first command-line argument.

```python
# Inside meeting_ai_d.py, in the __main__ block
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python meeting_ai_d.py <transcript_file_path>")
        print("Example: python meeting_ai_d.py sample_transcript.txt")
        sys.exit(1)

    transcript_file = sys.argv[1]

    # ... rest of the existing logic ...
    # (replace the hardcoded 'meeting_transcript.txt' and dummy content)
```

-----

## Project Structure

```
meeting-ai-d/
├── .env                  # Your OpenAI API key (DO NOT commit to Git!)
├── .gitignore            # Specifies files/folders to ignore in Git
├── meeting_ai_d.py       # Main Python script
├── sample_transcript.txt # (Optional) Example text transcript for testing
└── venv/                 # Python virtual environment (if created)
```

-----

## Contributing

Feel free to fork this repository, open issues, or submit pull requests to improve the functionality or add new features\!

-----

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

-----

## Acknowledgements

  * **OpenAI:** For providing the powerful GPT models.
  * **`python-dotenv`:** For secure environment variable loading.

-----
