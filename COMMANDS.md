```bash
conda create --prefix ./env -y python=3.10
conda activate ./env
pip install uv
uv pip install vllm
cp ~/.runpod_credentials .envrc
direnv allow
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| tee /etc/apt/sources.list.d/ngrok.list \
	&& apt update \
	&& apt install ngrok
ngrok config add-authtoken $NGROK_TOKEN

# Deploy phi-3-vision model on VLLM
vllm serve microsoft/Phi-3-vision-128k-instruct \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --disable-sliding-window \
    --max-num-batched-tokens 12288 \
    --max-num-seqs 16 \
    --mm-processor-kwargs "{\"num_crops\": 16}" \
    --trust-remote-code \
    --gpu-memory-utilization 0.95

ngrok http --url=lasting-swan-large.ngrok-free.app 8000

python phi3_vision_client.py
```