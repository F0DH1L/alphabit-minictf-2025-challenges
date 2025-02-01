import express from 'express';
import axios from 'axios';
import path from 'path';
import { fileURLToPath } from 'url';
import { BLACKLIST } from './blacklist.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = 1335;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

async function checkWebsite(url) {
    try {
        for (const blacklisted of BLACKLIST) {
            if (url.includes(blacklisted)) {
                return { msg: '', error: 'Blacklisted website!!' };
            }
        }
        const result = await axios.get(url);
        return { msg: result.data, error: '' };
    } catch (error) {
        return { msg: '', error: 'Error happened. Try again!!' };
    }
}

app.post('/view', async (req, res) => {
    const { url } = req.body;
    const { msg, error } = await checkWebsite(url);
    res.render('index', { msg, error });
});

app.get('/', (req, res) => {
    res.render('index', { msg: '', error: '' });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});