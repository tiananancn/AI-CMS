# AI-CMS Project - QWEN Context

## Project Overview

This is an AI Content Management System (CMS) built with Flask, designed to support content creation and management for articles, videos, and images. The system includes a comprehensive backend management interface, dynamic page creation capabilities, and a flexible frontend with customizable layouts.

**Project Type**: Full-stack web application (Flask-based CMS)

**Main Technologies**:
- **Backend Framework**: Flask 3.0.0
- **Database**: SQLAlchemy with SQLite
- **Frontend Framework**: Bootstrap 5
- **Rich Text Editor**: Quill.js
- **Icons**: Font Awesome
- **File Handling**: Werkzeug, Pillow

## Key Features

### Content Management
- **Article Management**: Create, edit, delete articles with rich text editor, categories, tags, and cover images
- **Video Management**: Manage video content with support for local files and external links
- **Image Management**: Upload and manage images with automatic metadata extraction
- **Dynamic Pages**: Create custom pages with drag-and-drop content blocks
- **Homepage Configuration**: Customize homepage layout and sections

### Advanced Features
- **Menu Management**: Dynamic menu system with multi-level support
- **Grid Editor**: Visual editing capabilities for dynamic pages
- **Customizable Layouts**: Configure homepage sections and ordering
- **API Endpoints**: RESTful API for all content types
- **File Upload**: Support for images, videos and other media files

### Technical Capabilities
- **Content Blocks**: Drag-and-drop page building with various block types
- **Responsive Design**: Mobile-friendly interface
- **View Tracking**: Built-in analytics for content views
- **Base64 Image Handling**: Optimized processing of embedded images
- **File Validation**: Comprehensive file type and size checking

## Project Structure

```
cms/
├── app.py                 # Main Flask application with all routes
├── models.py              # Database models (Article, Video, Image, etc.)
├── static/                # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── uploads/           # User uploaded files
│       ├── images/        # Image uploads
│       ├── videos/        # Video uploads
│       └── thumbnails/    # Generated thumbnails
├── templates/             # Jinja2 templates
│   ├── admin/             # Backend admin templates
│   └── *.html             # Frontend page templates
├── requirements.txt       # Python dependencies
├── start.sh               # Startup script
├── demo.py                # API demonstration script
├── README.md              # User documentation
└── various .md files      # Development documentation and reports
```

## Database Models

The system includes several models for managing different content types:

- **Article**: Stores articles with title, content, cover image, categories, tags
- **Video**: Manages video content with URL, description, and metadata
- **Image**: Handles image uploads with file information and metadata
- **DynamicPage**: Creates custom pages with configurable content
- **ContentBlock**: Provides drag-and-drop content blocks for pages
- **HomepageConfig**: Allows customization of homepage layout
- **MenuItem**: Supports dynamic menu management with multi-level structure

## Building and Running

### Installation Requirements
- Python 3.7+
- pip

### Setup Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Start the application
./start.sh
# OR
python app.py
```

### Access Information
- **Frontend**: http://localhost:8080
- **Admin Panel**: http://localhost:8080/admin/login
- **Default Credentials**: admin / admin

### API Endpoints
- `GET /api/articles` - Get all articles
- `GET /api/articles/<slug>` - Get specific article
- `GET /api/videos` - Get all videos
- `GET /api/videos/<slug>` - Get specific video
- `GET /api/images` - Get all images
- `GET /api/images/<slug>` - Get specific image
- `GET /api/dynamic-pages` - Get all dynamic pages
- Admin APIs for managing content and configuration

## Development Conventions

### Code Organization
- **Routes**: Organized by functionality in app.py
- **Models**: Defined in models.py with SQLAlchemy
- **Templates**: Separated into admin and public directories
- **Static Assets**: Organized by file type in static directory

### Security Features
- Basic authentication for admin panel
- File upload validation and size limits
- Base64 image size checking in content
- Input sanitization for content management

### Content Management
- Automatic slug generation for URLs
- Support for draft and published content
- View counting for analytics
- Category and tag management

## Special Features

### Dynamic Page Builder
- Grid-based page layout editor
- Drag-and-drop content blocks
- Multiple block types (text, image, video, etc.)

### Homepage Customization
- Configurable section ordering
- Toggle visibility of sections
- Customizable hero section

### Menu System
- Multi-level menu support
- Dynamic menu management
- Icon integration with Font Awesome

## Development Notes

### Current Status
- Production ready for basic CMS functionality
- Advanced features like drag-and-drop editor implemented
- Responsive design working across devices

### Next Steps (Planned)
- User authentication system
- Multi-user support
- Comment system
- SEO optimization
- Search functionality
- Theme system
- Plugin system

### File Upload Limits
- Up to 1GB file size for uploads
- Base64 image validation (max 500KB per image, 2MB total per article)

## Usage Guidelines

### For Content Creators
1. Log into admin panel with credentials
2. Use rich text editor to create articles
3. Upload images and videos for content
4. Configure pages with drag-and-drop editor
5. Customize homepage layout as needed

### For Developers
1. Use virtual environment for dependencies
2. Follow existing code patterns for consistency
3. Test API endpoints with demo.py script
4. Extend functionality through content blocks
5. Add new templates following Bootstrap 5 patterns