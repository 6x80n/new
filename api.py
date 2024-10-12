import os
import subprocess

def handler(request):
    # You can add logic to handle requests here if needed

    # Run the bot script
    result = subprocess.run(['bash bot.sh'], capture_output=True, text=True)
    
    return {
        "statusCode": 200,
        "body": result.stdout,
    }
