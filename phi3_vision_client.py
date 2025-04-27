import requests
import json

def query_phi3_vision():
    # API endpoint
    url = "https://lasting-swan-large.ngrok-free.app/v1/chat/completions"
    
    # Headers
    headers = {
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "model": "microsoft/Phi-3-vision-128k-instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Can you describe this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 1024,
        "temperature": 0.7
    }
    
    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=payload)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse and print the response
        result = response.json()
        
        # Extract and print the assistant's response
        assistant_message = result["choices"][0]["message"]["content"]
        print("\nPhi-3 Vision Response:")
        print("-" * 50)
        print(assistant_message)
        print("-" * 50)
        
        # Print full JSON response for debugging (optional)
        print("\nFull API Response:")
        print(json.dumps(result, indent=2))
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return None

if __name__ == "__main__":
    print("Sending request to Phi-3 Vision model...")
    query_phi3_vision() 