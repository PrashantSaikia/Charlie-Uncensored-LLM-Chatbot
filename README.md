# Charlie-Uncensored-LLM-Chatbot

## 0. Stop and remove running containers and networks
```
docker stop ollama
docker rm ollama
docker stop gradio-app
sudo systemctl stop ollama.service
sudo netstat -tulnp | grep 11434
docker network rm my-net
```

## 1. Execute the following commands
```
git clone https://github.com/PrashantSaikia/Charlie-Uncensored-LLM-Chatbot.git
cd Gradio-Ollama-Chatbot/
docker network create my-net
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama --net my-net ollama/ollama
docker exec ollama ollama run kristada673/solar-10.7b-instruct-v1.0-uncensored
docker build -t app .
export OLLAMA_API_ENDPOINT=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ollama)
docker run -d -p 8080:8080 -e OLLAMA_API_ENDPOINT --rm --name gradio-app --net my-net app
```
Need to create a docker network so the two containers (one for the Ollama server and one for the app UI) can talk to each other. Then, need to set the URL for the Ollama server in `app.py` as the IP address on which the Ollama container is running. Screenshot of the app running successfully:

<img width="909" alt="Screenshot 2024-04-05 at 4 30 20 PM" src="https://github.com/input-output-hk/Charlie-Uncensored-LLM-Chatbot/assets/39755678/95327684-eee9-41d1-931a-591e51be0601">
