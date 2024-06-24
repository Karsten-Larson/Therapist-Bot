# Therapist Bot

This bot uses Google Gemini API keys. Get your key at [https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key).

Then create a file under the `./src` folder named `.env`. The file will contain text formatted as this:

```
GEMINI_API_KEY=api_key
```

Put your API key after the `=` sign.

## Installation and Running

To install all the packages necessary to run the program I would recommend creating a virtual environment. Here is a link of how to do it: [https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

This is not necessarily required but it helps keep your packages organized.

### Downloading Packages

Then enter the following command into the terminal to download the required packages.

```
pip install -r requirements.txt
```

### Running Program

Once everything is configured to run the program:

```
python -m src
```

## Organization

Create a branch before making changes to the project just to keep things organized.
