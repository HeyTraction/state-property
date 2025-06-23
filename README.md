# TikTok Script Generator

Utilities for generating short-form video scripts using predefined brand voices.

## Installation

```bash
pip install -e .
```

## Usage

Run the command line interface and provide bullet points:

```bash
python -m tiktok_script_generator.cli "Awesome product" "Call to action" --voice enthusiastic
```

This will output a simple TikTok script with the selected brand voice.


## Deployment

The repository can be deployed as an Express application on platforms such as **Vercel** or **Heroku**.

### Vercel
1. Install the Vercel CLI with `npm i -g vercel`.
2. Run `vercel` in the project directory and follow the prompts.

### Heroku
1. Create a Heroku app using `heroku create`.
2. Push your code with `git push heroku main` to deploy.
