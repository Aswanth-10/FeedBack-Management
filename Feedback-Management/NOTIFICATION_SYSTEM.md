# Notification System Documentation

## Overview

The notification system provides real-time notifications for feedback form creators when new responses are submitted. It includes both WebSocket-based real-time updates and persistent notification storage in the database.

## Features

### 🎯 Core Features
- **Real-time notifications** via WebSocket
- **Persistent storage** of notifications in database
- **Visual indicators** with animated bell icon and badge
- **Browser notifications** (with permission)
- **Toast notifications** for immediate feedback
- **Click to mark as read** functionality
- **Navigation to responses** when clicking new response notifications

### 🔔 Notification Types
- `new_response` - When a new feedback response is submitted
- `form_created` - When a new form is created
- `form_updated` - When a form is updated
- `analytics_update` - When analytics are updated

## Architecture

### Backend Components

#### 1. Models (`feedback_app/models.py`)
```python
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=dict, blank=True)
```

#### 2. WebSocket Consumers (`feedback_app/consumers.py`)
- `NotificationConsumer` - Handles real-time notifications
- `FormAnalyticsConsumer` - Handles analytics updates
- Custom authentication middleware for WebSocket connections

#### 3. API Views (`feedback_app/views.py`)
- `NotificationViewSet` - CRUD operations for notifications
- Automatic notification creation when responses are submitted
- WebSocket integration for real-time updates

### Frontend Components

#### 1. Notification Context (`contexts/NotificationContext.tsx`)
- Manages notification state
- Handles WebSocket connections
- Provides notification functions

#### 2. Notification Panel (`components/NotificationsPanel.tsx`)
- Displays list of notifications
- Mark as read functionality
- Navigation to responses

#### 3. Layout Component (`components/Layout.tsx`)
- Notification bell icon with badge
- Animated indicators for unread notifications

## Setup Instructions

### 1. Backend Setup

Ensure the following dependencies are installed:
```bash
pip install channels channels-redis django-cors-headers
```

### 2. Frontend Setup

The notification system is already integrated into the React frontend.

### 3. WebSocket Configuration

The WebSocket routing is configured in:
- `feedback_api/asgi.py` - ASGI application setup
- `feedback_app/routing.py` - WebSocket URL patterns
- `feedback_app/middleware.py` - Custom authentication middleware

## Usage

### For Form Creators

1. **View Notifications**: Click the bell icon in the top-right corner
2. **Mark as Read**: Click on any unread notification to mark it as read
3. **Navigate to Responses**: Click on new response notifications to view responses
4. **Mark All as Read**: Use the "Mark all read" button in the notification panel

### For Developers

#### Adding New Notification Types

1. **Backend**: Add new notification type to `NOTIFICATION_TYPES` in models
2. **Frontend**: Update the `Notification` type interface
3. **WebSocket**: Add handling for new notification type in consumer

#### Testing Notifications

Use the test script:
```bash
python test_notification.py
```

## Technical Details

### WebSocket Authentication

The system uses token-based authentication for WebSocket connections:
- Tokens are passed as query parameters
- Custom middleware validates tokens
- Anonymous users are rejected

### Database Integration

Notifications are stored in the database and can be:
- Retrieved via REST API
- Updated via WebSocket
- Marked as read individually or in bulk

### Real-time Updates

The system provides real-time updates through:
1. **WebSocket connections** for immediate updates
2. **Database persistence** for reliability
3. **Fallback mechanisms** for connection issues

## Troubleshooting

### Common Issues

1. **WebSocket Connection Failed**
   - Check if backend server is running
   - Verify WebSocket URL configuration
   - Check browser console for errors

2. **Notifications Not Appearing**
   - Verify WebSocket connection is established
   - Check browser notification permissions
   - Ensure user is authenticated

3. **Database Notifications Missing**
   - Check if notification records are being created
   - Verify database migrations
   - Check server logs for errors

### Debug Steps

1. **Check WebSocket Connection**:
   ```javascript
   // In browser console
   websocketService.isConnected()
   ```

2. **Check Notification Count**:
   ```javascript
   // In browser console
   const { unreadCount } = useNotifications()
   console.log('Unread count:', unreadCount)
   ```

3. **Test API Endpoints**:
   ```bash
   curl http://localhost:8000/api/notifications/
   curl http://localhost:8000/api/notifications/unread_count/
   ```

## Performance Considerations

- **WebSocket connections** are user-specific and lightweight
- **Database queries** are optimized with proper indexing
- **Notification cleanup** can be implemented for old notifications
- **Rate limiting** should be considered for high-traffic scenarios

## Security

- **Authentication required** for all notification operations
- **User-specific notifications** - users only see their own notifications
- **Token-based WebSocket auth** prevents unauthorized access
- **CORS configuration** restricts cross-origin requests

## Future Enhancements

- [ ] Email notifications
- [ ] Push notifications for mobile
- [ ] Notification preferences/settings
- [ ] Notification categories and filtering
- [ ] Bulk notification operations
- [ ] Notification analytics and reporting 