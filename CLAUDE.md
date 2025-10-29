<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A lightweight CMS (Content Management System) built with Flask, featuring:
- Article management with rich text editor (Quill.js) and cover image support
- Video management with local files and external links
- Image management with upload and gallery features
- RESTful API for all content types
- Bootstrap 5-based responsive admin interface

## Quick Start

### Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Start development server
python app.py

# Access points:
# - Frontend: http://localhost:8080/
# - Admin: http://localhost:8080/admin/login
# - Default credentials: admin / admin
```

### Development Commands

```bash
# Run single test (if tests added)
python -m pytest tests/

# Check code formatting
python -m flake8

# Create database migrations (if using Flask-Migrate)
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Architecture

### Technology Stack
- **Backend**: Flask 3.0.0 + SQLAlchemy 3.1.1
- **Database**: SQLite (cms.db)
- **Frontend**: Bootstrap 5 + Quill.js (rich text editor)
- **Icons**: Font Awesome 6.4.0
- **Image Processing**: Pillow 10.0.0

### Key Files

```
cms/
├── app.py              # Main Flask application with all routes and business logic
├── models.py           # SQLAlchemy database models (Article, Video, Image)
├── requirements.txt    # Python dependencies
├── cms.db             # SQLite database (auto-created)
├── static/            # Static assets (CSS, JS, uploads)
│   └── uploads/
│       ├── images/    # Uploaded image files
│       ├── videos/    # Uploaded video files
│       └── thumbnails/
└── templates/         # Jinja2 HTML templates
    ├── base.html      # Base template
    ├── index.html     # Homepage
    ├── admin/         # Admin interface templates
    │   ├── base.html
    │   ├── login.html
    │   ├── dashboard.html
    │   ├── articles.html
    │   ├── article_edit.html  # Includes cover image picker JavaScript
    │   ├── videos.html
    │   ├── video_edit.html
    │   ├── images.html
    │   └── image_upload.html
    └── [content templates]  # Article, video, image detail pages
```

### Core Application Structure

**Main Application (app.py)**:
- Routes organized by feature (articles, videos, images, admin, API)
- Authentication via simple session-based login
- File upload handling with validation
- Base64 image checking for content size limits (500KB per image, 2MB total)
- Request size validation (50MB max)

**Database Models (models.py)**:
- **Article**: Title, slug, content (HTML), excerpt, cover_image, category, tags, status
- **Video**: Title, slug, description, video_url, thumbnail, duration, category, tags
- **Image**: Title, slug, filename, filepath, file_size, mime_type, dimensions, category, tags
- **MenuItem**: Label, url, icon, order, visible, parent_id (supports hierarchical menus)

### Admin Interface

The admin interface is located at `/admin/` and requires login (admin/admin).

**Key Features**:
- Dashboard with statistics
- CRUD operations for all content types
- Rich text editor for articles (Quill.js)
- Cover image picker for articles:
  - Select from existing images in library
  - Upload new images (<500KB for direct upload)
  - Remove existing cover images
- Image upload with file validation
- Category and tag management
- **Menu Management**:
  - Dynamic navigation menu system
  - Drag-and-drop reordering
  - Support for icons (Font Awesome)
  - Hierarchical menu support (2 levels)
  - Show/hide menu items

## API Endpoints

RESTful API available at `/api/`:

```bash
# Articles
GET  /api/articles              # List all published articles
GET  /api/articles/<slug>       # Get specific article

# Videos
GET  /api/videos                # List all published videos
GET  /api/videos/<slug>         # Get specific video

# Images
GET  /api/images                # List all published images
GET  /api/images/<slug>         # Get specific image

# Menu Items
GET  /api/menu-items            # Get visible menu items (for frontend)
GET  /api/admin/menu-items      # Get all menu items (admin)
POST /api/admin/menu-items      # Create new menu item
PUT  /api/admin/menu-items/<id> # Update menu item
DELETE /api/admin/menu-items/<id> # Delete menu item
POST /api/admin/menu-items/reorder # Reorder menu items
```

All API responses return JSON with model data via the `to_dict()` method.

## Database

SQLite database is automatically created on first run. To reset:

```bash
# Stop the application
# Delete database file
rm cms.db

# Restart application (will recreate empty database)
python app.py
```

## Development Notes

### Recent Fixes and Features

1. **Cover Image System** (article_edit.html):
   - JavaScript functions in global scope for onclick handlers
   - Bootstrap modal for image selection from library
   - File upload with size validation (<500KB for direct upload)
   - Base64 and server-side image handling
   - URL path normalization (/static/ prefix handling)

2. **File Upload Security**:
   - Extension validation (only allowed image/video types)
   - File type verification (actual file content check)
   - Size limits: 500KB per Base64 image, 2MB total for article content
   - Maximum request size: 50MB
   - Maximum file size: 1GB (configurable)

3. **Browser Cache Considerations**:
   - Frontend changes may require hard refresh (Ctrl+Shift+R)
   - Use incognito mode to avoid cached content during development

### Common Development Tasks

**Adding a New Content Type**:
1. Create model in `models.py` with `to_dict()` method
2. Add routes in `app.py` (list, detail, admin CRUD)
3. Create templates in `templates/admin/` and `templates/`
4. Add API endpoints
5. Update navigation in admin base template

**Modifying Database Schema**:
1. Edit model in `models.py`
2. Delete `cms.db` to reset database
3. Restart application

**Adding New Admin Features**:
1. Create route with `@login_required` decorator
2. Create template in `templates/admin/`
3. Update navigation in `templates/admin/base.html`

**Managing Navigation Menu**:
1. Access menu management at `/admin/menu-management`
2. Add new menu items with label, URL, and icon
3. Drag-and-drop to reorder menu items
4. Create sub-menus by setting parent menu
5. Toggle visibility to show/hide menu items
6. Default menus auto-created on first run: 首页, 文章, 视频, 图片

### Testing

A test page is available at `/test-js` to verify JavaScript functionality for:
- Image picker modal
- API connectivity
- File upload interface

### File Organization

**Static Files**: Stored in `static/uploads/`
- Images: `uploads/images/<filename>`
- Videos: `uploads/videos/<filename>`
- Thumbnails: `uploads/thumbnails/<filename>`

**Templates**: Jinja2 templates with Bootstrap 5
- Extend `base.html` for consistent layout
- Admin templates extend `admin/base.html`
- Use `url_for()` for all internal links

## Configuration

Key configuration in `app.py`:

```python
# File upload limits
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1GB
app.config['MAX_REQUEST_LENGTH'] = 1024 * 1024 * 1024   # 1GB

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'

# Allowed extensions
app.config['ALLOWED_EXTENSIONS'] = {
    'images': {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'svg'},
    'videos': {'mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mkv'},
}
```

## Troubleshooting

**"Function not defined" errors**:
- Ensure JavaScript functions are in global scope (not inside DOMContentLoaded)
- Check template includes the script block

**Images not displaying**:
- Verify file exists in `static/uploads/`
- Check path is correct (should have `/static/` prefix for URLs)
- Clear browser cache (Ctrl+Shift+R)

**Upload errors**:
- Check file size limits (500KB for Base64, 1GB for file uploads)
- Verify allowed extensions
- Ensure `static/uploads/` directory is writable

**Database issues**:
- Delete `cms.db` to reset
- Check model changes are reflected in database

## Production Considerations

Before deploying to production:
1. Change `SECRET_KEY` in `app.py`
2. Replace SQLite with PostgreSQL/MySQL
3. Implement proper user authentication system
4. Add CSRF protection
5. Configure HTTPS
6. Set up proper file storage (cloud storage for uploads)
7. Add caching layer (Redis/Memcached)
8. Implement rate limiting
9. Add logging and monitoring

## Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- Bootstrap 5: https://getbootstrap.com/docs/5.3/
- Quill.js: https://quilljs.com/
