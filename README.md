# Charlie-Uncensored-LLM-Chatbot

## 1. Install Ollama
```
docker stop ollama
docker rm ollama
sudo kill -9 `sudo lsof -t -i:11434`
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

## 2. Start both the docker images for the Ollama server and the UI frontend
`docker compose up -d --build`
