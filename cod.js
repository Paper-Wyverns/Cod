const http = require('http');
const request = require('request');

const PORT = 9097;

const server = http.createServer((req, res) => {
  if(req.method === 'GET') {
    handleRequest(req, res);
  }
});

function handleRequest(req, res) {
  const url = req.url.slice(1);

  req.pipe(request(url)).pipe(res);
}

server.listen(PORT);
console.log(`Proxy server running on port ${PORT}`);