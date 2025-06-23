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

## Deployment

### Deploying to Render

1. Push the repository to a Git provider supported by Render (GitHub, GitLab, or Bitbucket).
2. Log in to [Render](https://render.com/) and click **New Web Service**.
3. Connect your repository and choose **Node** as the runtime.
4. Set the **Build Command** to `npm install` and the **Start Command** to `npm start`.
5. Under **Environment Variables**, add `OPENAI_API_KEY` with your API key value.
6. Click **Create Web Service** to deploy. Render will build and run the server.

### Deploying to Vercel

1. Install the [Vercel CLI](https://vercel.com/docs/cli) and run `vercel login` to authenticate.
2. From the project directory, run `vercel` and follow the prompts to create a new project.
3. When asked for the **build command**, enter `npm install` and for the **output directory** leave it blank.
4. In the Vercel dashboard under **Settings → Environment Variables**, add `OPENAI_API_KEY` with your API key.
5. After the initial deploy, pushes to the connected repository will trigger automatic redeploys.
