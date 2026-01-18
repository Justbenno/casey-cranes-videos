# OpenAI Streaming Script Setup Guide

A simple step-by-step guide to get you started with the `stream_with_log.py` script.

## What This Script Does

The `stream_with_log.py` script allows you to:
1. Ask questions to OpenAI's GPT-4 model
2. See the response stream in real-time (word by word)
3. Automatically save every conversation to a timestamped file in the `responses/` folder

## Prerequisites

- Python 3.8 or higher installed on your computer
- An OpenAI API key (you can get one from https://platform.openai.com/api-keys)

## Step-by-Step Setup

### Step 1: Install the OpenAI Package

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and run:

```bash
pip install openai
```

If you're using Python 3 specifically, you might need:

```bash
pip3 install openai
```

### Step 2: Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Log in to your OpenAI account (or create one)
3. Click "Create new secret key"
4. Copy the key (it will look something like `sk-...`)
5. **Important**: Keep this key private and never share it publicly

### Step 3: Add Your API Key to the Script

**Option A: Edit the script directly (simpler)**

1. Open `scripts/stream_with_log.py` in a text editor (VS Code, Notepad++, or any editor)
2. Find the line that says:
   ```python
   openai.api_key = "your-api-key-here"
   ```
3. Replace `"your-api-key-here"` with your actual API key:
   ```python
   openai.api_key = "sk-your-actual-key-here"
   ```
4. Save the file

**Option B: Use an environment variable (more secure)**

Instead of editing the script, set an environment variable:

On Mac/Linux:
```bash
export OPENAI_API_KEY="sk-your-actual-key-here"
```

On Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=sk-your-actual-key-here
```

On Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="sk-your-actual-key-here"
```

Then modify the script to use the environment variable:
```python
import os
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
```

## Running the Script

### Basic Usage

1. Navigate to the scripts directory:
   ```bash
   cd scripts
   ```

2. Run the script:
   ```bash
   python stream_with_log.py
   ```

   Or if you're using Python 3:
   ```bash
   python3 stream_with_log.py
   ```

3. When prompted, type your question:
   ```
   What would you like to ask the model?
   > Tell me about crane safety best practices
   ```

4. Watch the response stream in real-time!

5. After the response completes, check the `responses/` folder for a saved file with the full conversation.

### Example Workflow

```bash
$ cd scripts
$ python3 stream_with_log.py

What would you like to ask the model?
> What are the best practices for crane maintenance?

Streaming response...

[Response appears here in real-time...]

Streaming complete!

Saved full response to: responses/response_2026-01-15_14-30-45.txt
```

## Understanding the Output

### Real-time Streaming
As the AI generates its response, you'll see each word appear in your terminal as it's created. This gives you immediate feedback.

### Saved Files
Each conversation is saved in the `responses/` directory with:
- **Filename format**: `response_YYYY-MM-DD_HH-MM-SS.txt`
- **Contents**: Both your prompt and the complete response

Example saved file:
```
PROMPT:
What are the best practices for crane maintenance?

RESPONSE:
[Full AI response here...]
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
- Solution: Install the package with `pip install openai`

### "AuthenticationError: Incorrect API key provided"
- Solution: Double-check that you've correctly copied your API key from OpenAI
- Make sure there are no extra spaces or quotes in the key

### "RateLimitError: You exceeded your current quota"
- Solution: Check your OpenAI account billing and usage limits at https://platform.openai.com/account/usage

### Permission Errors Creating the `responses/` Directory
- Solution: Make sure you have write permissions in the scripts directory
- Try running: `mkdir responses` manually first

## Customization Options

You can modify the script to:

### Change the Model
Replace `"gpt-4"` with other models like:
- `"gpt-3.5-turbo"` (faster, cheaper)
- `"gpt-4-turbo"` (newer, more capable)

```python
response_stream = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Changed from gpt-4
    messages=[{"role": "user", "content": prompt}],
    stream=True
)
```

### Change the Log Directory
Change the `LOG_DIR` variable at the top:
```python
LOG_DIR = "my_ai_conversations"  # Instead of "responses"
```

### Add System Instructions
Modify the messages to include a system prompt:
```python
messages=[
    {"role": "system", "content": "You are a helpful crane operation expert."},
    {"role": "user", "content": prompt}
],
```

## Cost Considerations

OpenAI API usage is billed based on tokens (roughly 4 characters = 1 token):
- **GPT-4**: More expensive, highest quality
- **GPT-3.5-turbo**: Much cheaper, still very good

Check current pricing at: https://openai.com/pricing

## Security Best Practices

1. **Never commit your API key to git** - The `.gitignore` file is already configured to exclude API keys
2. **Use environment variables** for production use
3. **Rotate your keys regularly** if you're sharing your computer
4. **Monitor your usage** on the OpenAI dashboard

## Need More Help?

If you're using:
- **VS Code**: Open the terminal inside VS Code (View → Terminal) and run the commands there
- **PyCharm**: Use the built-in terminal at the bottom of the screen
- **Plain Terminal**: Navigate to the project directory first with `cd`

Questions or issues? Check the OpenAI documentation: https://platform.openai.com/docs
