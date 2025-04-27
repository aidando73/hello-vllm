```bash
conda create --prefix ./env -y python=3.10
conda activate ./env
pip install uv
uv pip install vllm
cp ~/.runpod_credentials .envrc
direnv allow

# Deploy phi-3-vision model on VLLM

vllm serve microsoft/Phi-3-vision-128k-instruct


curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| tee /etc/apt/sources.list.d/ngrok.list \
	&& apt update \
	&& apt install ngrok

ngrok config add-authtoken $NGROK_TOKEN

ngrok http --url=lasting-swan-large.ngrok-free.app 80
```