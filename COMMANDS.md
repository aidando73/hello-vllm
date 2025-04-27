```bash
conda create --prefix ./env -y python=3.10
conda activate ./env


# Deploy phi-3-vision model on VLLM
cp ~/.runpod_credentials ./.envrc

curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| tee /etc/apt/sources.list.d/ngrok.list \
	&& apt update \
	&& apt install ngrok

ngrok config add-authtoken $NGROK_TOKEN

ngrok http --url=lasting-swan-large.ngrok-free.app 80
```