import 'dotenv/config';
import express from 'express';

const app = express();
const port = 8088;

app.get('/flag', (req, res) => {
    res.send(`GG here is your flags: ${process.env.FLAG}`);
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}/flag`);
});
