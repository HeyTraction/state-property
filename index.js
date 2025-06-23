const express = require('express');
const { Configuration, OpenAIApi } = require('openai');
const path = require('path');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

app.get('/', (req, res) => {
  res.redirect('/copywriter');
});

app.get('/copywriter', (req, res) => {
  res.render('copywriter');
});

app.post('/copywriter', async (req, res) => {
  const { productUrl, contentType, details } = req.body;
  const prompt = `Generate three short social media captions in a casual tone. Product URL: ${productUrl}. Content type: ${contentType}. Additional details: ${details}`;
  try {
    const completion = await openai.createChatCompletion({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.7,
    });
    const response = completion.data.choices[0].message.content;
    res.render('results', { captions: response.split(/\n+/).filter(Boolean) });
  } catch (err) {
    console.error(err);
    res.render('results', { captions: [], error: 'Failed to generate captions.' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

