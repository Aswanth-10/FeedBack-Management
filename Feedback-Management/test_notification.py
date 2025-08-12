#!/usr/bin/env python3
"""
Test script to simulate a feedback response and test the notification system
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
API_BASE = f"{BASE_URL}/api"

def test_notification_system():
    """Test the notification system by submitting a feedback response"""
    
    print("Testing notification system...")
    
    # Step 1: Get public forms
    try:
        response = requests.get(f"{API_BASE}/public/forms/")
        if response.status_code == 200:
            forms = response.json()
            if forms:
                form = forms[0]  # Use the first available form
                print(f"Found form: {form['title']}")
                
                # Step 2: Submit a test feedback response
                feedback_data = {
                    "answers": [
                        {
                            "question": form['questions'][0]['id'],
                            "answer_text": "This is a test response",
                            "answer_value": {}
                        }
                    ]
                }
                
                response = requests.post(
                    f"{API_BASE}/public/feedback/{form['id']}/",
                    json=feedback_data
                )
                
                if response.status_code == 201:
                    print("✅ Feedback response submitted successfully!")
                    print("Notification should be sent to the form creator.")
                    return True
                else:
                    print(f"❌ Failed to submit feedback: {response.status_code}")
                    print(response.text)
                    return False
            else:
                print("❌ No forms available for testing")
                return False
        else:
            print(f"❌ Failed to get forms: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server. Make sure the backend is running.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_websocket_connection():
    """Test WebSocket connection"""
    print("\nTesting WebSocket connection...")
    
    try:
        import websocket
        import json
        
        # Create a WebSocket connection
        ws = websocket.create_connection("ws://localhost:8000/ws/notifications/")
        
        # Send a test message
        test_message = {
            "type": "test",
            "message": "Test WebSocket connection"
        }
        ws.send(json.dumps(test_message))
        
        # Wait for response
        response = ws.recv()
        print(f"✅ WebSocket response: {response}")
        
        ws.close()
        return True
        
    except ImportError:
        print("⚠️  websocket-client not installed. Install with: pip install websocket-client")
        return False
    except Exception as e:
        print(f"❌ WebSocket test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Notification System Test")
    print("=" * 40)
    
    # Test feedback submission
    success = test_notification_system()
    
    if success:
        print("\n✅ Notification system test completed!")
        print("Check the frontend to see if the notification appears.")
    else:
        print("\n❌ Notification system test failed!")
    
    # Test WebSocket
    test_websocket_connection()
    
    print("\n📝 Instructions:")
    print("1. Make sure both backend and frontend servers are running")
    print("2. Open the frontend in your browser")
    print("3. Look for the notification bell icon in the top right")
    print("4. The notification should appear when a feedback response is submitted") 