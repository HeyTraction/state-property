# State Property Copywriter

This is a small Express application providing the `State Property Copywriter` tool.

## Setup

1. Install dependencies (requires Node.js installed):

```bash
npm install
```

2. Copy `.env.example` to `.env` and fill in your OpenAI API key.

```bash
cp .env.example .env
```

3. Start the server:

```bash
npm start
```

Then open `http://localhost:3000/copywriter` in your browser.

## Usage

Enter a product URL, choose the content type and provide any additional details. The app
sends this information to the OpenAI API and returns three caption suggestions for use on social media.
